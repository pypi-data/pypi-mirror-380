use std::collections::HashSet;

use anyhow::{anyhow, Result};
use baml_derive::BamlHash;
use baml_types::{EvaluationContext, StringOr, UnresolvedValue};
use indexmap::IndexMap;

use super::helpers::{Error, PropertyHandler};
use crate::{
    AllowedRoleMetadata, FinishReasonFilter, SupportedRequestModes, UnresolvedAllowedRoleMetadata,
    UnresolvedFinishReasonFilter,
};

#[derive(Debug, Clone, BamlHash)]
pub struct UnresolvedClaudeCode<Meta> {
    model: Option<StringOr>,
    plan_model: Option<StringOr>,
    execution_model: Option<StringOr>,
    haiku_model: Option<StringOr>,
    system_prompt: Option<StringOr>,
    append_system_prompt: Option<StringOr>,
    max_turns: Option<i32>,
    max_thinking_tokens: Option<i32>,
    continue_conversation: Option<bool>,
    resume_session: Option<StringOr>,
    allowed_tools: Vec<StringOr>,
    disallowed_tools: Vec<StringOr>,
    permission_mode: Option<StringOr>,
    permission_prompt_tool_name: Option<StringOr>,
    cwd: Option<StringOr>,
    add_dirs: Vec<StringOr>,
    settings: Option<StringOr>,
    claude_code_binary: Option<StringOr>,
    node_binary: Option<StringOr>,
    output_format: Option<StringOr>,
    api_key: Option<StringOr>,
    // SDK-Specific Features
    subagents: Vec<StringOr>,
    auto_detect_subagents: Option<bool>,
    hooks: Option<StringOr>,
    slash_commands: Vec<StringOr>,
    memory_files: Vec<StringOr>,
    auto_load_memory: Option<bool>,
    // Advanced Streaming
    realtime_streaming: Option<bool>,
    enhanced_metadata: Option<bool>,
    stream_metadata: Option<bool>,
    // Advanced Authentication
    auth_token: Option<StringOr>,
    custom_headers: Option<StringOr>,
    custom_auth: Option<StringOr>,
    // Timeout Configuration
    timeout_ms: Option<i64>,
    #[baml_safe_hash]
    extra_args: IndexMap<String, (Meta, UnresolvedValue<Meta>)>,
    #[baml_safe_hash]
    mcp_servers: Option<(Meta, UnresolvedValue<Meta>)>,
    allowed_metadata: UnresolvedAllowedRoleMetadata,
    supported_request_modes: SupportedRequestModes,
    finish_reason_filter: UnresolvedFinishReasonFilter,
}

impl<Meta: Clone> UnresolvedClaudeCode<Meta> {
    pub fn without_meta(&self) -> UnresolvedClaudeCode<()> {
        UnresolvedClaudeCode {
            model: self.model.clone(),
            plan_model: self.plan_model.clone(),
            execution_model: self.execution_model.clone(),
            haiku_model: self.haiku_model.clone(),
            system_prompt: self.system_prompt.clone(),
            append_system_prompt: self.append_system_prompt.clone(),
            max_turns: self.max_turns,
            max_thinking_tokens: self.max_thinking_tokens,
            continue_conversation: self.continue_conversation,
            resume_session: self.resume_session.clone(),
            allowed_tools: self.allowed_tools.clone(),
            disallowed_tools: self.disallowed_tools.clone(),
            permission_mode: self.permission_mode.clone(),
            permission_prompt_tool_name: self.permission_prompt_tool_name.clone(),
            cwd: self.cwd.clone(),
            add_dirs: self.add_dirs.clone(),
            settings: self.settings.clone(),
            claude_code_binary: self.claude_code_binary.clone(),
            node_binary: self.node_binary.clone(),
            output_format: self.output_format.clone(),
            api_key: self.api_key.clone(),
            // SDK-Specific Features
            subagents: self.subagents.clone(),
            auto_detect_subagents: self.auto_detect_subagents,
            hooks: self.hooks.clone(),
            slash_commands: self.slash_commands.clone(),
            memory_files: self.memory_files.clone(),
            auto_load_memory: self.auto_load_memory,
            // Advanced Streaming
            realtime_streaming: self.realtime_streaming,
            enhanced_metadata: self.enhanced_metadata,
            stream_metadata: self.stream_metadata,
            // Advanced Authentication
            auth_token: self.auth_token.clone(),
            custom_headers: self.custom_headers.clone(),
            custom_auth: self.custom_auth.clone(),
            // Timeout Configuration
            timeout_ms: self.timeout_ms,
            extra_args: self
                .extra_args
                .iter()
                .map(|(k, (_, v))| (k.clone(), ((), v.without_meta())))
                .collect(),
            mcp_servers: self
                .mcp_servers
                .as_ref()
                .map(|(_, v)| ((), v.without_meta())),
            allowed_metadata: self.allowed_metadata.clone(),
            supported_request_modes: self.supported_request_modes.clone(),
            finish_reason_filter: self.finish_reason_filter.clone(),
        }
    }

    pub fn required_env_vars(&self) -> HashSet<String> {
        let mut vars = HashSet::new();

        if let Some(model) = &self.model {
            vars.extend(model.required_env_vars());
        }
        if let Some(plan_model) = &self.plan_model {
            vars.extend(plan_model.required_env_vars());
        }
        if let Some(execution_model) = &self.execution_model {
            vars.extend(execution_model.required_env_vars());
        }
        if let Some(haiku_model) = &self.haiku_model {
            vars.extend(haiku_model.required_env_vars());
        }
        if let Some(system_prompt) = &self.system_prompt {
            vars.extend(system_prompt.required_env_vars());
        }
        if let Some(append_system_prompt) = &self.append_system_prompt {
            vars.extend(append_system_prompt.required_env_vars());
        }
        if let Some(resume) = &self.resume_session {
            vars.extend(resume.required_env_vars());
        }
        if let Some(permission_mode) = &self.permission_mode {
            vars.extend(permission_mode.required_env_vars());
        }
        if let Some(permission_prompt_tool_name) = &self.permission_prompt_tool_name {
            vars.extend(permission_prompt_tool_name.required_env_vars());
        }
        if let Some(cwd) = &self.cwd {
            vars.extend(cwd.required_env_vars());
        }
        if let Some(settings) = &self.settings {
            vars.extend(settings.required_env_vars());
        }
        if let Some(binary) = &self.claude_code_binary {
            vars.extend(binary.required_env_vars());
        }
        if let Some(node_binary) = &self.node_binary {
            vars.extend(node_binary.required_env_vars());
        }
        if let Some(output_format) = &self.output_format {
            vars.extend(output_format.required_env_vars());
        }
        if let Some(api_key) = &self.api_key {
            vars.extend(api_key.required_env_vars());
        }
        // SDK-Specific Features
        for value in &self.subagents {
            vars.extend(value.required_env_vars());
        }
        if let Some(hooks) = &self.hooks {
            vars.extend(hooks.required_env_vars());
        }
        for value in &self.slash_commands {
            vars.extend(value.required_env_vars());
        }
        for value in &self.memory_files {
            vars.extend(value.required_env_vars());
        }
        // Advanced Authentication
        if let Some(auth_token) = &self.auth_token {
            vars.extend(auth_token.required_env_vars());
        }
        if let Some(custom_headers) = &self.custom_headers {
            vars.extend(custom_headers.required_env_vars());
        }
        if let Some(custom_auth) = &self.custom_auth {
            vars.extend(custom_auth.required_env_vars());
        }

        for value in &self.allowed_tools {
            vars.extend(value.required_env_vars());
        }
        for value in &self.disallowed_tools {
            vars.extend(value.required_env_vars());
        }
        for value in &self.add_dirs {
            vars.extend(value.required_env_vars());
        }

        if let Some((_, value)) = &self.mcp_servers {
            vars.extend(value.required_env_vars());
        }

        for (_, (_, value)) in &self.extra_args {
            vars.extend(value.required_env_vars());
        }

        vars.extend(self.allowed_metadata.required_env_vars());
        vars.extend(self.supported_request_modes.required_env_vars());
        vars.extend(self.finish_reason_filter.required_env_vars());

        vars
    }

    pub fn resolve(&self, ctx: &EvaluationContext<'_>) -> Result<ResolvedClaudeCode> {
        let model = self.model.as_ref().map(|m| m.resolve(ctx)).transpose()?;
        let model = model.unwrap_or_else(|| "sonnet".to_string());

        let plan_model = self
            .plan_model
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;
        let execution_model = self
            .execution_model
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;
        let haiku_model = self
            .haiku_model
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;
        let system_prompt = self
            .system_prompt
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;
        let append_system_prompt = self
            .append_system_prompt
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;

        let resume_session = self
            .resume_session
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;

        let permission_mode = self
            .permission_mode
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;
        let permission_prompt_tool_name = self
            .permission_prompt_tool_name
            .as_ref()
            .map(|m| m.resolve(ctx))
            .transpose()?;

        let cwd = self.cwd.as_ref().map(|v| v.resolve(ctx)).transpose()?;
        let settings = self.settings.as_ref().map(|v| v.resolve(ctx)).transpose()?;
        let claude_code_binary = self
            .claude_code_binary
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;
        let node_binary = self
            .node_binary
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;
        let output_format = self
            .output_format
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;
        let api_key = self.api_key.as_ref().map(|v| v.resolve(ctx)).transpose()?;

        // SDK-Specific Features
        let subagents = self
            .subagents
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;
        let auto_detect_subagents = self.auto_detect_subagents.unwrap_or(true);
        let hooks = self.hooks.as_ref().map(|v| v.resolve(ctx)).transpose()?;
        let slash_commands = self
            .slash_commands
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;
        let memory_files = self
            .memory_files
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;
        let auto_load_memory = self.auto_load_memory.unwrap_or(true);
        // Advanced Streaming
        let realtime_streaming = self.realtime_streaming.unwrap_or(false);
        let enhanced_metadata = self.enhanced_metadata.unwrap_or(false);
        let stream_metadata = self.stream_metadata.unwrap_or(false);
        // Advanced Authentication
        let auth_token = self
            .auth_token
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;
        let custom_headers = self
            .custom_headers
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;
        let custom_auth = self
            .custom_auth
            .as_ref()
            .map(|v| v.resolve(ctx))
            .transpose()?;

        // Timeout Configuration
        let timeout_ms = self.timeout_ms.map(|v| v as u64);

        let allowed_tools = self
            .allowed_tools
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;
        let disallowed_tools = self
            .disallowed_tools
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;
        let add_dirs = self
            .add_dirs
            .iter()
            .map(|v| v.resolve(ctx))
            .collect::<Result<Vec<_>>>()?;

        let mcp_servers = match &self.mcp_servers {
            Some((_, value)) => Some(value.resolve_serde::<serde_json::Value>(ctx)?),
            None => None,
        };

        let extra_args = self
            .extra_args
            .iter()
            .map(|(key, (_, value))| {
                let resolved = value.resolve_serde::<serde_json::Value>(ctx)?;
                match resolved {
                    serde_json::Value::Null => Ok((key.clone(), None)),
                    serde_json::Value::String(s) => Ok((key.clone(), Some(s))),
                    serde_json::Value::Bool(true) => Ok((key.clone(), None)),
                    serde_json::Value::Bool(false) => Ok((key.clone(), Some("false".to_string()))),
                    other => Err(anyhow!(
                        "extra_args values must be strings, booleans, or null. Got: {other:?}"
                    )),
                }
            })
            .collect::<Result<IndexMap<_, _>>>()?;

        let allowed_metadata = self.allowed_metadata.resolve(ctx)?;
        let finish_reason_filter = self.finish_reason_filter.resolve(ctx)?;

        let max_turns = self
            .max_turns
            .and_then(|v| if v > 0 { Some(v as u32) } else { None });
        let max_thinking_tokens =
            self.max_thinking_tokens
                .and_then(|v| if v > 0 { Some(v as u32) } else { None });

        Ok(ResolvedClaudeCode {
            model,
            plan_model,
            execution_model,
            system_prompt,
            append_system_prompt,
            max_turns,
            max_thinking_tokens,
            continue_conversation: self.continue_conversation.unwrap_or(false),
            resume_session,
            allowed_tools,
            disallowed_tools,
            permission_mode,
            permission_prompt_tool_name,
            cwd,
            add_dirs,
            settings,
            claude_code_binary,
            node_binary,
            output_format,
            api_key,
            // SDK-Specific Features
            subagents,
            auto_detect_subagents,
            hooks,
            slash_commands,
            memory_files,
            auto_load_memory,
            // Advanced Streaming
            realtime_streaming,
            enhanced_metadata,
            stream_metadata,
            // Advanced Authentication
            auth_token,
            custom_headers,
            custom_auth,
            // Timeout Configuration
            timeout_ms,
            haiku_model,
            extra_args,
            mcp_servers,
            allowed_metadata,
            supported_request_modes: self.supported_request_modes.clone(),
            finish_reason_filter,
        })
    }

    pub fn create_from(mut properties: PropertyHandler<Meta>) -> Result<Self, Vec<Error<Meta>>> {
        let model = properties.ensure_string("model", false).map(|(_, v, _)| v);
        let plan_model = properties
            .ensure_string("plan_model", false)
            .map(|(_, v, _)| v);
        let execution_model = properties
            .ensure_string("execution_model", false)
            .map(|(_, v, _)| v);
        let haiku_model = properties
            .ensure_string("haiku_model", false)
            .map(|(_, v, _)| v);
        let system_prompt = properties
            .ensure_string("system_prompt", false)
            .map(|(_, v, _)| v);
        let append_system_prompt = properties
            .ensure_string("append_system_prompt", false)
            .map(|(_, v, _)| v);

        let max_turns = properties.ensure_int("max_turns", false).map(|(_, v, _)| v);
        let max_thinking_tokens = properties
            .ensure_int("max_thinking_tokens", false)
            .map(|(_, v, _)| v);
        let continue_conversation = properties
            .ensure_bool("continue_conversation", false)
            .map(|(_, v, _)| v);
        let resume_session = properties.ensure_string("resume", false).map(|(_, v, _)| v);

        let allowed_tools = properties
            .ensure_array("allowed_tools", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties.push_error(
                        "allowed_tools entries must be strings",
                        value.meta().clone(),
                    );
                    None
                }
            })
            .collect::<Vec<_>>();

        let disallowed_tools = properties
            .ensure_array("disallowed_tools", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties.push_error(
                        "disallowed_tools entries must be strings",
                        value.meta().clone(),
                    );
                    None
                }
            })
            .collect::<Vec<_>>();

        let permission_mode = properties
            .ensure_string("permission_mode", false)
            .map(|(_, v, _)| v);
        let permission_prompt_tool_name = properties
            .ensure_string("permission_prompt_tool_name", false)
            .map(|(_, v, _)| v);

        let cwd = properties.ensure_string("cwd", false).map(|(_, v, _)| v);
        let add_dirs = properties
            .ensure_array("add_dirs", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties.push_error("add_dirs entries must be strings", value.meta().clone());
                    None
                }
            })
            .collect::<Vec<_>>();
        let settings = properties
            .ensure_string("settings", false)
            .map(|(_, v, _)| v);
        let claude_code_binary = properties
            .ensure_string("claude_binary", false)
            .map(|(_, v, _)| v)
            .or_else(|| {
                properties
                    .ensure_string("claude_code_binary", false)
                    .map(|(_, v, _)| v)
            });
        let node_binary = properties
            .ensure_string("node_binary", false)
            .map(|(_, v, _)| v);
        let output_format = properties
            .ensure_string("output_format", false)
            .map(|(_, v, _)| v);
        let api_key = properties
            .ensure_string("api_key", false)
            .map(|(_, v, _)| v);

        // Timeout Configuration
        let timeout_ms = properties
            .ensure_int("timeout_ms", false)
            .map(|(_, v, _)| v as i64);

        let extra_args = properties
            .ensure_map("extra_args", false)
            .map(|(_, value, _)| value)
            .unwrap_or_default();

        let mcp_servers = properties.ensure_any("mcp_servers");

        let allowed_metadata = properties.ensure_allowed_metadata();
        let supported_request_modes = properties.ensure_supported_request_modes();
        let finish_reason_filter = properties.ensure_finish_reason_filter();

        // SDK-Specific Features
        let subagents = properties
            .ensure_array("subagents", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties
                        .push_error("subagents entries must be strings", value.meta().clone());
                    None
                }
            })
            .collect::<Vec<_>>();
        let auto_detect_subagents = properties
            .ensure_bool("auto_detect_subagents", false)
            .map(|(_, v, _)| v)
            .unwrap_or(true);
        let hooks = properties.ensure_string("hooks", false).map(|(_, v, _)| v);
        let slash_commands = properties
            .ensure_array("slash_commands", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties.push_error(
                        "slash_commands entries must be strings",
                        value.meta().clone(),
                    );
                    None
                }
            })
            .collect::<Vec<_>>();
        let memory_files = properties
            .ensure_array("memory_files", false)
            .map(|(_, values, _)| values)
            .unwrap_or_default()
            .into_iter()
            .filter_map(|value| match value.as_str() {
                Some(s) => Some(s.clone()),
                None => {
                    properties
                        .push_error("memory_files entries must be strings", value.meta().clone());
                    None
                }
            })
            .collect::<Vec<_>>();
        let auto_load_memory = properties
            .ensure_bool("auto_load_memory", false)
            .map(|(_, v, _)| v)
            .unwrap_or(true);
        // Advanced Streaming
        let realtime_streaming = properties
            .ensure_bool("realtime_streaming", false)
            .map(|(_, v, _)| v)
            .unwrap_or(false);
        let enhanced_metadata = properties
            .ensure_bool("enhanced_metadata", false)
            .map(|(_, v, _)| v)
            .unwrap_or(false);
        let stream_metadata = properties
            .ensure_bool("stream_metadata", false)
            .map(|(_, v, _)| v)
            .unwrap_or(false);
        // Advanced Authentication
        let auth_token = properties
            .ensure_string("auth_token", false)
            .map(|(_, v, _)| v);
        let custom_headers = properties
            .ensure_string("custom_headers", false)
            .map(|(_, v, _)| v);
        let custom_auth = properties
            .ensure_string("custom_auth", false)
            .map(|(_, v, _)| v);

        let (remaining, errors) = properties.finalize();

        let mut errors = errors;
        for (k, (span, _)) in remaining {
            errors.push(Error::new(format!("Unsupported property: {k}"), span));
        }

        if !errors.is_empty() {
            return Err(errors);
        }

        Ok(UnresolvedClaudeCode {
            model,
            plan_model,
            execution_model,
            system_prompt,
            append_system_prompt,
            max_turns,
            max_thinking_tokens,
            continue_conversation,
            resume_session,
            allowed_tools,
            disallowed_tools,
            permission_mode,
            permission_prompt_tool_name,
            cwd,
            add_dirs,
            settings,
            claude_code_binary,
            node_binary,
            output_format,
            api_key,
            // SDK-Specific Features
            subagents,
            auto_detect_subagents: Some(auto_detect_subagents),
            hooks,
            slash_commands,
            memory_files,
            auto_load_memory: Some(auto_load_memory),
            // Advanced Streaming
            realtime_streaming: Some(realtime_streaming),
            enhanced_metadata: Some(enhanced_metadata),
            stream_metadata: Some(stream_metadata),
            // Advanced Authentication
            auth_token,
            custom_headers,
            custom_auth,
            // Timeout Configuration
            timeout_ms,
            haiku_model,
            extra_args,
            mcp_servers,
            allowed_metadata,
            supported_request_modes,
            finish_reason_filter,
        })
    }
}

#[derive(Clone)]
pub struct ResolvedClaudeCode {
    pub model: String,
    pub plan_model: Option<String>,
    pub execution_model: Option<String>,
    pub haiku_model: Option<String>,
    pub system_prompt: Option<String>,
    pub append_system_prompt: Option<String>,
    pub max_turns: Option<u32>,
    pub max_thinking_tokens: Option<u32>,
    pub continue_conversation: bool,
    pub resume_session: Option<String>,
    pub allowed_tools: Vec<String>,
    pub disallowed_tools: Vec<String>,
    pub permission_mode: Option<String>,
    pub permission_prompt_tool_name: Option<String>,
    pub cwd: Option<String>,
    pub add_dirs: Vec<String>,
    pub settings: Option<String>,
    pub claude_code_binary: Option<String>,
    pub node_binary: Option<String>,
    pub output_format: Option<String>,
    pub api_key: Option<String>,
    // SDK-Specific Features
    pub subagents: Vec<String>,
    pub auto_detect_subagents: bool,
    pub hooks: Option<String>,
    pub slash_commands: Vec<String>,
    pub memory_files: Vec<String>,
    pub auto_load_memory: bool,
    // Advanced Streaming
    pub realtime_streaming: bool,
    pub enhanced_metadata: bool,
    pub stream_metadata: bool,
    // Advanced Authentication
    pub auth_token: Option<String>,
    pub custom_headers: Option<String>,
    pub custom_auth: Option<String>,
    // Timeout Configuration
    pub timeout_ms: Option<u64>,
    pub extra_args: IndexMap<String, Option<String>>,
    pub mcp_servers: Option<serde_json::Value>,
    pub allowed_metadata: AllowedRoleMetadata,
    pub supported_request_modes: SupportedRequestModes,
    pub finish_reason_filter: FinishReasonFilter,
}

impl ResolvedClaudeCode {
    pub fn allowed_roles(&self) -> Vec<String> {
        vec![
            "user".to_string(),
            "assistant".to_string(),
            "system".to_string(),
        ]
    }

    pub fn default_role(&self) -> String {
        "user".to_string()
    }
}
