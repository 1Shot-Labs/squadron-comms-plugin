# Quick Start Guide

Get Squadron Comms Plugin running in 5 minutes.

## 1. Install Prerequisites

**PortAudio Library** (required for audio playback):

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install libportaudio2
```

**macOS:**
```bash
brew install portaudio
```

**Windows:**
PortAudio usually installs automatically. If you get errors, run:
```powershell
pip install --force-reinstall sounddevice soundfile
```

## 2. Get ElevenLabs API Key

1. Go to [elevenlabs.io](https://elevenlabs.io)
2. Sign up or log in
3. Navigate to Settings → API Keys
4. Copy your API key

## 3. Install Plugin

```bash
# Start Claude
claude

# In Claude, add marketplace and install plugin
/plugin marketplace add 1Shot-Labs/marketplace
/plugin install squadron-comms
```

## 4. Configure API Key

**macOS / Linux:**
```bash
# Set your ElevenLabs API key
export ELEVENLABS_API_KEY="your_api_key_here"

# Make it permanent
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
# Set permanently (user-level)
[System.Environment]::SetEnvironmentVariable('ELEVENLABS_API_KEY', 'your_api_key_here', 'User')

# Restart Claude Code for changes to take effect
```

## 5. Verify Installation

**Important:** Restart Claude Code after installing the plugin.

```bash
# Exit Claude Code (Ctrl+D or type 'exit')
# Then start it again
claude
```

Run the setup verification command:
```bash
/squadron-comms:verify-setup
```

This checks all requirements and provides specific troubleshooting if anything is misconfigured.

Then check agents are available:
```bash
/agents
```

You should see:
- `red-agent` (General Purpose)
- `gold-agent` (Analysis & Research)
- `blue-agent` (Performance & Optimization)
- `green-agent` (Polish & UX)

> **Note:** Agents are loaded at session start. If you don't see them, restart Claude Code.

## 6. Test Voice Broadcast

In Claude, add **"with voice comms"** to activate voice broadcasting:
```
Analyze the authentication module with voice comms
```

You should hear:
- **Commander:** "Commander here. Deploying Red Squadron for authentication analysis."
- **Red Leader:** "Red Leader here. Beginning code analysis of authentication module."

## 7. Try Some Examples

**To activate voice comms, include any of these keywords in your request:**
- "with voice comms"
- "with voice updates"
- "announce your progress"
- "broadcast updates"

### Parallel Analysis
```
Analyze the database schema and review the API endpoints at the same time. Announce progress with voice.
```

### Performance Optimization
```
Optimize the slow dashboard loading with voice updates
```

### Accessibility Check
```
Make sure our app meets WCAG AA standards. Use voice comms to keep me updated.
```

## Common Commands

```bash
# View recent broadcasts
/squadron-comms:mission-status

# List available agents
/agents

# Check plugin status
/plugin list
```

## Troubleshooting

**No audio?**
```bash
# Test MPV
mpv https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3

# Check API key
echo $ELEVENLABS_API_KEY
```

**Agents not showing?**
```bash
# Restart Claude Code first (agents load at session start)
# Exit with Ctrl+D, then restart: claude

# If still not showing, reinstall
/plugin uninstall squadron-comms
/plugin install squadron-comms
# Then restart Claude Code again
```

**Rate limit errors?**
- Wait 60 seconds between broadcasts
- Check your ElevenLabs plan limits

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [examples](skills/comms/examples/broadcast-examples.md) for usage patterns
- See [INSTALL.md](INSTALL.md) for detailed setup options

## Squadron Quick Reference

| Squadron | Color | Use For |
|----------|-------|---------|
| Red | 🔴 | General tasks |
| Gold | 🟡 | Analysis & research |
| Blue | 🔵 | Performance |
| Green | 🟢 | Polish & UX |

**Ready to coordinate your squadron!** 🚀
