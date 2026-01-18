# Changelog

All notable changes to the Squadron Comms Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-17

### Added

- Initial release of Squadron Comms Plugin
- Four specialized squadron agents:
  - Red Squadron (General Purpose) - Daniel voice
  - Gold Squadron (Analysis & Research) - Joseph voice
  - Blue Squadron (Performance & Optimization) - Jeremy voice
  - Green Squadron (Polish & UX) - Matilda voice
- Commander role with Bill voice (authoritative American)
- Voice broadcasting skill (`comms`) with ElevenLabs TTS integration
- Mission logging to JSONL format
- File locking for concurrent audio playback
- Mission status command (`/squadron-comms:mission-status`)
- Broadcast helper script for shell usage
- Comprehensive documentation and examples
- ElevenLabs MCP server configuration
- Color-coded squadron identification

### Technical Details

- Plugin structure following Claude Code best practices
- Agent definitions with voice profiles
- Skills directory with comms skill
- Commands for mission status
- Example broadcasts and usage patterns
- Proper file locking with flock
- JSONL mission log format

### Dependencies

- Claude Code CLI
- ElevenLabs API key
- mpv media player
- mcp-eleven-labs MCP server

## [Unreleased]

### Added

- Cross-platform file locking using Python `filelock` library
- `/squadron-comms:verify-setup` command for comprehensive installation validation
- `play_audio.py` script for Windows-compatible audio playback and logging
- `requirements.txt` for Python dependencies
- Windows-specific installation instructions across all documentation

### Changed

- File locking now uses Python instead of Unix-only `flock` command
- All squadron agents now use Opus model instead of Sonnet
- Improved documentation accuracy for environment variable setup
- Added Python 3.8+ as a prerequisite

### Fixed

- Windows compatibility for file locking (flock doesn't exist on Windows)
- ElevenLabs MCP package name corrected to `elevenlabs-mcp`
- Documentation now correctly states to restart Claude Code, not terminal
- Plugin.json validation errors resolved

### Planned

- Custom voice profile configuration
- Web dashboard for mission log visualization
- Additional squadron types
- Integration with other TTS providers
- Voice command recognition
- Team collaboration features

---

[1.0.0]: https://github.com/1Shot-Labs/squadron-comms-plugin/releases/tag/v1.0.0
