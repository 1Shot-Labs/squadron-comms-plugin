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
- Played through system audio
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

To broadcast a voice message, follow these steps:

1. **Identify Your Squadron**: Determine your call sign and voice ID from the table above
2. **Generate TTS**: Use ElevenLabs to convert your message to speech
3. **Play & Log**: Play the audio and append to mission log

### Example: Red Squadron Broadcast

```markdown
I'll broadcast a mission start announcement:

1. Generate TTS using Red Leader's voice
2. Play the audio with file locking
3. Log to mission-log.jsonl
```

**Step 1: Generate TTS**
```
mcp__elevenlabs__text_to_speech(
  text="Red Leader here. Beginning code analysis of authentication module.",
  voice_id="onwK4e9ZLuTAKqWW03F9",
  speed=1.1,
  output_directory="${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio"
)
```

**Step 2: Play & Log (single atomic command)**
```bash
flock ${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio.lock mpv --no-video --really-quiet /path/to/generated.mp3 && echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%S.000Z)'","callSign":"Red Leader","squadron":"red","message":"Red Leader here. Beginning code analysis of authentication module."}' >> ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

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

## File Locking

Always use `flock` to prevent audio overlap when multiple agents broadcast simultaneously:

```bash
flock ${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio.lock [audio command]
```

This ensures only one agent broadcasts at a time.

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
├── .audio/                     # Generated TTS audio files
├── .audio.lock                 # File lock for audio playback
└── mission-log.jsonl          # Broadcast history
```

## Troubleshooting

**Audio not playing:**
- Ensure `mpv` is installed: `which mpv`
- Check ElevenLabs API key is configured: `echo $ELEVENLABS_API_KEY`
- Verify audio file was generated successfully

**File lock errors:**
- The lock prevents simultaneous broadcasts - this is expected behavior
- Wait for current broadcast to complete before next one

**Mission log not updating:**
- Check write permissions on `mission-log.jsonl`
- Ensure `${CLAUDE_PLUGIN_ROOT}` resolves correctly

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
