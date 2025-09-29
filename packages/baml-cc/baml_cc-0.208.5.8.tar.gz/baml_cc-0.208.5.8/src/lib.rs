//! BAML Claude Code Provider
//!
//! This crate provides a Claude Code provider for BAML, enabling advanced
//! Claude Code features including subagents, hooks, slash commands, and more.

pub mod error;

pub use error::ClaudeCodeError;

/// Version of the BAML Claude Code provider
pub const VERSION: &str = env!("CARGO_PKG_VERSION");

/// Upstream BAML version this package is based on
pub const UPSTREAM_VERSION: &str = "0.208.5";
pub const UPSTREAM_COMMIT: &str = "main";
pub const PATCH_VERSION: &str = "1";

// NAPI-RS bindings for TypeScript
#[cfg(feature = "napi")]
mod napi_bindings;

#[cfg(feature = "napi")]
use napi_bindings::*;
