# Squadron Comms Plugin

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/1Shot-Labs/squadron-comms-plugin/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet.svg)](https://claude.ai/code)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-green.svg)](https://elevenlabs.io)

> Voice communication system with ElevenLabs TTS for multi-agent coordination in Claude Code

A Claude Code plugin that enables voice broadcasting for coordinated multi-agent operations. Spawn colored squadron agents (Red, Gold, Blue, Green) that announce their progress using distinct ElevenLabs voices while working on tasks in parallel.

## Features

- **🎯 Four Specialized Squadron Agents**: Each with unique voice profiles and mission focuses
  - **Red Squadron** (Daniel, British) - General purpose tasks
  - **Gold Squadron** (Joseph, British) - Analysis and research
  - **Blue Squadron** (Jeremy, American-Irish) - Performance and optimization
  - **Green Squadron** (Matilda, American) - Polish and UX improvements

- **🎙️ Voice Broadcasting**: Real-time TTS announcements using ElevenLabs
- **📝 Mission Logging**: All broadcasts logged to JSONL for history
- **🔒 Concurrent Safe**: File locking prevents audio overlap
- **🎨 Color-Coded**: Visual squadron identification in Claude Code
- **📡 Commander Role**: Main agent can coordinate squadrons

## Quick Start

### 1. Prerequisites

- Claude Code CLI installed
- ElevenLabs API key ([get one here](https://elevenlabs.io))
- PortAudio library (for audio playback)

**Install PortAudio:**

<details>
<summary><strong>macOS</strong></summary>

PortAudio usually installs automatically when the ElevenLabs MCP server is installed. If you encounter audio playback issues:

```bash
brew install portaudio
```

Verify installation:
```bash
brew list portaudio
```
</details>

<details>
<summary><strong>Linux (Ubuntu/Debian)</strong></summary>

Install PortAudio library:

```bash
sudo apt-get update
sudo apt-get install libportaudio2
```

For development headers (if needed):
```bash
sudo apt-get install portaudio19-dev
```

Verify installation:
```bash
dpkg -l | grep libportaudio2
```
</details>

<details>
<summary><strong>Linux (Fedora/RHEL)</strong></summary>

Install PortAudio library:

```bash
sudo dnf install portaudio
```

Verify installation:
```bash
rpm -qa | grep portaudio
```
</details>

<details>
<summary><strong>Windows</strong></summary>

PortAudio usually installs automatically when the ElevenLabs MCP server is installed via `uvx elevenlabs-mcp`.

If you encounter "PortAudio library not found" errors:

1. Ensure Python is installed from [python.org](https://www.python.org/downloads/)
2. Reinstall audio packages:
   ```powershell
   pip install --force-reinstall sounddevice soundfile
   ```
3. Restart Claude Code

> **Note:** On Windows, PortAudio typically installs automatically as part of the sounddevice package dependencies. Manual installation is rarely needed.

</details>

### 2. Installation

**Option A: From Marketplace (Recommended)**
```bash
# Add the 1Shot Labs marketplace
/plugin marketplace add 1Shot-Labs/marketplace

# Install the plugin
/plugin install squadron-comms
```

**Option B: Local Development**
```bash
# Clone the repository
git clone https://github.com/1Shot-Labs/squadron-comms-plugin.git

# Load the plugin
claude --plugin-dir ./squadron-comms-plugin
```

### 3. Configure ElevenLabs API Key

Set your ElevenLabs API key as an environment variable:

<details>
<summary><strong>macOS / Linux</strong></summary>

**Temporary (current session only):**
```bash
export ELEVENLABS_API_KEY="your_api_key_here"
```

**Permanent:**

Add to your shell configuration file:
```bash
# For bash
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# For zsh
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

Verify it's set:
```bash
echo $ELEVENLABS_API_KEY
```
</details>

<details>
<summary><strong>Windows</strong></summary>

**Temporary (current session only):**

PowerShell:
```powershell
$env:ELEVENLABS_API_KEY="your_api_key_here"
```

Command Prompt:
```cmd
set ELEVENLABS_API_KEY=your_api_key_here
```

**Permanent (User-level):**

PowerShell (recommended):
```powershell
[System.Environment]::SetEnvironmentVariable('ELEVENLABS_API_KEY', 'your_api_key_here', 'User')
```

Or via GUI:
1. Open Start Menu → Search "Environment Variables"
2. Click "Edit environment variables for your account"
3. Under "User variables", click "New"
4. Variable name: `ELEVENLABS_API_KEY`
5. Variable value: `your_api_key_here`
6. Click OK
7. **Restart Claude Code** for changes to take effect

Verify it's set:

PowerShell:
```powershell
$env:ELEVENLABS_API_KEY
```

Command Prompt:
```cmd
echo %ELEVENLABS_API_KEY%
```
</details>

### 4. Verify Installation

Run the setup verification command to check all requirements:
```bash
/squadron-comms:verify-setup
```

This will verify:
- Environment variables are set
- PortAudio is installed and working
- ElevenLabs API connection works
- Squadron voice profiles are accessible
- File permissions are correct

### 5. Check Agents Loaded

**Important:** After installing the plugin, you need to **restart Claude Code** for the agents to become available.

Exit Claude Code and restart it, then check that the agents are loaded:
```bash
/agents
```

You should see the squadron agents listed:
- `red-agent` (Red Squadron)
- `gold-agent` (Gold Squadron)
- `blue-agent` (Blue Squadron)
- `green-agent` (Green Squadron)

> **Note:** If you don't see the agents after installation, restart Claude Code. Agents are loaded at session start.

## Usage

### Spawning Squadron Agents

Use the Task tool to spawn squadron agents. Each agent automatically has the `comms` skill and will broadcast voice updates.

**Example: Spawn Red Squadron for general task**
```
Could you analyze the authentication module?

> I'll deploy Red Squadron for this task.
> [Red Squadron broadcasts: "Red Leader here. Beginning code analysis of authentication module."]
```

**Example: Deploy multiple squadrons in parallel**
```
Analyze the codebase architecture and optimize the slow database queries.

> I'll deploy Gold Squadron for architecture analysis and Blue Squadron for database optimization.
> [Gold broadcasts: "Gold Leader here. Initiating architecture analysis."]
> [Blue broadcasts: "Blue Leader here. Beginning database query optimization."]
```

### Squadron Specializations

Choose the right squadron for the job:

| Squadron | Color | Use For | Example Tasks |
|----------|-------|---------|---------------|
| **Red** | 🔴 Red | General purpose | Testing, file operations, debugging |
| **Gold** | 🟡 Yellow | Analysis & Research | Code archaeology, documentation review, dependency analysis |
| **Blue** | 🔵 Blue | Performance & Optimization | Profiling, query optimization, bundle size reduction |
| **Green** | 🟢 Green | Polish & UX | Accessibility, error messages, visual consistency |

### Voice Broadcasting

All squadron agents have access to the `comms` skill:

```markdown
Example broadcast flow:
1. Agent generates TTS using their squadron voice
2. Audio plays through system speakers
3. Broadcast logged to mission-log.jsonl
```

**Typical broadcast pattern:**
- **Mission Start**: "Red Leader here. Beginning authentication module analysis."
- **Progress Update**: "Red Leader reporting. Found 3 potential race conditions."
- **Mission Complete**: "Red Leader. Analysis complete. Results ready for review."

### Commands

**`/squadron-comms:verify-setup`**
Verify that the plugin is properly configured and all requirements are met:
```bash
/squadron-comms:verify-setup
```

Checks:
- Environment variables (ELEVENLABS_API_KEY)
- PortAudio installation
- ElevenLabs MCP server connection
- ElevenLabs API connection
- Squadron voice availability
- File permissions

**`/squadron-comms:mission-status`**
Display recent voice broadcasts from the mission log:
```bash
/squadron-comms:mission-status
```

Shows the last 10 broadcasts with timestamps, call signs, and messages.

## Configuration

### Voice Profiles

Each squadron has a pre-configured ElevenLabs voice:

| Squadron | Call Sign | Voice ID | Voice Name | Speed |
|----------|-----------|----------|------------|-------|
| Commander | Commander | `pqHfZKP75CvOlQylNhV4` | Bill | 1.2 |
| Red | Red Leader | `onwK4e9ZLuTAKqWW03F9` | Daniel | 1.1 |
| Gold | Gold Leader | `Zlb1dXrM653N07WRdFW3` | Joseph | 1.1 |
| Blue | Blue Leader | `bVMeCyTHy58xNoL34h3p` | Jeremy | 1.1 |
| Green | Green Leader | `XrExE9yKIg1WjnnlVkGX` | Matilda | 1.1 |

### Mission Log

All broadcasts are logged to:
```
${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

**Log entry format:**
```json
{
  "timestamp": "2025-01-17T12:34:56.000Z",
  "callSign": "Red Leader",
  "squadron": "red",
  "message": "Beginning code analysis of authentication module."
}
```

### Audio Files

Generated TTS audio is stored in:
```
${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio/
```

Audio files are automatically created and can be cleaned up periodically.

## Examples

### Example 1: Parallel Task Execution

**User Request:**
```
Analyze the database schema and review the API endpoints at the same time.
```

**Claude Response:**
```
I'll deploy Gold Squadron for schema analysis and Red Squadron for API review.
```

**Voice Broadcasts:**
```
[Gold Leader]: "Gold Leader here. Initiating database schema analysis."
[Red Leader]: "Red Leader here. Beginning API endpoint review."
[Both work in parallel]
[Gold Leader]: "Gold Leader. Schema analysis complete. Identified 12 tables with relationships mapped."
[Red Leader]: "Red Leader. API review complete. Found 23 endpoints across 4 controllers."
```

### Example 2: Optimization Pipeline

**User Request:**
```
Make the dashboard load faster.
```

**Claude Response:**
```
I'll deploy Blue Squadron to optimize dashboard performance.
```

**Voice Broadcasts:**
```
[Blue Leader]: "Blue Leader here. Baseline dashboard load time is 3.2 seconds. Beginning optimization."
[Blue Leader]: "Blue Leader reporting. Reduced database queries from 15 to 3 using eager loading."
[Blue Leader]: "Blue Leader reporting. Implemented code splitting for dashboard components."
[Blue Leader]: "Blue Leader. Optimization complete. Load time reduced to 1.1 seconds. 66% improvement."
```

### Example 3: Accessibility Audit

**User Request:**
```
Make sure our app meets WCAG AA standards.
```

**Claude Response:**
```
I'll deploy Green Squadron for accessibility compliance.
```

**Voice Broadcasts:**
```
[Green Leader]: "Green Leader here. Beginning WCAG AA accessibility audit."
[Green Leader]: "Green Leader reporting. Identified 8 contrast ratio violations."
[Green Leader]: "Green Leader reporting. Missing ARIA labels on 12 interactive elements."
[Green Leader]: "Green Leader. Audit complete. All WCAG AA violations remediated."
```

## Advanced Usage

### Custom Voice Broadcasts

Agents can customize their broadcast style based on mission context:

**Technical Details:**
```
Red Leader reporting. Analyzed 47 functions. Found 3 potential race conditions in session handling.
```

**Urgent Alerts:**
```
Blue Leader. Critical: Memory leak detected in user session handler. Requires immediate attention.
```

**Multi-Squadron Coordination:**
```
Gold Leader to Blue Leader. Analysis reveals performance bottleneck in database layer.
Blue Leader acknowledging. Will optimize database query performance.
```

### Mission Log Analysis

Parse the mission log for insights:

```bash
# Show all Red Squadron broadcasts
grep '"squadron":"red"' ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl

# Count broadcasts by squadron
jq -r '.squadron' ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl | sort | uniq -c

# Show today's broadcasts
grep $(date -u +%Y-%m-%d) ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

## Troubleshooting

### Audio not playing

**Check mpv installation:**
```bash
which mpv
# Should output: /usr/bin/mpv or /usr/local/bin/mpv
```

**Check ElevenLabs API key:**
```bash
echo $ELEVENLABS_API_KEY
# Should output your API key
```

**Test mpv:**
```bash
# Download a test file and play it
mpv --no-video https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3
```

### ElevenLabs API errors

**Invalid API key:**
```
Error: Invalid API key
```
Solution: Check that `ELEVENLABS_API_KEY` is set correctly.

**Rate limit exceeded:**
```
Error: Rate limit exceeded
```
Solution: Wait a moment before broadcasting again. ElevenLabs has rate limits on TTS generation.

**Insufficient credits:**
```
Error: Insufficient credits
```
Solution: Check your ElevenLabs account and add credits.

### File lock issues

**Broadcasts being skipped:**
This is expected behavior when multiple agents try to broadcast simultaneously. The file lock ensures only one agent speaks at a time.

**Lock file stuck:**
```bash
# Remove stuck lock file
rm ${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio.lock
```

### Mission log not updating

**Check permissions:**
```bash
ls -la ${CLAUDE_PLUGIN_ROOT}/skills/comms/
# Ensure mission-log.jsonl is writable
```

**Create missing log file:**
```bash
touch ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

## Development

### Project Structure

```
squadron-comms-plugin/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── agents/
│   ├── red-agent.md          # Red Squadron agent
│   ├── gold-agent.md         # Gold Squadron agent
│   ├── blue-agent.md         # Blue Squadron agent
│   └── green-agent.md        # Green Squadron agent
├── skills/
│   └── comms/
│       ├── SKILL.md          # Comms skill documentation
│       ├── scripts/
│       │   └── broadcast.sh  # Broadcast helper script
│       └── examples/
│           └── broadcast-examples.md
├── commands/
│   └── mission-status.md     # Mission status command
├── .mcp.json                 # ElevenLabs MCP server config
├── README.md                 # This file
├── CHANGELOG.md              # Version history
└── LICENSE                   # MIT License
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Testing

Test the plugin locally:

```bash
# Load plugin in development mode
claude --plugin-dir ./squadron-comms-plugin

# Test squadron agents
# In Claude, ask to spawn agents and verify voice broadcasts work
```

## Roadmap

- [ ] Custom voice profile configuration
- [ ] Web dashboard for mission log visualization
- [ ] Additional squadron types (Orange, Purple, etc.)
- [ ] Integration with other TTS providers
- [ ] Voice command recognition (bidirectional comms)
- [ ] Team collaboration features (shared mission logs)

## Credits

- **ElevenLabs**: TTS voice generation
- **Claude Code**: Plugin platform
- **MPV**: Audio playback

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/1Shot-Labs/squadron-comms-plugin/issues)
- **Discussions**: [GitHub Discussions](https://github.com/1Shot-Labs/squadron-comms-plugin/discussions)
- **Documentation**: [Wiki](https://github.com/1Shot-Labs/squadron-comms-plugin/wiki)

---

Made with ❤️ by [1Shot Labs](https://1shotlabs.com)

**Ready to coordinate your squadron? Install now and deploy your agents!**
