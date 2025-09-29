//! BAML Claude Code CLI tool
//!
//! This binary provides command-line utilities for the BAML Claude Code provider.

use baml_claude_code::VERSION;

fn main() {
    println!("BAML Claude Code Provider v{}", VERSION);
    println!("This is a Python package. Use the Python API instead:");
    println!("  from baml_claude_code import ClaudeCodeClient");
    println!("  client = ClaudeCodeClient()");
}
