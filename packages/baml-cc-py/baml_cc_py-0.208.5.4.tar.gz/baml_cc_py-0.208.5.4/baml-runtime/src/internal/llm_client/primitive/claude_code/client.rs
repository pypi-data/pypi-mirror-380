use std::{collections::HashMap, path::PathBuf, process::Command as StdCommand};

use anyhow::{anyhow, Context, Result};
use baml_types::BamlMap;
use internal_baml_core::ir::ClientWalker;
use internal_baml_jinja::{
    ChatMessagePart, RenderContext_Client, RenderedChatMessage, RenderedPrompt,
};
use internal_llm_client::{
    claude_code::ResolvedClaudeCode, AllowedRoleMetadata, ClientProvider, ResolvedClientProperty,
};
#[cfg(not(target_arch = "wasm32"))]
use once_cell::sync::OnceCell;
#[cfg(not(target_arch = "wasm32"))]
use serde::Deserialize;
use serde_json::json;
use tempfile::NamedTempFile;
use tokio::time::timeout;
use web_time::{Instant, SystemTime};
#[cfg(not(target_arch = "wasm32"))]
use {std::time::Duration, tracing::warn};

use crate::{
    client_registry::ClientProperty,
    internal::llm_client::{
        primitive::request::RequestBuilder,
        traits::{
            CompletionToProviderBody, HttpContext, ToProviderMessage, ToProviderMessageExt,
            WithChat, WithClient, WithClientProperties, WithNoCompletion, WithRetryPolicy,
            WithStreamChat,
        },
        ErrorCode, LLMCompleteResponse, LLMCompleteResponseMetadata, LLMResponse, ModelFeatures,
        ResolveMediaUrls,
    },
    RuntimeContext,
};

// Removed hardcoded fallback models - using Anthropic aliases instead

#[derive(Debug, Default)]
struct LatestModels {
    opus: Option<String>,
    sonnet: Option<String>,
    haiku: Option<String>,
}

#[cfg(not(target_arch = "wasm32"))]
#[derive(Deserialize)]
struct ModelsResponse {
    data: Vec<ModelInfo>,
}

#[cfg(not(target_arch = "wasm32"))]
#[derive(Deserialize)]
struct ModelInfo {
    id: String,
    #[serde(default)]
    display_name: Option<String>,
    #[serde(default)]
    created_at: Option<String>,
    #[serde(default)]
    status: Option<String>,
}

#[cfg(not(target_arch = "wasm32"))]
fn latest_models() -> Option<&'static LatestModels> {
    // Disabled to avoid reqwest::blocking::Client runtime conflicts in async contexts
    // Always return None to use fallback models
    None
}

#[cfg(target_arch = "wasm32")]
fn latest_models() -> Option<&'static LatestModels> {
    None
}

#[cfg(not(target_arch = "wasm32"))]
fn fetch_model_catalog() -> Option<LatestModels> {
    let key = std::env::var("ANTHROPIC_ADMIN_API_KEY")
        .or_else(|_| std::env::var("ANTHROPIC_API_KEY"))
        .map_err(|err| warn!("Anthropic model refresh skipped: {err}"))
        .ok()?;

    let client = reqwest::blocking::Client::builder()
        .timeout(Duration::from_secs(5))
        .build()
        .map_err(|err| warn!("Anthropic model refresh skipped: failed to build client: {err}"))
        .ok()?;

    let response = client
        .get("https://api.anthropic.com/v1/models")
        .header("x-api-key", key)
        .header("anthropic-version", "2023-06-01")
        .send()
        .map_err(|err| warn!("Anthropic model refresh skipped: request failed: {err}"))
        .ok()?;

    if !response.status().is_success() {
        warn!(
            "Anthropic model refresh skipped: unexpected status {}",
            response.status()
        );
        return None;
    }

    let payload: ModelsResponse = response
        .json()
        .map_err(|err| warn!("Anthropic model refresh skipped: invalid response: {err}"))
        .ok()?;

    Some(pick_latest_models(&payload.data))
}

#[cfg(not(target_arch = "wasm32"))]
fn pick_latest_models(models: &[ModelInfo]) -> LatestModels {
    let mut best_opus: Option<(String, String)> = None;
    let mut best_sonnet: Option<(String, String)> = None;
    let mut best_haiku: Option<(String, String)> = None;

    for model in models {
        if !is_released(model) {
            continue;
        }
        let sort_key = model
            .created_at
            .as_ref()
            .cloned()
            .unwrap_or_else(|| model.id.clone());

        if model.id.contains("opus") {
            update_best(&mut best_opus, &model.id, &sort_key);
        }
        if model.id.contains("sonnet") {
            update_best(&mut best_sonnet, &model.id, &sort_key);
        }
        if model.id.contains("haiku") {
            update_best(&mut best_haiku, &model.id, &sort_key);
        }
    }

    LatestModels {
        opus: best_opus.map(|(id, _)| id),
        sonnet: best_sonnet.map(|(id, _)| id),
        haiku: best_haiku.map(|(id, _)| id),
    }
}

#[cfg(not(target_arch = "wasm32"))]
fn update_best(best: &mut Option<(String, String)>, candidate_id: &str, sort_key: &str) {
    match best {
        Some((_, existing_key)) if existing_key.as_str() >= sort_key => {}
        _ => {
            *best = Some((candidate_id.to_string(), sort_key.to_string()));
        }
    }
}

#[cfg(not(target_arch = "wasm32"))]
fn is_released(model: &ModelInfo) -> bool {
    match model.status.as_deref() {
        Some(status) => matches!(
            status.to_ascii_lowercase().as_str(),
            "released" | "available"
        ),
        None => true,
    }
}

#[cfg(target_arch = "wasm32")]
fn fetch_model_catalog() -> Option<LatestModels> {
    None
}

fn resolve_properties(
    provider: &ClientProvider,
    options: &internal_llm_client::UnresolvedClientProperty<()>,
    ctx: &RuntimeContext,
) -> Result<ResolvedClaudeCode> {
    let resolved = options.resolve(provider, &ctx.eval_ctx(false))?;
    let ResolvedClientProperty::ClaudeCode(properties) = resolved else {
        anyhow::bail!("Invalid client property. Expected claude-code properties");
    };
    Ok(properties)
}

pub struct ClaudeCodeClient {
    pub name: String,
    retry_policy: Option<String>,
    context: RenderContext_Client,
    features: ModelFeatures,
    properties: ResolvedClaudeCode,
    request_options: BamlMap<String, serde_json::Value>,
    default_models: (String, String, String), // (opus, sonnet, haiku)
}

impl ClaudeCodeClient {
    pub fn dynamic_new(client: &ClientProperty, ctx: &RuntimeContext) -> Result<Self> {
        let properties = resolve_properties(&client.provider, &client.unresolved_options()?, ctx)?;
        Self::from_parts(client.name.clone(), client.retry_policy.clone(), properties)
    }

    pub fn new(client: &ClientWalker, ctx: &RuntimeContext) -> Result<Self> {
        let properties = resolve_properties(&client.elem().provider, client.options(), ctx)?;
        let retry_policy = client
            .elem()
            .retry_policy_id
            .as_ref()
            .map(|s| s.to_string());
        Self::from_parts(client.name().to_string(), retry_policy, properties)
    }

    fn from_parts(
        name: String,
        retry_policy: Option<String>,
        properties: ResolvedClaudeCode,
    ) -> Result<Self> {
        let request_options = Self::build_request_options_map(&properties);
        let context = RenderContext_Client {
            name: name.clone(),
            provider: "claude-code".to_string(),
            default_role: properties.default_role(),
            allowed_roles: properties.allowed_roles(),
            remap_role: HashMap::new(),
            options: request_options.clone(),
        };

        let features = ModelFeatures {
            chat: true,
            completion: false,
            max_one_system_prompt: false,
            resolve_audio_urls: ResolveMediaUrls::Never,
            resolve_image_urls: ResolveMediaUrls::Never,
            resolve_pdf_urls: ResolveMediaUrls::Never,
            resolve_video_urls: ResolveMediaUrls::Never,
            allowed_metadata: properties.allowed_metadata.clone(),
        };

        // Use Anthropic aliases instead of hardcoded models
        let default_models = (
            "opus".to_string(),   // Anthropic alias for latest Opus
            "sonnet".to_string(), // Anthropic alias for latest Sonnet
            "haiku".to_string(),  // Anthropic alias for latest Haiku
        );

        Ok(Self {
            name,
            retry_policy,
            context,
            features,
            properties,
            request_options,
            default_models,
        })
    }

    fn build_request_options_map(
        properties: &ResolvedClaudeCode,
    ) -> BamlMap<String, serde_json::Value> {
        let mut map = BamlMap::new();
        map.insert("model".to_string(), json!(properties.model));
        if let Some(plan_model) = &properties.plan_model {
            map.insert("plan_model".to_string(), json!(plan_model));
        }
        if let Some(execution_model) = &properties.execution_model {
            map.insert("execution_model".to_string(), json!(execution_model));
        }
        if let Some(haiku_model) = &properties.haiku_model {
            map.insert("haiku_model".to_string(), json!(haiku_model));
        }
        if let Some(system_prompt) = &properties.system_prompt {
            map.insert("system_prompt".to_string(), json!(system_prompt));
        }
        if let Some(append_system_prompt) = &properties.append_system_prompt {
            map.insert(
                "append_system_prompt".to_string(),
                json!(append_system_prompt),
            );
        }
        if let Some(max_turns) = properties.max_turns {
            map.insert("max_turns".to_string(), json!(max_turns));
        }
        if let Some(max_thinking_tokens) = properties.max_thinking_tokens {
            map.insert(
                "max_thinking_tokens".to_string(),
                json!(max_thinking_tokens),
            );
        }
        if properties.continue_conversation {
            map.insert("continue_conversation".to_string(), json!(true));
        }
        if let Some(resume) = &properties.resume_session {
            map.insert("resume".to_string(), json!(resume));
        }
        if !properties.allowed_tools.is_empty() {
            map.insert("allowed_tools".to_string(), json!(properties.allowed_tools));
        }
        if !properties.disallowed_tools.is_empty() {
            map.insert(
                "disallowed_tools".to_string(),
                json!(properties.disallowed_tools),
            );
        }
        if let Some(permission_mode) = &properties.permission_mode {
            map.insert("permission_mode".to_string(), json!(permission_mode));
        }
        if let Some(permission_prompt_tool_name) = &properties.permission_prompt_tool_name {
            map.insert(
                "permission_prompt_tool_name".to_string(),
                json!(permission_prompt_tool_name),
            );
        }
        if let Some(cwd) = &properties.cwd {
            map.insert("cwd".to_string(), json!(cwd));
        }
        if !properties.add_dirs.is_empty() {
            map.insert("add_dirs".to_string(), json!(properties.add_dirs));
        }
        if let Some(settings) = &properties.settings {
            map.insert("settings".to_string(), json!(settings));
        }
        if let Some(output_format) = &properties.output_format {
            map.insert("output_format".to_string(), json!(output_format));
        }
        if let Some(api_key) = &properties.api_key {
            map.insert("api_key".to_string(), json!(api_key));
        }
        if let Some(timeout_ms) = properties.timeout_ms {
            map.insert("timeout_ms".to_string(), json!(timeout_ms));
        }
        if let Some(mcp_servers) = &properties.mcp_servers {
            map.insert("mcp_servers".to_string(), mcp_servers.clone());
        }
        if !properties.extra_args.is_empty() {
            map.insert("extra_args".to_string(), json!(properties.extra_args));
        }
        map
    }

    fn stringify_messages(&self, prompt: &[RenderedChatMessage]) -> String {
        prompt
            .iter()
            .map(|message| {
                let content = message
                    .parts
                    .iter()
                    .map(|part| self.stringify_part(part))
                    .collect::<Vec<_>>()
                    .join("\n");
                format!("{}: {}", message.role, content)
            })
            .collect::<Vec<_>>()
            .join("\n\n")
    }

    fn stringify_part(&self, part: &ChatMessagePart) -> String {
        match part {
            ChatMessagePart::Text(text) => text.to_string(),
            ChatMessagePart::Media(media) => format!("[media:{}]", media.media_type),
            ChatMessagePart::WithMeta(inner, meta) => {
                let value = self.stringify_part(inner);
                if meta.is_empty() {
                    value
                } else {
                    format!("{} {{meta:{:?}}}", value, meta)
                }
            }
        }
    }

    fn parts_to_message(
        &self,
        parts: &[ChatMessagePart],
    ) -> Result<Vec<serde_json::Map<String, serde_json::Value>>> {
        let mut message_parts = Vec::new();

        for part in parts {
            let mut content = serde_json::Map::new();
            match part {
                ChatMessagePart::Text(text) => {
                    content.insert("type".into(), json!("text"));
                    content.insert("text".into(), json!(text));
                }
                ChatMessagePart::Media(media) => {
                    content.insert("type".into(), json!("media"));
                    content.insert("media_type".into(), json!(media.media_type.to_string()));
                }
                ChatMessagePart::WithMeta(inner, meta) => {
                    // Handle the inner part first
                    let mut inner_content = match &**inner {
                        ChatMessagePart::Text(text) => {
                            let mut inner_map = serde_json::Map::new();
                            inner_map.insert("type".into(), json!("text"));
                            inner_map.insert("text".into(), json!(text));
                            inner_map
                        }
                        ChatMessagePart::Media(media) => {
                            let mut inner_map = serde_json::Map::new();
                            inner_map.insert("type".into(), json!("media"));
                            inner_map
                                .insert("media_type".into(), json!(media.media_type.to_string()));
                            inner_map
                        }
                        ChatMessagePart::WithMeta(_, _) => {
                            // This shouldn't happen in practice, but handle it gracefully
                            let mut inner_map = serde_json::Map::new();
                            inner_map.insert("type".into(), json!("text"));
                            inner_map.insert("text".into(), json!("[nested meta]"));
                            inner_map
                        }
                    };

                    // Add metadata if present
                    if !meta.is_empty() {
                        inner_content.insert("meta".into(), json!(meta));
                    }

                    content = inner_content;
                }
            }
            message_parts.push(content);
        }

        Ok(message_parts)
    }

    async fn run_claude(&self, prompt: &str, stream: bool) -> Result<ClaudeRunResult> {
        let timeout_duration = Duration::from_millis(
            self.properties.timeout_ms.unwrap_or(300_000), // Default to 5 minutes (300,000 ms)
        );

        // Extract command details
        let binary = self
            .properties
            .claude_code_binary
            .clone()
            .unwrap_or_else(|| "claude".to_string());

        let mut args = vec!["-p".to_string(), prompt.to_string()];
        let output_format = if stream {
            "stream-json".to_string()
        } else {
            self.properties
                .output_format
                .clone()
                .unwrap_or_else(|| "json".to_string())
        };
        args.push("--output-format".to_string());
        args.push(output_format);
        args.push("--model".to_string());
        args.push(self.properties.model.clone());

        if let Some(system_prompt) = &self.properties.system_prompt {
            args.push("--system-prompt".to_string());
            args.push(system_prompt.clone());
        }
        if let Some(append_system_prompt) = &self.properties.append_system_prompt {
            args.push("--append-system-prompt".to_string());
            args.push(append_system_prompt.clone());
        }
        if let Some(max_turns) = self.properties.max_turns {
            args.push("--max-turns".to_string());
            args.push(max_turns.to_string());
        }
        if let Some(max_thinking_tokens) = self.properties.max_thinking_tokens {
            args.push("--max-thinking-tokens".to_string());
            args.push(max_thinking_tokens.to_string());
        }
        if self.properties.continue_conversation {
            args.push("--continue".to_string());
        }
        if let Some(resume) = &self.properties.resume_session {
            args.push("--resume".to_string());
            args.push(resume.clone());
        }
        if !self.properties.allowed_tools.is_empty() {
            args.push("--allowedTools".to_string());
            args.push(self.properties.allowed_tools.join(","));
        }
        if !self.properties.disallowed_tools.is_empty() {
            args.push("--disallowedTools".to_string());
            args.push(self.properties.disallowed_tools.join(","));
        }
        if let Some(permission_mode) = &self.properties.permission_mode {
            args.push("--permission-mode".to_string());
            args.push(permission_mode.clone());
        }
        if let Some(permission_prompt_tool_name) = &self.properties.permission_prompt_tool_name {
            args.push("--permission-prompt-tool".to_string());
            args.push(permission_prompt_tool_name.clone());
        }
        if let Some(settings) = &self.properties.settings {
            args.push("--settings".to_string());
            args.push(settings.clone());
        }
        for dir in &self.properties.add_dirs {
            args.push("--add-dir".to_string());
            args.push(dir.clone());
        }

        // SDK-Specific Features
        if !self.properties.subagents.is_empty() {
            args.push("--subagents".to_string());
            args.push(self.properties.subagents.join(","));
        }
        if !self.properties.auto_detect_subagents {
            args.push("--no-auto-detect-subagents".to_string());
        }
        if let Some(hooks) = &self.properties.hooks {
            args.push("--hooks".to_string());
            args.push(hooks.clone());
        }
        // Note: Slash commands are not CLI arguments - they are used within prompts
        // The slash_commands configuration is kept for future SDK integration
        if !self.properties.memory_files.is_empty() {
            args.push("--memory-files".to_string());
            args.push(self.properties.memory_files.join(","));
        }
        if !self.properties.auto_load_memory {
            args.push("--no-auto-load-memory".to_string());
        }
        // Advanced Streaming
        if self.properties.realtime_streaming {
            args.push("--realtime-streaming".to_string());
        }
        if self.properties.enhanced_metadata {
            args.push("--enhanced-metadata".to_string());
        }
        if self.properties.stream_metadata {
            args.push("--stream-metadata".to_string());
        }
        // Advanced Authentication
        if let Some(auth_token) = &self.properties.auth_token {
            args.push("--auth-token".to_string());
            args.push(auth_token.clone());
        }
        if let Some(custom_headers) = &self.properties.custom_headers {
            args.push("--custom-headers".to_string());
            args.push(custom_headers.clone());
        }
        if let Some(custom_auth) = &self.properties.custom_auth {
            args.push("--custom-auth".to_string());
            args.push(custom_auth.clone());
        }

        let cwd = self.properties.cwd.clone();

        // Add environment variables
        let mut env_vars = std::collections::HashMap::new();

        // Handle API key with proper fallback to environment
        let api_key = if let Some(key) = &self.properties.api_key {
            key.clone()
        } else {
            // Try to get API key from environment as fallback
            std::env::var("ANTHROPIC_API_KEY").unwrap_or_else(|_| "".to_string())
        };

        env_vars.insert("ANTHROPIC_API_KEY".to_string(), api_key);

        // Use pre-fetched model environment variables to avoid async context issues
        let (default_opus, default_sonnet, default_haiku) = (
            &self.default_models.0,
            &self.default_models.1,
            &self.default_models.2,
        );

        // Only set environment variables for opusplan - let other aliases be handled by CLI
        if self.properties.model == "opusplan" {
            // Plan model (planning phase)
            if let Some(plan_model) = &self.properties.plan_model {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_OPUS_MODEL".to_string(),
                    plan_model.clone(),
                );
            } else {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_OPUS_MODEL".to_string(),
                    default_opus.clone(),
                );
            }

            // Execution model (implementation phase)
            if let Some(exec_model) = &self.properties.execution_model {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_SONNET_MODEL".to_string(),
                    exec_model.clone(),
                );
            } else {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_SONNET_MODEL".to_string(),
                    default_sonnet.clone(),
                );
            }

            // Haiku model (background tasks)
            if let Some(haiku_model) = &self.properties.haiku_model {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_HAIKU_MODEL".to_string(),
                    haiku_model.clone(),
                );
            } else {
                env_vars.insert(
                    "ANTHROPIC_DEFAULT_HAIKU_MODEL".to_string(),
                    default_haiku.clone(),
                );
            }
        }
        // For other aliases (sonnet, opus, haiku, default, sonnet[1m]), let Claude Code CLI handle the mapping

        // Handle MCP servers
        let mcp_config = if let Some(mcp_servers) = &self.properties.mcp_servers {
            let mut file = NamedTempFile::new()?;
            serde_json::to_writer_pretty(file.as_file_mut(), mcp_servers)?;
            Some((file.path().to_path_buf(), file))
        } else {
            None
        };

        if let Some((mcp_path, _)) = &mcp_config {
            args.push("--mcp-config".to_string());
            args.push(mcp_path.to_string_lossy().to_string());
        }

        for (key, value) in &self.properties.extra_args {
            let flag = if key.starts_with('-') {
                key.clone()
            } else {
                format!("--{}", key)
            };
            args.push(flag);
            if let Some(value) = value {
                args.push(value.clone());
            }
        }

        // Use spawn_blocking to run CLI in a blocking context without creating new runtimes
        let output = tokio::time::timeout(
            timeout_duration,
            tokio::task::spawn_blocking(move || {
                let mut cmd = StdCommand::new(binary);
                cmd.args(&args);

                if let Some(cwd) = cwd {
                    cmd.current_dir(cwd);
                }

                for (key, value) in env_vars {
                    cmd.env(key, value);
                }

                cmd.stderr(std::process::Stdio::piped());
                cmd.stdout(std::process::Stdio::piped());

                cmd.output()
            }),
        )
        .await
        .with_context(|| "Claude Code CLI timed out after 5 minutes")?
        .with_context(|| "Failed to spawn blocking task")?
        .with_context(|| "Failed to execute Claude Code CLI")?;

        drop(mcp_config);

        if !output.status.success() {
            let stderr = String::from_utf8_lossy(&output.stderr).to_string();
            let stdout = String::from_utf8_lossy(&output.stdout).to_string();

            // Provide more helpful error messages
            if stderr.contains("not found") || stderr.contains("command not found") {
                anyhow::bail!("Claude Code CLI not found. Please install it: npm install -g @anthropic-ai/claude-code");
            } else if stderr.contains("authentication") || stderr.contains("API key") {
                anyhow::bail!("Claude Code authentication failed. Check your API key or CloudPlan setup: {stderr}");
            } else if stderr.contains("timeout") {
                anyhow::bail!("Claude Code CLI timed out: {stderr}");
            } else {
                anyhow::bail!(
                    "Claude Code CLI returned error (exit code {}): {stderr}\nOutput: {stdout}",
                    output.status.code().unwrap_or(-1)
                );
            }
        }

        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        Ok(ClaudeRunResult { stdout })
    }

    fn parse_response(&self, raw: &str) -> ParsedClaudeResponse {
        let mut session_id = None;
        let mut final_text = String::new();
        let mut chunks: Vec<String> = Vec::new();
        let mut finish_reason = None;
        let mut prompt_tokens = None;
        let mut output_tokens = None;
        let mut total_tokens = None;
        let mut slash_commands = Vec::new();

        let mut saw_json = false;
        for line in raw.lines() {
            let trimmed = line.trim();
            if trimmed.is_empty() {
                continue;
            }

            match serde_json::from_str::<serde_json::Value>(trimmed) {
                Ok(value) => {
                    saw_json = true;
                    match value.get("type").and_then(|v| v.as_str()) {
                        Some("system") => {
                            if value
                                .get("subtype")
                                .and_then(|v| v.as_str())
                                .map(|s| s == "init")
                                .unwrap_or(false)
                            {
                                if let Some(id) = value.get("session_id").and_then(|v| v.as_str()) {
                                    session_id = Some(id.to_string());
                                }
                                // Extract available slash commands from system init message
                                if let Some(commands) =
                                    value.get("slash_commands").and_then(|v| v.as_array())
                                {
                                    slash_commands = commands
                                        .iter()
                                        .filter_map(|cmd| cmd.as_str())
                                        .map(|s| s.to_string())
                                        .collect();
                                }
                            }
                        }
                        Some("assistant") => {
                            if let Some(content) = value.get("content").and_then(|v| v.as_array()) {
                                for block in content {
                                    if let Some(text) = block.get("text").and_then(|t| t.as_str()) {
                                        chunks.push(text.to_string());
                                    }
                                }
                            }
                            if let Some(reason) = value
                                .get("stop_reason")
                                .or_else(|| value.get("finish_reason"))
                                .and_then(|v| v.as_str())
                            {
                                finish_reason = Some(reason.to_string());
                            }
                        }
                        Some("result") => {
                            if let Some(result) = value.get("result").and_then(|v| v.as_str()) {
                                final_text = result.to_string();
                            }
                            if let Some(usage) = value.get("usage") {
                                prompt_tokens = usage.get("input_tokens").and_then(|v| v.as_u64());
                                output_tokens = usage.get("output_tokens").and_then(|v| v.as_u64());
                                total_tokens = usage.get("total_tokens").and_then(|v| v.as_u64());
                            }
                            if finish_reason.is_none() {
                                if let Some(reason) =
                                    value.get("finish_reason").and_then(|v| v.as_str())
                                {
                                    finish_reason = Some(reason.to_string());
                                }
                            }
                        }
                        _ => {}
                    }
                }
                Err(_) => {
                    chunks.push(trimmed.to_string());
                }
            }
        }

        if final_text.is_empty() {
            final_text = chunks.join("").trim().to_string();
        }

        if final_text.is_empty() && !saw_json {
            final_text = raw.trim().to_string();
        }

        ParsedClaudeResponse {
            content: final_text,
            session_id,
            finish_reason,
            prompt_tokens,
            output_tokens,
            total_tokens,
            slash_commands,
        }
    }
}

impl WithRetryPolicy for ClaudeCodeClient {
    fn retry_policy_name(&self) -> Option<&str> {
        self.retry_policy.as_deref()
    }
}

impl WithClientProperties for ClaudeCodeClient {
    fn allowed_metadata(&self) -> &AllowedRoleMetadata {
        &self.properties.allowed_metadata
    }

    fn supports_streaming(&self) -> bool {
        self.properties
            .supported_request_modes
            .stream
            .unwrap_or(false)
    }

    fn finish_reason_filter(&self) -> &internal_llm_client::FinishReasonFilter {
        &self.properties.finish_reason_filter
    }

    fn default_role(&self) -> String {
        self.properties.default_role()
    }

    fn allowed_roles(&self) -> Vec<String> {
        self.properties.allowed_roles()
    }
}

impl WithClient for ClaudeCodeClient {
    fn context(&self) -> &RenderContext_Client {
        &self.context
    }

    fn model_features(&self) -> &ModelFeatures {
        &self.features
    }
}

impl WithNoCompletion for ClaudeCodeClient {}

impl WithChat for ClaudeCodeClient {
    async fn chat(&self, _ctx: &impl HttpContext, prompt: &[RenderedChatMessage]) -> LLMResponse {
        let start_time = SystemTime::now();
        let instant_start = Instant::now();
        let rendered_prompt = RenderedPrompt::Chat(prompt.to_vec());
        let prompt_text = self.stringify_messages(prompt);

        match self.run_claude(&prompt_text, false).await {
            Ok(result) => {
                let parsed = self.parse_response(&result.stdout);
                let response = LLMCompleteResponse {
                    client: self.name.clone(),
                    model: self.properties.model.clone(),
                    prompt: rendered_prompt,
                    request_options: self.request_options.clone(),
                    content: parsed.content,
                    start_time,
                    latency: instant_start.elapsed(),
                    metadata: LLMCompleteResponseMetadata {
                        baml_is_complete: true,
                        finish_reason: parsed.finish_reason.or_else(|| Some("stop".to_string())),
                        prompt_tokens: parsed.prompt_tokens,
                        output_tokens: parsed.output_tokens,
                        total_tokens: parsed.total_tokens,
                        cached_input_tokens: None,
                    },
                };
                LLMResponse::Success(response)
            }
            Err(err) => LLMResponse::InternalFailure(format!("Claude Code client error: {err}")),
        }
    }
}

impl WithStreamChat for ClaudeCodeClient {
    async fn stream_chat(
        &self,
        ctx: &impl HttpContext,
        prompt: &[RenderedChatMessage],
    ) -> crate::internal::llm_client::traits::StreamResponse {
        if !self.supports_streaming() {
            let response = self.chat(ctx, prompt).await;
            return Ok(Box::pin(futures::stream::once(async move { response })));
        }

        let prompt_text = self.stringify_messages(prompt);
        let rendered_prompt = RenderedPrompt::Chat(prompt.to_vec());
        let start_time = SystemTime::now();
        let instant_start = Instant::now();
        let properties = self.properties.clone();
        let name = self.name.clone();

        match self.run_claude(&prompt_text, true).await {
            Ok(result) => {
                let parsed = self.parse_response(&result.stdout);
                let response = LLMResponse::Success(LLMCompleteResponse {
                    client: name,
                    model: properties.model.clone(),
                    prompt: rendered_prompt,
                    request_options: self.request_options.clone(),
                    content: parsed.content,
                    start_time,
                    latency: instant_start.elapsed(),
                    metadata: LLMCompleteResponseMetadata {
                        baml_is_complete: true,
                        finish_reason: parsed.finish_reason.or_else(|| Some("stop".to_string())),
                        prompt_tokens: parsed.prompt_tokens,
                        output_tokens: parsed.output_tokens,
                        total_tokens: parsed.total_tokens,
                        cached_input_tokens: None,
                    },
                });

                Ok(Box::pin(futures::stream::once(async move { response })))
            }
            Err(err) => Err(LLMResponse::InternalFailure(format!(
                "Claude Code client error: {err}"
            ))),
        }
    }
}

impl ToProviderMessage for ClaudeCodeClient {
    fn to_chat_message(
        &self,
        mut content: serde_json::Map<String, serde_json::Value>,
        text: &str,
    ) -> Result<serde_json::Map<String, serde_json::Value>> {
        content.insert("type".into(), json!("text"));
        content.insert("text".into(), json!(text));
        Ok(content)
    }

    fn to_media_message(
        &self,
        mut content: serde_json::Map<String, serde_json::Value>,
        media: &baml_types::BamlMedia,
    ) -> Result<serde_json::Map<String, serde_json::Value>> {
        content.insert("type".into(), json!("media"));
        content.insert("media_type".into(), json!(media.media_type.to_string()));
        Ok(content)
    }

    fn role_to_message(
        &self,
        content: &RenderedChatMessage,
    ) -> Result<serde_json::Map<String, serde_json::Value>> {
        let mut message = serde_json::Map::new();
        message.insert("role".into(), json!(content.role.clone()));
        let parts = self.parts_to_message(&content.parts)?;
        message.insert(
            "content".into(),
            serde_json::Value::Array(
                parts
                    .into_iter()
                    .map(serde_json::Value::Object)
                    .collect::<Vec<_>>(),
            ),
        );
        Ok(message)
    }
}

impl ToProviderMessageExt for ClaudeCodeClient {
    fn chat_to_message(
        &self,
        chat: &[RenderedChatMessage],
    ) -> Result<serde_json::Map<String, serde_json::Value>> {
        let messages = chat
            .iter()
            .map(|message| self.role_to_message(message))
            .collect::<Result<Vec<_>>>()?;

        let mut map = serde_json::Map::new();
        map.insert(
            "messages".into(),
            serde_json::Value::Array(
                messages
                    .into_iter()
                    .map(serde_json::Value::Object)
                    .collect::<Vec<_>>(),
            ),
        );
        Ok(map)
    }
}

impl CompletionToProviderBody for ClaudeCodeClient {
    fn completion_to_provider_body(
        &self,
        prompt: &str,
    ) -> serde_json::Map<String, serde_json::Value> {
        let mut map = serde_json::Map::new();
        map.insert("prompt".into(), json!(prompt));
        map
    }
}

impl RequestBuilder for ClaudeCodeClient {
    fn http_client(&self) -> &reqwest::Client {
        // Claude Code doesn't use HTTP - return a dummy client
        static DUMMY_CLIENT: once_cell::sync::Lazy<reqwest::Client> =
            once_cell::sync::Lazy::new(|| reqwest::Client::new());
        &DUMMY_CLIENT
    }

    fn request_options(&self) -> &BamlMap<String, serde_json::Value> {
        &self.request_options
    }

    async fn build_request(
        &self,
        _prompt: either::Either<&String, &[RenderedChatMessage]>,
        _allow_proxy: bool,
        _stream: bool,
        _expose_secrets: bool,
    ) -> Result<reqwest::RequestBuilder> {
        Err(anyhow!(
            "Claude Code provider executes the claude CLI directly and does not support HTTP requests"
        ))
    }
}

struct ClaudeRunResult {
    stdout: String,
}

struct ParsedClaudeResponse {
    content: String,
    session_id: Option<String>,
    finish_reason: Option<String>,
    prompt_tokens: Option<u64>,
    output_tokens: Option<u64>,
    total_tokens: Option<u64>,
    slash_commands: Vec<String>,
}

#[cfg(test)]
mod tests {
    use indexmap::IndexMap;

    use super::*;

    fn sample_properties() -> ResolvedClaudeCode {
        ResolvedClaudeCode {
            model: "sonnet".to_string(),
            plan_model: None,
            execution_model: None,
            haiku_model: Some("haiku".to_string()),
            system_prompt: None,
            append_system_prompt: None,
            max_turns: None,
            max_thinking_tokens: None,
            continue_conversation: false,
            resume_session: None,
            allowed_tools: Vec::new(),
            disallowed_tools: Vec::new(),
            permission_mode: None,
            permission_prompt_tool_name: None,
            cwd: None,
            add_dirs: Vec::new(),
            settings: None,
            claude_code_binary: None,
            node_binary: None,
            output_format: None,
            api_key: None,
            // SDK-Specific Features
            subagents: Vec::new(),
            auto_detect_subagents: true,
            hooks: None,
            slash_commands: Vec::new(),
            memory_files: Vec::new(),
            auto_load_memory: true,
            // Advanced Streaming
            realtime_streaming: false,
            enhanced_metadata: false,
            stream_metadata: false,
            // Advanced Authentication
            auth_token: None,
            custom_headers: None,
            custom_auth: None,
            // Timeout Configuration
            timeout_ms: None,
            extra_args: IndexMap::new(),
            mcp_servers: None,
            allowed_metadata: AllowedRoleMetadata::All,
            supported_request_modes: internal_llm_client::SupportedRequestModes {
                stream: Some(false),
            },
            finish_reason_filter: internal_llm_client::FinishReasonFilter::All,
        }
    }

    #[test]
    fn parse_response_extracts_usage() {
        let client =
            ClaudeCodeClient::from_parts("test".into(), None, sample_properties()).unwrap();
        let raw = r#"{"type":"system","subtype":"init","session_id":"abc"}
{"type":"assistant","content":[{"type":"text","text":"Hello"}]}
{"type":"result","result":"Hello world","usage":{"input_tokens":10,"output_tokens":20,"total_tokens":30},"finish_reason":"stop"}
"#;

        let parsed = client.parse_response(raw);
        assert_eq!(parsed.content, "Hello world");
        assert_eq!(parsed.session_id.as_deref(), Some("abc"));
        assert_eq!(parsed.prompt_tokens, Some(10));
        assert_eq!(parsed.output_tokens, Some(20));
        assert_eq!(parsed.total_tokens, Some(30));
        assert_eq!(parsed.finish_reason.as_deref(), Some("stop"));
        assert_eq!(parsed.slash_commands, Vec::<String>::new());
    }

    #[test]
    fn parse_response_extracts_slash_commands() {
        let client =
            ClaudeCodeClient::from_parts("test".into(), None, sample_properties()).unwrap();
        let raw = r#"{"type":"system","subtype":"init","session_id":"abc","slash_commands":["/compact","/clear","/help"]}
{"type":"assistant","content":[{"type":"text","text":"Hello"}]}
{"type":"result","result":"Hello world","usage":{"input_tokens":10,"output_tokens":20,"total_tokens":30},"finish_reason":"stop"}
"#;

        let parsed = client.parse_response(raw);
        assert_eq!(parsed.content, "Hello world");
        assert_eq!(parsed.session_id.as_deref(), Some("abc"));
        assert_eq!(parsed.slash_commands, vec!["/compact", "/clear", "/help"]);
    }

    #[cfg(not(target_arch = "wasm32"))]
    #[test]
    fn pick_latest_models_prefers_newest_ids() {
        let models = vec![
            ModelInfo {
                id: "claude-opus-4-1-20250701".to_string(),
                created_at: Some("2025-07-01T00:00:00Z".to_string()),
                status: Some("released".to_string()),
                display_name: None,
            },
            ModelInfo {
                id: "claude-opus-4-1-20250805".to_string(),
                created_at: Some("2025-08-05T00:00:00Z".to_string()),
                status: Some("released".to_string()),
                display_name: None,
            },
            ModelInfo {
                id: "claude-sonnet-4-20250514".to_string(),
                created_at: Some("2025-05-14T00:00:00Z".to_string()),
                status: Some("released".to_string()),
                display_name: None,
            },
            ModelInfo {
                id: "claude-sonnet-4-20250401".to_string(),
                created_at: Some("2025-04-01T00:00:00Z".to_string()),
                status: Some("deprecated".to_string()),
                display_name: None,
            },
            ModelInfo {
                id: "claude-3-5-haiku-20241022".to_string(),
                created_at: Some("2024-10-22T00:00:00Z".to_string()),
                status: Some("released".to_string()),
                display_name: None,
            },
        ];

        let latest = pick_latest_models(&models);
        assert_eq!(latest.opus.as_deref(), Some("claude-opus-4-1-20250805"));
        assert_eq!(latest.sonnet.as_deref(), Some("claude-sonnet-4-20250514"));
        assert_eq!(latest.haiku.as_deref(), Some("claude-3-5-haiku-20241022"));
    }
}
