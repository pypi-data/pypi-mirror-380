//! Error types for the BAML Claude Code provider

use thiserror::Error;

/// Errors that can occur when using the Claude Code provider
#[derive(Error, Debug)]
pub enum ClaudeCodeError {
    #[error("Claude Code CLI not found: {0}")]
    CliNotFound(String),

    #[error("Claude Code execution failed: {0}")]
    ExecutionFailed(String),

    #[error("Invalid configuration: {0}")]
    InvalidConfig(String),

    #[error("Authentication failed: {0}")]
    AuthenticationFailed(String),

    #[error("Timeout occurred: {0}")]
    Timeout(String),

    #[error("Serialization error: {0}")]
    SerializationError(#[from] serde_json::Error),

    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),

    #[error("BAML runtime error: {0}")]
    BamlError(String),
}

/// Result type for Claude Code operations
pub type ClaudeCodeResult<T> = Result<T, ClaudeCodeError>;
