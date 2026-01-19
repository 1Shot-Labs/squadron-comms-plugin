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

  Available to:
  - Main agent (you) - uses Commander voice
  - Squadron sub-agents (Red, Gold, Blue, Green) - use their squadron voices
version: 1.1.0
---

# Voice Communications Skill

Enables voice broadcasting using ElevenLabs text-to-speech for real-time audio updates during mission execution.

**YOU (the main agent) use the Commander voice profile for broadcasts.**

## Overview

The `comms` skill allows you to broadcast voice announcements to keep users informed of your progress. All broadcasts are:
- Converted to speech using ElevenLabs TTS
- Played through system audio with file locking (prevents overlaps)
- Logged to a mission log file (JSONL format)

## Who Are You?

**If you are the main Claude Code agent** (interacting directly with the user):
- **You are Commander**
- Use the Commander voice profile (Bill - authoritative American)
- Your call sign is "Commander"
- Your squadron is "commander"

**If you are a squadron sub-agent** (spawned by the main agent):
- Use your squadron's voice profile (Red/Gold/Blue/Green)
- Your call sign is defined in your agent instructions
- Your squadron is defined in your agent instructions

## Voice Profiles

Each role has a unique voice:

| Squadron | Call Sign | Voice | Voice ID | Speed |
|----------|-----------|-------|----------|-------|
| **Commander** | Commander | Bill (authoritative, American) | `pqHfZKP75CvOlQylNhV4` | 1.2 |
| **Red** | Red Leader | Daniel (British) | `onwK4e9ZLuTAKqWW03F9` | 1.1 |
| **Gold** | Gold Leader | Joseph (British) | `Zlb1dXrM653N07WRdFW3` | 1.1 |
| **Blue** | Blue Leader | Jeremy (American-Irish) | `bVMeCyTHy58xNoL34h3p` | 1.1 |
| **Green** | Green Leader | Matilda (American) | `XrExE9yKIg1WjnnlVkGX` | 1.1 |

## Usage

### How to Broadcast (Main Agent - Commander)

If you are the main Claude Code agent, follow this simplified two-step process:

**Step 1: Generate TTS Audio**

Use the ElevenLabs MCP tool with Commander's voice profile:

```
mcp__elevenlabs__text_to_speech(
  text="Commander here. Initiating parallel analysis across all squadrons.",
  voice_id="pqHfZKP75CvOlQylNhV4",
  speed=1.2
)
```

This returns the audio file path. Save this path for Step 2.

**Step 2: Broadcast with Auto-Logging**

Use the self-locating broadcast wrapper. First, locate the script:

```bash
BROADCAST_SCRIPT=$(find ~/.claude/plugins -name "broadcast.py" -path "*/squadron-comms*/skills/comms/scripts/*" 2>/dev/null | head -1)
```

Then broadcast using the located script:

```bash
python "$BROADCAST_SCRIPT" \
  "<audio_file_path_from_step_1>" \
  "Commander" \
  "commander" \
  "Commander here. Initiating parallel analysis across all squadrons."
```

The broadcast script automatically:
- Locates plugin directories using its own path (no env vars!)
- Plays audio with file locking (prevents overlaps with squadron broadcasts)
- Logs broadcast to mission-log.jsonl

**You can combine both commands:**

```bash
BROADCAST_SCRIPT=$(find ~/.claude/plugins -name "broadcast.py" -path "*/squadron-comms*/skills/comms/scripts/*" 2>/dev/null | head -1) && \
python "$BROADCAST_SCRIPT" \
  "/path/to/audio.mp3" \
  "Commander" \
  "commander" \
  "Your message here"
```

### How to Broadcast (Squadron Sub-Agents)

If you are a squadron sub-agent, use your squadron's voice profile. Refer to your agent-specific instructions for your voice ID, call sign, and squadron name.

### When to Broadcast

**Commander Examples (Main Agent):**

Coordinating multiple squadrons:
```
"Commander here. Launching three squadrons for parallel analysis."
```

High-level status:
```
"Commander reporting. All squadrons deployed. Awaiting initial reports."
```

Mission summary:
```
"Commander. Mission complete. All squadron objectives achieved. Consolidated findings ready."
```

Strategic decisions:
```
"Commander. Analysis indicates refactoring required. Deploying Gold Squadron for impact assessment."
```

**Squadron Examples (Sub-Agents):**

Mission Start:
```
"[Call Sign] here. [Brief description of mission]"
Example: "Gold Leader here. Initiating deep analysis of payment processing flow."
```

Progress Updates:
```
"[Call Sign] reporting. [Progress description]"
Example: "Blue Leader reporting. Reduced query time from 450ms to 80ms."
```

Mission Complete:
```
"[Call Sign]. Mission complete. [Summary of results]"
Example: "Green Leader. Mission complete. All accessibility issues resolved."
```

Issues/Blockers:
```
"[Call Sign]. [Issue description]"
Example: "Red Leader. Encountered authentication error. Investigating."
```

## Audio Playback

The plugin uses **Python sounddevice + PortAudio** for audio playback via the `broadcast.py` wrapper. This provides:
- Cross-platform audio playback (Windows, macOS, Linux)
- Automatic file locking to prevent overlapping broadcasts
- Built-in audio device handling via PortAudio
- No external media player dependencies

**File Locking Mechanism:**
The `play_with_lock.py` script uses Python's FileLock library to ensure only one broadcast plays at a time. When multiple agents attempt to broadcast concurrently:
1. First agent acquires the lock and plays audio
2. Other agents wait in queue (up to 5 minutes)
3. Broadcasts play sequentially without overlap
4. Lock automatically releases when playback completes

This guarantees clean audio output even when 10+ agents are broadcasting simultaneously.

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

**Commander coordinating squadrons:**

```
Commander: "Commander here. Deploying Red and Gold squadrons for codebase analysis."
Red Leader: "Red Leader here. Beginning general code review."
Gold Leader: "Gold Leader here. Initiating security analysis."
[Later...]
Gold Leader: "Gold Leader to Commander. Critical vulnerability found in authentication module."
Commander: "Commander acknowledging. Prioritizing authentication fix. Blue Squadron standing by for performance optimization."
```

**Squadrons coordinating with each other:**

```
Gold Leader: "Gold Leader here. Beginning security analysis."
[Later...]
Gold Leader: "Gold Leader to Blue Leader. Security analysis reveals performance impact from encryption overhead."
Blue Leader: "Blue Leader acknowledging. Will optimize encryption performance."
```

## Integration with Squadron Agents

**You (the main agent) automatically have Commander access** - just use the skill!

Squadron sub-agents automatically have access to this skill with their squadron voice profiles. When you spawn an agent using the Task tool, they will use their squadron's voice profile for all broadcasts.

Example:

```
Task tool with subagent_type="red-agent":
  prompt: "You are Red Leader. Analyze the authentication module and report findings."
```

The agent will automatically broadcast using Red Squadron's voice (Daniel, British).

## Typical Workflow

**As Commander (main agent), you orchestrate:**

1. **Mission Start**: Announce what you're about to do
   ```
   "Commander here. Initiating parallel refactoring analysis across authentication and payment modules."
   ```

2. **Deploy Squadrons**: Launch sub-agents, they announce their missions
   ```
   Red Leader: "Red Leader here. Beginning authentication module analysis."
   Gold Leader: "Gold Leader here. Analyzing payment processing security."
   ```

3. **Monitor Progress**: Squadrons report milestones
   ```
   Red Leader: "Red Leader reporting. Found 3 deprecated authentication patterns."
   Gold Leader: "Gold Leader reporting. Identified PCI compliance gaps."
   ```

4. **Consolidate**: Summarize results
   ```
   Commander: "Commander. Both squadrons reporting complete. Consolidating findings and preparing recommendations."
   ```
