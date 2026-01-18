# Quick Start Guide

Get Squadron Comms Plugin running in 5 minutes.

## 1. Install Prerequisites

```bash
# Install MPV (choose your OS)
brew install mpv                    # macOS
sudo apt install mpv                # Ubuntu/Debian
sudo dnf install mpv                # Fedora
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
/plugin marketplace add 1Shot-Labs/squadron-comms-plugin
/plugin install squadron-comms
```

## 4. Configure API Key

```bash
# Set your ElevenLabs API key
export ELEVENLABS_API_KEY="your_api_key_here"

# Make it permanent (choose your shell)
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## 5. Verify Installation

```bash
# Start Claude again
claude

# Check agents are available
/agents
```

You should see:
- `red-agent` (General Purpose)
- `gold-agent` (Analysis & Research)
- `blue-agent` (Performance & Optimization)
- `green-agent` (Polish & UX)

## 6. Test Voice Broadcast

In Claude:
```
Spawn Red Squadron and have them announce "Squadron Comms operational"
```

You should hear: **"Red Leader here. Squadron Comms operational."**

## 7. Try Some Examples

### Parallel Analysis
```
Analyze the database schema and review the API endpoints at the same time
```

### Performance Optimization
```
Optimize the slow dashboard loading
```

### Accessibility Check
```
Make sure our app meets WCAG AA standards
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
# Reinstall plugin
/plugin uninstall squadron-comms
/plugin install squadron-comms
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
