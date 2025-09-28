use baml_runtime::{
    errors::ExposedError, internal::llm_client::LLMResponse, scope_diagnostics::ScopeStack,
};
use pyo3::{
    create_exception, pymodule,
    types::{PyAnyMethods, PyModule, PyModuleMethods},
    Bound, PyErr, PyResult, Python,
};

create_exception!(baml_py, BamlError, pyo3::exceptions::PyException);
// Existing exception definitions
// A note on custom exceptions https://github.com/PyO3/pyo3/issues/295
create_exception!(baml_py, BamlInvalidArgumentError, BamlError);
create_exception!(baml_py, BamlClientError, BamlError);
create_exception!(baml_py, BamlAbortError, BamlError);

// Define the BamlValidationError/BamlClientHttpError/BamlClientFinishReasonError exception with additional fields
// can't use extends=PyException yet https://github.com/PyO3/pyo3/discussions/3838

#[allow(non_snake_case)]
fn raise_baml_validation_error(
    prompt: String,
    message: String,
    raw_output: String,
    detailed_message: String,
) -> PyErr {
    Python::with_gil(|py| {
        let internal_monkeypatch = py.import("baml_py.internal_monkeypatch").unwrap();
        let exception = internal_monkeypatch.getattr("BamlValidationError").unwrap();
        let args = (prompt, message, raw_output, detailed_message);
        let inst = exception.call1(args).unwrap();
        PyErr::from_value(inst)
    })
}

#[allow(non_snake_case)]
fn raise_baml_client_http_error(
    client_name: String,
    message: String,
    status_code: u16,
    detailed_message: String,
) -> PyErr {
    Python::with_gil(|py| {
        let internal_monkeypatch = py.import("baml_py.internal_monkeypatch").unwrap();
        let exception = internal_monkeypatch.getattr("BamlClientHttpError").unwrap();
        let args = (client_name, message, status_code, detailed_message);
        let inst = exception.call1(args).unwrap();
        PyErr::from_value(inst)
    })
}

#[allow(non_snake_case)]
fn raise_baml_client_finish_reason_error(
    prompt: String,
    raw_output: String,
    message: String,
    finish_reason: Option<String>,
    detailed_message: String,
) -> PyErr {
    Python::with_gil(|py| {
        let internal_monkeypatch = py.import("baml_py.internal_monkeypatch").unwrap();
        let exception = internal_monkeypatch
            .getattr("BamlClientFinishReasonError")
            .unwrap();
        let args = (prompt, message, raw_output, finish_reason, detailed_message);
        let inst = exception.call1(args).unwrap();
        PyErr::from_value(inst)
    })
}

/// Defines the errors module with the BamlValidationError exception.
/// IIRC the name of this function is the name of the module that pyo3 generates (errors.py)
#[pymodule]
pub fn errors(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    parent_module.add("BamlError", parent_module.py().get_type::<BamlError>())?;
    parent_module.add(
        "BamlInvalidArgumentError",
        parent_module.py().get_type::<BamlInvalidArgumentError>(),
    )?;
    parent_module.add(
        "BamlClientError",
        parent_module.py().get_type::<BamlClientError>(),
    )?;
    parent_module.add(
        "BamlAbortError",
        parent_module.py().get_type::<BamlAbortError>(),
    )?;

    Ok(())
}

impl BamlError {
    pub fn from_anyhow(err: impl Into<anyhow::Error>) -> PyErr {
        let err = err.into();
        if let Some(er) = err.downcast_ref::<ExposedError>() {
            match er {
                ExposedError::ValidationError {
                    prompt,
                    raw_output,
                    message,
                    detailed_message,
                    ..
                } => {
                    // Assuming ValidationError has fields that correspond to prompt, message, and raw_output
                    // If not, you may need to adjust this part based on the actual structure of ValidationError
                    raise_baml_validation_error(
                        prompt.clone(),
                        message.clone(),
                        raw_output.clone(),
                        detailed_message.clone(),
                    )
                }
                ExposedError::FinishReasonError {
                    prompt,
                    raw_output,
                    message,
                    finish_reason,
                    detailed_message,
                    ..
                } => raise_baml_client_finish_reason_error(
                    prompt.clone(),
                    raw_output.clone(),
                    message.clone(),
                    finish_reason.clone(),
                    detailed_message.clone(),
                ),
                ExposedError::ClientHttpError {
                    client_name,
                    message,
                    status_code,
                    detailed_message,
                    ..
                } => raise_baml_client_http_error(
                    client_name.clone(),
                    message.clone(),
                    status_code.to_u16(),
                    detailed_message.clone(),
                ),
                ExposedError::AbortError { .. } => {
                    PyErr::new::<BamlAbortError, _>("AbortError".to_string())
                }
            }
        } else if let Some(er) = err.downcast_ref::<ScopeStack>() {
            PyErr::new::<BamlInvalidArgumentError, _>(format!("Invalid argument: {er}"))
        } else if let Some(er) = err.downcast_ref::<LLMResponse>() {
            match er {
                LLMResponse::Success(_) => {
                    PyErr::new::<BamlError, _>(format!("Unexpected error from BAML: {err}"))
                }
                LLMResponse::LLMFailure(failed) => match &failed.code {
                    baml_runtime::internal::llm_client::ErrorCode::Other(2) => {
                        PyErr::new::<BamlClientError, _>(format!(
                            "Something went wrong with the LLM client {}: {}",
                            failed.client, failed.message
                        ))
                    }
                    baml_runtime::internal::llm_client::ErrorCode::Other(_)
                    | baml_runtime::internal::llm_client::ErrorCode::InvalidAuthentication
                    | baml_runtime::internal::llm_client::ErrorCode::NotSupported
                    | baml_runtime::internal::llm_client::ErrorCode::RateLimited
                    | baml_runtime::internal::llm_client::ErrorCode::ServerError
                    | baml_runtime::internal::llm_client::ErrorCode::ServiceUnavailable
                    | baml_runtime::internal::llm_client::ErrorCode::UnsupportedResponse(_) => {
                        raise_baml_client_http_error(
                            failed.client.clone(),
                            failed.message.clone(),
                            failed.code.to_u16(),
                            String::new(),
                        )
                    }
                },
                LLMResponse::UserFailure(msg) => {
                    PyErr::new::<BamlInvalidArgumentError, _>(format!("Invalid argument: {msg}"))
                }
                LLMResponse::InternalFailure(_) => PyErr::new::<BamlClientError, _>(format!(
                    "Something went wrong with the LLM client: {err}"
                )),
                LLMResponse::Cancelled(msg) => {
                    PyErr::new::<BamlAbortError, _>(format!("Operation was aborted: {msg}"))
                }
            }
        } else {
            PyErr::new::<BamlError, _>(format!("{err:?}"))
        }
    }
}
