use anyhow::Result;
use baml_runtime::RuntimeCliDefaults;

const UPSTREAM_VERSION: &str = "0.208.5";
const UPSTREAM_COMMIT: &str = "main";
const PATCH_VERSION: &str = "1";

fn main() -> Result<()> {
    baml_log::init()?;

    let argv: Vec<String> = std::env::args().collect();

    baml_cli::run_cli(
        argv,
        RuntimeCliDefaults {
            output_type: baml_types::GeneratorOutputType::OpenApi,
        },
    )?;
    Ok(())
}
