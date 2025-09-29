//! NAPI-RS bindings for TypeScript integration

use napi::bindgen_prelude::*;
use napi_derive::napi;

/// Get the version of the BAML Claude Code provider
#[napi]
pub fn get_version() -> String {
    crate::VERSION.to_string()
}

/// Initialize the Claude Code provider
#[napi]
pub async fn initialize_provider() -> Result<String, napi::Error> {
    match crate::ClaudeCodeProvider::with_defaults() {
        Ok(_provider) => Ok("Claude Code provider initialized successfully".to_string()),
        Err(e) => Err(napi::Error::new(
            napi::Status::GenericFailure,
            format!("Failed to initialize Claude Code provider: {}", e),
        )),
    }
}

/// Check if the provider is available
#[napi]
pub fn is_provider_available() -> bool {
    crate::ClaudeCodeProvider::with_defaults().is_ok()
}
