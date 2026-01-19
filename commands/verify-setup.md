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
- [ERROR] **FAILED**: Environment variable not configured
- Provide setup instructions for the user's platform

If set but empty:
- [WARN] **WARNING**: Environment variable is set but empty
- Ask user to configure it properly

If set with a value:
- [OK] **PASSED**: Environment variable configured (show first 8 chars only for security)

### 2. Check PortAudio Installation

Test if PortAudio is installed and the ElevenLabs MCP play_audio tool works:

Try to play a test audio file using the MCP tool (if available):
- Use `mcp__elevenlabs__play_audio` with a sample file

Or manually check PortAudio:
- **Linux**: `dpkg -l | grep libportaudio2`
- **macOS**: `brew list portaudio`
- **Windows**: Check if Python sounddevice package works: `python -c "import sounddevice"`

If PortAudio not found:
- [ERROR] **FAILED**: PortAudio not installed
- **Linux**: Install with `sudo apt-get install libportaudio2`
- **macOS**: Install with `brew install portaudio`
- **Windows**: Reinstall with `pip install --force-reinstall sounddevice soundfile`

If PortAudio found:
- [OK] **PASSED**: PortAudio installed and working

### 3. Check Bash Availability

Verify bash is available for mission logging:
- Run: `bash --version`

If not found (rare on Windows):
- [WARN] **WARNING**: bash not available
- Mission logging may not work
- Install Git Bash for Windows

If found:
- [OK] **PASSED**: bash available for logging

### 4. Check ElevenLabs MCP Server Connection

Test the ElevenLabs MCP server:
- Try to list available voices using the ElevenLabs MCP tools
- Use: `mcp__elevenlabs__search_voices` tool with empty search

If connection fails:
- [ERROR] **FAILED**: Cannot connect to ElevenLabs API
- Check API key validity
- Check internet connection
- Verify MCP server is running

If connection succeeds:
- [OK] **PASSED**: Connected to ElevenLabs API
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
- [WARN] **WARNING**: Some squadron voices not available in your account
- List missing voices
- Note: Voices can still work if they're in the professional voice library

If all found:
- [OK] **PASSED**: All squadron voice profiles available

### 6. Check File Permissions

Verify the plugin can write to necessary directories:
- Check if `${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio/` is writable
- Check if `${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl` is writable

Test by attempting to create a test file in each location.

If write fails:
- [ERROR] **FAILED**: Permission denied for [location]
- Provide troubleshooting steps

If write succeeds:
- [OK] **PASSED**: File permissions correct

### 7. Check Squadron Agents

Verify all agents are loaded:
- Check that red-agent, gold-agent, blue-agent, green-agent are available

If agents missing:
- [WARN] **WARNING**: Agents not loaded
- Instruct user to restart Claude Code

If all present:
- [OK] **PASSED**: All 4 squadron agents loaded

## Output Format

Present results in a clear summary table:

```
Squadron Comms Setup Verification
═════════════════════════════════════════════

[OK]   ELEVENLABS_API_KEY:     Configured (sk_daf7a...)
[OK]   PortAudio Library:      Installed and working
[OK]   Bash Shell:             Available for logging
[OK]   ElevenLabs MCP Server:  Connected
[OK]   ElevenLabs API:         Connected (42 voices available)
[WARN] Squadron Voices:        4/5 available (Bill missing)
[OK]   File Permissions:       Write access verified
[OK]   Squadron Agents:        All 4 agents loaded

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
