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

### Dependencies (v1.0.0)

- Claude Code CLI
- ElevenLabs API key
- elevenlabs-mcp MCP server
- No audio playback dependencies in v1.0.0 (added in v1.1.0)

## [1.1.0] - 2025-01-18

### Changed - Audio Locking & Path Resolution

- **Added cross-platform audio file locking** to prevent simultaneous broadcasts
  - New `play_with_lock.py` script with FileLock library
  - Uses Python sounddevice + soundfile for audio playback
  - Removes dependency on external media players (mpv)
  - PortAudio library provides cross-platform audio support
  - Automatic queuing when multiple agents broadcast concurrently

- **Created self-locating broadcast wrapper** to fix path resolution issues
  - New `broadcast.py` script handles complete broadcast workflow
  - Uses `__file__` for path discovery (no environment variables needed)
  - Agents locate script with `find` command (bulletproof across platforms)
  - Combines TTS playback + mission logging in single call
  - Fixed 90% agent failure rate from path resolution issues

- **Simplified broadcast process** from 3 manual steps to 2 steps:
  1. Generate TTS audio with `mcp__elevenlabs__text_to_speech` (anywhere)
  2. Call `broadcast.py` with audio path (handles playback + logging)

### Added

- **Commander voice support** for main agent
  - Main Claude Code agent can now broadcast as Commander (Bill voice)
  - Voice coordination between Commander and squadron leaders
  - Clear role distinction (orchestrator vs execution agents)

- `broadcast.py` - Self-locating wrapper for complete broadcast workflow
- `play_with_lock.py` - Cross-platform audio playback with file locking
- `log_broadcast.sh` - Mission logging helper script
- Dependencies: `filelock>=3.13.0`, `sounddevice>=0.4.6`, `soundfile>=0.12.1`
- Activation keywords documentation ("with voice comms", "announce progress")
- PortAudio installation instructions for all platforms
- Comprehensive Windows installation documentation

### Removed

- mpv media player dependency (replaced with sounddevice)
- ${CLAUDE_PLUGIN_ROOT} environment variable requirement (self-locating scripts)
- Manual 3-step broadcast process (automated by broadcast.py)

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
