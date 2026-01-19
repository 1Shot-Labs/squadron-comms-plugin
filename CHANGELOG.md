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

## [1.1.0] - 2025-01-18

### Changed - Major Redesign

- **Switched to ElevenLabs MCP play_audio tool** for all audio playback
  - Removes dependency on mpv media player
  - Uses PortAudio library instead (cross-platform)
  - Consistent behavior across Windows, macOS, and Linux
  - Eliminates GUI window popups during playback

- **Simplified broadcast process** from 2 steps to 3 steps:
  1. Generate TTS audio with `mcp__elevenlabs__text_to_speech`
  2. Play audio with `mcp__elevenlabs__play_audio`
  3. Log broadcast with `log_broadcast.sh`

- **Removed Python file locking**
  - File locking rarely needed in practice
  - TTS generation naturally serializes broadcasts
  - Simplified codebase and dependencies

### Added

- `log_broadcast.sh` - Simple mission logging script
- PortAudio installation instructions for all platforms
- `/squadron-comms:verify-setup` command updated for PortAudio checks
- Comprehensive Windows installation documentation

### Removed

- `play_audio.py` script (no longer needed)
- `filelock` dependency
- mpv media player requirement
- Complex file locking mechanism

### Fixed

- Windows encoding issues (replaced Unicode symbols with ASCII)
- ElevenLabs MCP package name corrected to `elevenlabs-mcp`
- Documentation accuracy (restart Claude Code, not terminal)
- Plugin.json validation errors
- All squadron agents now use Opus model

### Planned

- Custom voice profile configuration
- Web dashboard for mission log visualization
- Additional squadron types
- Integration with other TTS providers
- Voice command recognition
- Team collaboration features

---

[1.0.0]: https://github.com/1Shot-Labs/squadron-comms-plugin/releases/tag/v1.0.0
