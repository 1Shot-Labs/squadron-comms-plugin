---
description: Verify Squadron Comms plugin installation and configuration
---

Run a comprehensive check of the Squadron Comms plugin setup to ensure all requirements are met and the plugin is ready to use.

## Verification Steps

Check the following in order and report results:

### 1. Check ELEVENLABS_API_KEY Environment Variable

Verify the environment variable is set:
- On Windows: Check if `$env:ELEVENLABS_API_KEY` (PowerShell) or `%ELEVENLABS_API_KEY%` (CMD) is set
- On macOS/Linux: Check if `$ELEVENLABS_API_KEY` is set

If not set:
- ❌ **FAILED**: Environment variable not configured
- Provide setup instructions for the user's platform

If set but empty:
- ⚠️ **WARNING**: Environment variable is set but empty
- Ask user to configure it properly

If set with a value:
- ✅ **PASSED**: Environment variable configured (show first 8 chars only for security)

### 2. Check MPV Installation

Test if mpv is installed and accessible using the plugin's detection logic:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/comms/scripts/play_audio.py --check-mpv
```

Or manually check:
- Unix: `which mpv` or `which mpvnet`
- Windows: `where mpv` or `where mpvnet.exe`
- Run: `mpv --version` or `mpvnet --version` to verify it works

The plugin supports multiple mpv variants:
- `mpv` (standard on Unix, available via Scoop/Chocolatey on Windows)
- `mpvnet.exe` (mpv.net on Windows)
- Common installation paths on Windows are checked automatically

If not found:
- ❌ **FAILED**: mpv not installed or not in PATH
- Provide installation instructions for user's platform

If found:
- ✅ **PASSED**: mpv installed at [path] (show version and variant)

### 3. Check Python and filelock Library

Verify Python and the filelock library:
- Run: `python3 --version` or `python --version`
- Run: `python3 -c "import filelock; print(filelock.__version__)"` or `python -c "import filelock; print(filelock.__version__)"`

If Python not found:
- ❌ **FAILED**: Python not installed
- Provide installation instructions

If filelock not found:
- ⚠️ **WARNING**: filelock library not installed
- Instruct: `pip install filelock` or `pip install -r ${CLAUDE_PLUGIN_ROOT}/requirements.txt`

If both found:
- ✅ **PASSED**: Python [version], filelock [version]

### 4. Check ElevenLabs MCP Server Connection

Test the ElevenLabs MCP server:
- Try to list available voices using the ElevenLabs MCP tools
- Use: `mcp__elevenlabs__search_voices` tool with empty search

If connection fails:
- ❌ **FAILED**: Cannot connect to ElevenLabs API
- Check API key validity
- Check internet connection
- Verify MCP server is running

If connection succeeds:
- ✅ **PASSED**: Connected to ElevenLabs API
- Show number of voices available

### 5. Check Squadron Voice Profiles

Verify the required voices are available:
- Daniel (onwK4e9ZLuTAKqWW03F9) - Red Squadron
- Joseph (Zlb1dXrM653N07WRdFW3) - Gold Squadron
- Jeremy (bVMeCyTHy58xNoL34h3p) - Blue Squadron
- Matilda (XrExE9yKIg1WjnnlVkGX) - Green Squadron
- Bill (pqHfZKP75CvOlQylNhV4) - Commander

Use the voice list from step 4 to check availability.

If any voices missing:
- ⚠️ **WARNING**: Some squadron voices not available in your account
- List missing voices
- Note: Voices can still work if they're in the professional voice library

If all found:
- ✅ **PASSED**: All squadron voice profiles available

### 6. Check File Permissions

Verify the plugin can write to necessary directories:
- Check if `${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio/` is writable
- Check if `${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl` is writable

Test by attempting to create a test file in each location.

If write fails:
- ❌ **FAILED**: Permission denied for [location]
- Provide troubleshooting steps

If write succeeds:
- ✅ **PASSED**: File permissions correct

### 7. Check Squadron Agents

Verify all agents are loaded:
- Check that red-agent, gold-agent, blue-agent, green-agent are available

If agents missing:
- ⚠️ **WARNING**: Agents not loaded
- Instruct user to restart Claude Code

If all present:
- ✅ **PASSED**: All 4 squadron agents loaded

## Output Format

Present results in a clear summary table:

```
Squadron Comms Setup Verification
═════════════════════════════════════════════

✅ ELEVENLABS_API_KEY:     Configured (sk_daf7a...)
✅ MPV Media Player:       Installed (v0.38.0)
✅ Python & filelock:      Python 3.12.1, filelock 3.20.3
✅ ElevenLabs API:         Connected (42 voices available)
⚠️  Squadron Voices:       4/5 available (Bill missing)
✅ File Permissions:       Write access verified
✅ Squadron Agents:        All 4 agents loaded

Overall Status: READY (1 warning)

Warnings:
- Voice 'Bill' (Commander) not found in account. You can still use squadron agents.

Next Steps:
1. Test voice broadcast: Spawn Red Squadron and request a test announcement
2. Check mission log: /squadron-comms:mission-status
```

If there are failures, provide specific remediation steps for each failed check.

## Error Handling

If unable to perform checks due to missing tools, explain what couldn't be verified and why.

Always end with clear next steps based on the verification results.
