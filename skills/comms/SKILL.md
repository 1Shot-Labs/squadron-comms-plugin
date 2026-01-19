---
name: comms
description: |
  Voice communication system for broadcasting updates using ElevenLabs TTS.

  Use when:
  - You need to announce mission start, progress, or completion
  - Broadcasting important findings or results
  - Alerting about issues or blockers
  - Coordinating with other agents
  - Providing status updates during long-running operations

  This skill is automatically available to all squadron agents (Red, Gold, Blue, Green).
version: 1.0.0
---

# Voice Communications Skill

Enables voice broadcasting using ElevenLabs text-to-speech for real-time audio updates during mission execution.

## Overview

The `comms` skill allows you to broadcast voice announcements to keep users informed of your progress. All broadcasts are:
- Converted to speech using ElevenLabs TTS
- Played through system audio using the ElevenLabs MCP play_audio tool
- Logged to a mission log file (JSONL format)

## Squadron Voice Profiles

Each squadron has a unique voice:

| Squadron | Call Sign | Voice | Voice ID | Speed |
|----------|-----------|-------|----------|-------|
| **Commander** | Commander | Bill (authoritative, American) | `pqHfZKP75CvOlQylNhV4` | 1.2 |
| **Red** | Red Leader | Daniel (British) | `onwK4e9ZLuTAKqWW03F9` | 1.1 |
| **Gold** | Gold Leader | Joseph (British) | `Zlb1dXrM653N07WRdFW3` | 1.1 |
| **Blue** | Blue Leader | Jeremy (American-Irish) | `bVMeCyTHy58xNoL34h3p` | 1.1 |
| **Green** | Green Leader | Matilda (American) | `XrExE9yKIg1WjnnlVkGX` | 1.1 |

## Usage

### Basic Broadcasting

To broadcast a voice message, follow these three steps:

1. **Generate TTS Audio**: Use ElevenLabs to convert your message to speech
2. **Play Audio**: Use the ElevenLabs MCP play_audio tool
3. **Log Broadcast**: Append to mission log for history

### Example: Red Squadron Broadcast

**Step 1: Generate TTS Audio**
```
mcp__elevenlabs__text_to_speech(
  text="Red Leader here. Beginning code analysis of authentication module.",
  voice_id="onwK4e9ZLuTAKqWW03F9",
  speed=1.1,
  output_directory="${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio"
)
```

The tool will return the path to the generated audio file (e.g., `/path/to/.audio/tts_Red_L_20250118_123456.mp3`).

**Step 2: Play Audio**

Use the ElevenLabs MCP play_audio tool with the file path from Step 1:

```
mcp__elevenlabs__play_audio(
  input_file_path="/path/to/.audio/tts_Red_L_20250118_123456.mp3"
)
```

**Step 3: Log Broadcast**

After playback, log the broadcast to the mission log:

```bash
bash ${CLAUDE_PLUGIN_ROOT}/skills/comms/scripts/log_broadcast.sh \
  "Red Leader" \
  "red" \
  "Red Leader here. Beginning code analysis of authentication module."
```

This creates a JSONL entry with timestamp, call sign, squadron, and message.

### When to Broadcast

**Mission Start:**
```
"[Call Sign] here. [Brief description of mission]"
Example: "Gold Leader here. Initiating deep analysis of payment processing flow."
```

**Progress Updates:**
```
"[Call Sign] reporting. [Progress description]"
Example: "Blue Leader reporting. Reduced query time from 450ms to 80ms."
```

**Mission Complete:**
```
"[Call Sign]. Mission complete. [Summary of results]"
Example: "Green Leader. Mission complete. All accessibility issues resolved."
```

**Issues/Blockers:**
```
"[Call Sign]. [Issue description]"
Example: "Red Leader. Encountered authentication error. Investigating."
```

## Audio Playback

The plugin uses the **ElevenLabs MCP play_audio tool** for audio playback. This provides:
- Cross-platform audio playback (Windows, macOS, Linux)
- Consistent behavior across all platforms
- Built-in audio device handling via PortAudio
- No external media player dependencies

**Note on Concurrent Broadcasts:**
While agents can technically broadcast simultaneously, in practice this is rare. The ElevenLabs TTS generation is sequential enough that broadcasts naturally queue. If you need strict synchronization, consider spawning agents with delays between them.

## Mission Log Format

Each broadcast is logged as a JSON line in `mission-log.jsonl`:

```json
{
  "timestamp": "2025-01-17T12:34:56.000Z",
  "callSign": "Red Leader",
  "squadron": "red",
  "message": "Beginning code analysis of authentication module."
}
```

**Squadron values:**
- `commander` - Commander
- `red` - Red Squadron
- `gold` - Gold Squadron (yellow color)
- `blue` - Blue Squadron
- `green` - Green Squadron

## Best Practices

1. **Be Concise**: Keep broadcasts short and focused
2. **Use Call Signs**: Always identify yourself with your squadron call sign
3. **Report Progress**: Broadcast at key milestones, not continuously
4. **Clear Language**: Speak in plain, professional language
5. **Coordinate**: When working with other squadrons, reference their call signs

## Directory Structure

The comms skill maintains these files:

```
skills/comms/
├── SKILL.md                    # This documentation
├── scripts/
│   └── log_broadcast.sh       # Mission log appender
├── examples/
│   └── broadcast-examples.md  # Usage examples
├── .audio/                     # Generated TTS audio files
└── mission-log.jsonl          # Broadcast history
```

## Troubleshooting

**Setup verification:**
Run `/squadron-comms:verify-setup` to check all requirements and get specific troubleshooting guidance.

**Audio not playing:**
- Check ElevenLabs API key is configured: `echo $ELEVENLABS_API_KEY` (Unix) or `echo %ELEVENLABS_API_KEY%` (Windows)
- Verify PortAudio is installed:
  - Linux: `dpkg -l | grep libportaudio2` or install with `sudo apt-get install libportaudio2`
  - macOS: Usually auto-installs with ElevenLabs MCP
  - Windows: Usually auto-installs with ElevenLabs MCP
- On Windows: Restart Claude Code after setting environment variables
- Verify audio file was generated successfully

**PortAudio errors:**
- **Linux**: Install PortAudio library: `sudo apt-get install libportaudio2 portaudio19-dev`
- **macOS**: Install via Homebrew: `brew install portaudio`
- **Windows**: PortAudio usually installs automatically, but if issues persist, reinstall Python audio packages
- Restart Claude Code after installing PortAudio

**Mission log not updating:**
- Check write permissions on `mission-log.jsonl`
- Ensure `${CLAUDE_PLUGIN_ROOT}` resolves correctly
- Verify log_broadcast.sh script has execute permissions: `chmod +x ${CLAUDE_PLUGIN_ROOT}/skills/comms/scripts/log_broadcast.sh`

**ElevenLabs MCP connection errors:**
- Verify API key is set as a Windows User environment variable (not just terminal session)
- Check internet connection
- Verify ElevenLabs API status

## Advanced Usage

### Custom Announcements

You can customize announcement style based on mission type:

**Technical Details:**
```
"Red Leader reporting. Analyzed 47 functions. Found 3 potential race conditions."
```

**Urgent Issues:**
```
"Blue Leader. Critical: Memory leak detected in user session handler."
```

**Coordination:**
```
"Gold Leader to Blue Leader. Analysis complete. Performance bottlenecks identified in database layer."
```

### Multi-Agent Coordination

When multiple squadrons work together, coordinate broadcasts:

1. Announce your mission start
2. Reference other squadrons when relevant
3. Share findings that may impact other missions
4. Coordinate completion announcements

**Example:**
```
Gold Leader: "Gold Leader here. Beginning security analysis."
[Later...]
Gold Leader: "Gold Leader to Blue Leader. Security analysis reveals performance impact from encryption overhead."
Blue Leader: "Blue Leader acknowledging. Will optimize encryption performance."
```

## Integration with Squadron Agents

All squadron agents automatically have access to this skill. When you spawn an agent using the Task tool, they will use their squadron's voice profile for all broadcasts.

Simply include the agent's call sign in their prompt:

```
Task tool with subagent_type="red-agent":
  prompt: "You are Red Leader. Analyze the authentication module and report findings."
```

The agent will automatically broadcast using Red Squadron's voice (Daniel, British).
