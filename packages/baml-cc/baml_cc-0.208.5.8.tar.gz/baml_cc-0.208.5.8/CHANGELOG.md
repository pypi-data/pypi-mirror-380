# Changelog

All notable changes to the BAML Claude Code Provider will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-09-25

### Added
- Initial release of BAML Claude Code Provider
- Claude Code CLI integration
- CloudPlan authentication (default)
- API key authentication support
- Multiple model support (Sonnet, Haiku, custom)
- Subagents configuration
- Hooks support (pre/post execution)
- Slash commands functionality
- Memory files support
- Real-time streaming capabilities
- Enhanced metadata support
- Custom authentication methods
- Cross-platform installation scripts
- Python package (PyPI)
- TypeScript/Node.js package (NPM)
- Comprehensive documentation
- CLI tools for testing and validation
- GitHub Actions CI/CD pipeline
- Multi-platform binary releases

### Features
- **Core Integration**: Direct integration with Claude Code CLI
- **Authentication**: CloudPlan (default) and API key support
- **Models**: Support for Claude 3.5 Sonnet, Haiku, and custom models
- **Advanced Features**: Subagents, hooks, slash commands, memory files
- **Streaming**: Real-time response streaming with metadata
- **Cross-Platform**: Linux, macOS, Windows support
- **Package Managers**: PyPI and NPM packages
- **CLI Tools**: Command-line utilities for testing and validation

### Technical Details
- **Rust Backend**: High-performance Rust implementation
- **Python Bindings**: PyO3-based Python integration
- **TypeScript Bindings**: NAPI-based Node.js integration
- **BAML Integration**: Native BAML provider support
- **Error Handling**: Comprehensive error types and handling
- **Documentation**: Extensive documentation and examples

### Installation
- **Quick Install**: One-line installation script
- **Package Managers**: `pip install baml-claude-code` or `npm install @baml/claude-code`
- **Manual Install**: GitHub releases with pre-built binaries
- **Docker**: Container support (planned for future releases)

### Documentation
- **README**: Comprehensive usage guide
- **API Reference**: Complete API documentation
- **Examples**: Code examples and use cases
- **Troubleshooting**: Common issues and solutions
- **Migration Guide**: Upgrade instructions

---

## [Unreleased]

### Planned Features
- Docker container support
- Homebrew formula (macOS)
- Chocolatey package (Windows)
- APT/YUM repositories (Linux)
- VSCode extension integration
- JetBrains plugin support
- Advanced caching mechanisms
- Performance monitoring
- Metrics and analytics
- Enterprise features

### Known Issues
- Windows tar.gz extraction requires additional tools
- Some advanced features require Claude Code CLI updates
- Memory files path resolution on Windows

---

## Version History

- **1.0.0** - Initial release with full feature set
- **0.9.0** - Beta release (internal testing)
- **0.8.0** - Alpha release (development)

---

## Support

For support and questions:
- 📖 [Documentation](https://github.com/ViperJuice/baml-cc#readme)
- 🐛 [Issue Tracker](https://github.com/ViperJuice/baml-cc/issues)
- 💬 [Discussions](https://github.com/ViperJuice/baml-cc/discussions)

---

**Note**: This changelog follows [Keep a Changelog](https://keepachangelog.com/) format and [Semantic Versioning](https://semver.org/) principles.


