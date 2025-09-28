use anyhow::Result;
use baml_types::{BamlValue, BamlValueWithMeta};
use colored::*;
use jsonish::{
    deserializer::deserialize_flags::Flag, BamlValueWithFlags, ResponseBamlValue, SerializeMode,
};

pub use crate::internal::llm_client::LLMResponse;
use crate::{
    errors::ExposedError,
    internal::llm_client::{orchestrator::OrchestrationScope, ErrorCode},
    test_constraints::TestConstraintsResult,
};

#[derive(Debug)]
pub struct FunctionResult {
    event_chain: Vec<(
        OrchestrationScope,
        LLMResponse,
        Option<Result<ResponseBamlValue>>,
    )>,
}

impl std::fmt::Display for FunctionResult {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // print out the number of previous tries only if there was more than 1
        if self.event_chain.len() > 1 {
            writeln!(
                f,
                "{}",
                format!("({} other previous tries)", self.event_chain.len() - 1).yellow()
            )?;
        }
        writeln!(f, "{}", self.llm_response())?;
        match &self.result_with_constraints() {
            Some(Ok(val)) => {
                writeln!(
                    f,
                    "{}",
                    format!("---Parsed Response ({})---", val.0.r#type()).blue()
                )?;
                write!(f, "{:#}", serde_json::json!(val.serialize_partial()))
            }
            Some(Err(e)) => {
                writeln!(f, "{}", "---Parsed Response---".blue())?;
                write!(f, "{}", e.to_string().red())
            }
            None => Ok(()),
        }
    }
}

impl FunctionResult {
    pub fn new(
        scope: OrchestrationScope,
        response: LLMResponse,
        baml_value: Option<Result<ResponseBamlValue>>,
    ) -> Self {
        Self {
            event_chain: vec![(scope, response, baml_value)],
        }
    }

    pub(crate) fn event_chain(
        &self,
    ) -> &Vec<(
        OrchestrationScope,
        LLMResponse,
        Option<Result<ResponseBamlValue>>,
    )> {
        &self.event_chain
    }

    pub fn new_chain(
        chain: Vec<(
            OrchestrationScope,
            LLMResponse,
            Option<Result<ResponseBamlValue>>,
        )>,
    ) -> Result<Self> {
        if chain.is_empty() {
            anyhow::bail!("No events in the chain");
        }

        Ok(Self { event_chain: chain })
    }

    pub fn content(&self) -> Result<&str> {
        self.llm_response().content()
    }

    pub fn llm_response(&self) -> &LLMResponse {
        &self.event_chain.last().unwrap().1
    }

    pub fn scope(&self) -> &OrchestrationScope {
        &self.event_chain.last().unwrap().0
    }

    pub fn parsed(&self) -> &Option<Result<ResponseBamlValue>> {
        let last = self.event_chain.last();
        match last {
            Some((_, _, result)) => result,
            None => &None,
        }
    }

    pub fn result_with_constraints(&self) -> &Option<Result<ResponseBamlValue>> {
        match self.event_chain.last() {
            Some((_, _, result)) => result,
            None => &None,
        }
    }

    pub fn result_with_constraints_content(&self) -> Result<&ResponseBamlValue> {
        self.result_with_constraints()
            .as_ref()
            .map(|res| match res {
                Ok(val) => Ok(val),
                Err(err) => Err(anyhow::anyhow!(self.format_last_error_with_details(err))),
            })
            .unwrap_or_else(|| Err(anyhow::anyhow!("No result from baml - Please report this error to our team with BAML_LOG=info enabled so we can improve this error message")))
    }

    fn format_last_error_with_details(&self, last_error: &anyhow::Error) -> ExposedError {
        let detailed_message = self.create_detailed_message();

        if let Some(exposed_error) = last_error.downcast_ref::<ExposedError>() {
            return self.add_detailed_message_to_exposed(exposed_error.clone(), detailed_message);
        }

        self.add_detailed_message_to_exposed(self.format_single_error(last_error), detailed_message)
    }

    fn format_single_error(&self, err: &anyhow::Error) -> ExposedError {
        if let Some(exposed_error) = err.downcast_ref::<ExposedError>() {
            return exposed_error.clone();
        }

        // Capture the actual error to preserve its details
        let actual_error = err.to_string();

        // TODO: HACK! Figure out why now connection errors dont get converted into ExposedError. Instead of converting to a validation error, check for connection errors here. We probably are missing a lot of other connection failures that should NOT be validation errors.
        if actual_error.to_lowercase().contains("connecterror")
            || actual_error
                .to_lowercase()
                .contains("profilefile provider could not be built")
            || actual_error
                .to_lowercase()
                .contains("session token not found")
        {
            return ExposedError::ClientHttpError {
                client_name: match self.llm_response() {
                    LLMResponse::Success(resp) => resp.client.clone(),
                    LLMResponse::LLMFailure(err) => err.client.clone(),
                    _ => "unknown".to_string(),
                },
                detailed_message: actual_error.clone(),
                message: actual_error,
                status_code: ErrorCode::ServiceUnavailable,
            };
        }
        let message = match self.llm_response() {
            LLMResponse::Success(_) => {
                format!("Failed to parse LLM response: {actual_error}")
            }
            LLMResponse::LLMFailure(err) => format!(
                "LLM Failure: {} ({}) - {}",
                err.message, err.code, actual_error
            ),
            LLMResponse::UserFailure(err) => {
                format!("User Failure: {err} - {actual_error}")
            }
            LLMResponse::InternalFailure(err) => {
                format!("Internal Failure: {err} - {actual_error}")
            }
            LLMResponse::Cancelled(err) => {
                format!("Operation Cancelled: {err} - {actual_error}")
            }
        };
        ExposedError::ValidationError {
            prompt: match self.llm_response() {
                LLMResponse::Success(resp) => resp.prompt.to_string(),
                LLMResponse::LLMFailure(err) => err.prompt.to_string(),
                _ => "N/A".to_string(),
            },
            raw_output: self
                .llm_response()
                .content()
                .unwrap_or_default()
                .to_string(),
            // The only branch that should be hit is LLMResponse::Success(_) since we
            // only call this function when we have a successful response.
            detailed_message: message.clone(),
            message,
        }
    }

    fn create_detailed_message(&self) -> String {
        let error_vec = self
            .event_chain
            .iter()
            .enumerate()
            .filter_map(|(index, (_, _, parse_result))| {
                let Some(Err(err)) = parse_result else {
                    return None;
                };
                Some(self.format_single_error(err).to_string())
            })
            .collect::<Vec<String>>();

        match error_vec.len() {
            0 => String::new(),
            1 => error_vec[0].clone(),
            _ => format!(
                "{} failed attempts:\n\n{}",
                error_vec.len(),
                error_vec
                    .into_iter()
                    .enumerate()
                    .map(|(index, error)| format!(
                        "Attempt {}: {}",
                        index,
                        error.replace("\n", "\n    ")
                    ))
                    .collect::<Vec<String>>()
                    .join("\n")
            ),
        }
    }

    fn add_detailed_message_to_exposed(
        &self,
        mut error: ExposedError,
        detail: String,
    ) -> ExposedError {
        match &mut error {
            ExposedError::ValidationError {
                detailed_message: ref mut prev,
                ..
            } => *prev = detail,
            ExposedError::FinishReasonError {
                detailed_message: ref mut prev,
                ..
            } => *prev = detail,
            ExposedError::ClientHttpError {
                detailed_message: ref mut prev,
                ..
            } => *prev = detail,
            ExposedError::AbortError {
                detailed_message: ref mut prev,
            } => *prev = detail,
        }
        error
    }
}

#[derive(Debug)]
pub struct TestResponse {
    pub function_response: FunctionResult,
    pub function_call: baml_ids::FunctionCallId,
    pub constraints_result: TestConstraintsResult,
}

impl std::fmt::Display for TestResponse {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{}", self.function_response)
    }
}

#[derive(Debug, PartialEq, Eq)]
/// A test may result in one of 3 following states:
///
///   1. pass
///   2. at least one @check failed
///   3. at least one @assert failed
///
/// NeedsHumanEval corresponds to (2) and Fail corresponds to (3).
///
/// (There was a broader design conversation when we made this decision about
/// value transforms and what it means for a check to "fail".)
pub enum TestStatus<'a> {
    Pass,
    NeedsHumanEval(Vec<String>),
    Fail(TestFailReason<'a>),
}

impl From<TestStatus<'_>> for BamlValue {
    fn from(status: TestStatus) -> Self {
        match status {
            TestStatus::Pass => BamlValue::String("pass".to_string()),
            TestStatus::NeedsHumanEval(checks) => {
                BamlValue::String(format!("checks need human evaluation: {checks:?}"))
            }
            TestStatus::Fail(r) => BamlValue::String(format!("failed! {r:?}")),
        }
    }
}

#[derive(Debug)]
pub enum TestFailReason<'a> {
    TestUnspecified(anyhow::Error),
    TestLLMFailure(&'a LLMResponse),
    TestParseFailure(&'a anyhow::Error),
    TestFinishReasonFailed(&'a anyhow::Error),
    TestConstraintsFailure {
        checks: Vec<(String, bool)>,
        failed_assert: Option<String>,
    },
}

impl PartialEq for TestFailReason<'_> {
    fn eq(&self, other: &Self) -> bool {
        match (self, other) {
            (Self::TestUnspecified(a), Self::TestUnspecified(b)) => a.to_string() == b.to_string(),
            (Self::TestLLMFailure(_), Self::TestLLMFailure(_)) => true,
            (Self::TestParseFailure(a), Self::TestParseFailure(b)) => {
                a.to_string() == b.to_string()
            }
            (Self::TestFinishReasonFailed(a), Self::TestFinishReasonFailed(b)) => {
                a.to_string() == b.to_string()
            }
            _ => false,
        }
    }
}

impl Eq for TestFailReason<'_> {}

impl TestResponse {
    pub fn status(&self) -> TestStatus<'_> {
        let func_res = &self.function_response;
        if let Some(parsed) = func_res.result_with_constraints() {
            if parsed.is_ok() {
                match self.constraints_result.clone() {
                    TestConstraintsResult::InternalError { details } => {
                        TestStatus::Fail(TestFailReason::TestUnspecified(anyhow::anyhow!(details)))
                    }
                    TestConstraintsResult::Completed {
                        checks,
                        failed_assert,
                    } => {
                        let n_failed_checks: usize =
                            checks.iter().filter(|(_, pass)| !pass).count();
                        if failed_assert.is_some() || n_failed_checks > 0 {
                            TestStatus::Fail(TestFailReason::TestConstraintsFailure {
                                checks,
                                failed_assert,
                            })
                        } else {
                            TestStatus::Pass
                        }
                    }
                }
            } else {
                let err = parsed.as_ref().unwrap_err();
                match err.downcast_ref::<crate::errors::ExposedError>() {
                    Some(ExposedError::FinishReasonError { .. }) => {
                        TestStatus::Fail(TestFailReason::TestFinishReasonFailed(err))
                    }
                    _ => TestStatus::Fail(TestFailReason::TestParseFailure(err)),
                }
            }
        } else {
            TestStatus::Fail(TestFailReason::TestLLMFailure(func_res.llm_response()))
        }
    }
}

impl std::fmt::Display for TestFailReason<'_> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::TestUnspecified(e) => write!(f, "{e}"),
            Self::TestLLMFailure(r) => write!(f, "{r}"),
            Self::TestParseFailure(e) => write!(f, "{e}"),
            Self::TestFinishReasonFailed(e) => write!(f, "{e}"),
            Self::TestConstraintsFailure {
                checks,
                failed_assert,
            } => {
                for (check, pass) in checks {
                    write!(f, "{} - {}", check, if *pass { "passed" } else { "failed" })?;
                }
                if let Some(failed_assert) = failed_assert {
                    write!(f, "{failed_assert}")?;
                }
                Ok(())
            }
        }
    }
}

#[cfg(test)]
use std::process::Termination;

// This allows tests to pass or fail based on the contents of the FunctionResult
#[cfg(test)]
impl Termination for FunctionResult {
    fn report(self) -> std::process::ExitCode {
        if self.result_with_constraints_content().is_ok() {
            std::process::ExitCode::SUCCESS
        } else {
            std::process::ExitCode::FAILURE
        }
    }
}

// This allows tests to pass or fail based on the contents of the TestResponse
#[cfg(test)]
impl Termination for TestResponse {
    fn report(self) -> std::process::ExitCode {
        if self.status() == TestStatus::Pass {
            std::process::ExitCode::SUCCESS
        } else {
            std::process::ExitCode::FAILURE
        }
    }
}
