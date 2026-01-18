# Installation Guide

Complete guide to installing and configuring the Squadron Comms Plugin for Claude Code.

## Prerequisites

Before installing the plugin, ensure you have:

### 1. Claude Code CLI

Install Claude Code CLI:
```bash
# Using npm
npm install -g @anthropic/claude-code

# Or using homebrew (macOS)
brew install claude-code
```

Verify installation:
```bash
claude --version
```

### 2. ElevenLabs API Key

1. Sign up for an ElevenLabs account at [elevenlabs.io](https://elevenlabs.io)
2. Navigate to your profile settings
3. Generate an API key
4. Copy the API key (you'll need it in step 3 of installation)

### 3. MPV Media Player

The plugin uses MPV to play generated audio.

**macOS:**
```bash
brew install mpv
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mpv
```

**Fedora/RHEL:**
```bash
sudo dnf install mpv
```

**Arch Linux:**
```bash
sudo pacman -S mpv
```

**Windows:**
Download from [mpv.io](https://mpv.io/installation/) and add to PATH.

Verify MPV installation:
```bash
mpv --version
```

## Installation Methods

### Method 1: GitHub Marketplace (Recommended)

This is the easiest method for most users.

**Step 1: Add the marketplace**
```bash
claude
```

Then in Claude:
```
/plugin marketplace add 1Shot-Labs/squadron-comms-plugin
```

**Step 2: Install the plugin**
```
/plugin install squadron-comms
```

**Step 3: Configure ElevenLabs API key**
```bash
export ELEVENLABS_API_KEY="your_api_key_here"
```

Make it permanent by adding to your shell profile:
```bash
# For bash
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# For zsh
echo 'export ELEVENLABS_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**Step 4: Verify installation**
```bash
claude
```

Then in Claude:
```
/agents
```

You should see: `red-agent`, `gold-agent`, `blue-agent`, `green-agent`

### Method 2: Direct GitHub Clone

For development or if you want the latest code.

**Step 1: Clone the repository**
```bash
cd ~/Downloads  # or your preferred directory
git clone https://github.com/1Shot-Labs/squadron-comms-plugin.git
```

**Step 2: Launch Claude with the plugin**
```bash
claude --plugin-dir ~/Downloads/squadron-comms-plugin
```

**Step 3: Configure ElevenLabs API key**

Same as Method 1, Step 3.

**Step 4: Verify installation**

Same as Method 1, Step 4.

### Method 3: Local Development

For plugin developers or contributors.

**Step 1: Clone and set up**
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/squadron-comms-plugin.git
cd squadron-comms-plugin

# Make changes...
```

**Step 2: Test locally**
```bash
claude --plugin-dir .
```

**Step 3: Configure API key**

Same as Method 1, Step 3.

## Configuration

### Setting up .claude Directory (Optional)

For team-wide plugin usage, add to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "squadron-comms": {
      "source": {
        "source": "github",
        "repo": "1Shot-Labs/squadron-comms-plugin"
      }
    }
  },
  "enabledPlugins": {
    "squadron-comms@squadron-comms": true
  }
}
```

### Environment Variables

The plugin requires one environment variable:

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `ELEVENLABS_API_KEY` | Yes | Your ElevenLabs API key | `sk_1234567890abcdef...` |

**Set temporarily (current session only):**
```bash
export ELEVENLABS_API_KEY="your_key_here"
```

**Set permanently:**

Add to your shell profile file:

```bash
# ~/.bashrc (Linux/WSL)
# ~/.zshrc (macOS)
# ~/.profile (generic)

export ELEVENLABS_API_KEY="your_key_here"
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

**Verify it's set:**
```bash
echo $ELEVENLABS_API_KEY
```

### Optional: Configure Audio Output Directory

By default, audio files are stored in:
```
${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio/
```

This is automatically managed by the plugin.

### Optional: Configure Mission Log Location

By default, the mission log is at:
```
${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

You can read it with:
```bash
cat ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

Or view recent broadcasts:
```
/squadron-comms:mission-status
```

## Verification

### Test 1: Check Agents Available

```bash
claude
```

In Claude:
```
/agents
```

Expected output should include:
```
Available agents:
- red-agent (Red Squadron)
- gold-agent (Gold Squadron)
- blue-agent (Blue Squadron)
- green-agent (Green Squadron)
```

### Test 2: Check ElevenLabs Connection

In Claude:
```
Can you list the available ElevenLabs voices?
```

If configured correctly, Claude will use the ElevenLabs MCP server to list voices.

### Test 3: Test Voice Broadcast

In Claude:
```
Please spawn Red Squadron and have them announce "Test broadcast successful"
```

You should:
1. Hear an audio broadcast in Daniel's voice (British)
2. See a log entry in `mission-log.jsonl`

### Test 4: Check Mission Status Command

```
/squadron-comms:mission-status
```

Should display recent broadcasts.

## Troubleshooting Installation

### Issue: "Plugin not found"

**Cause:** Plugin not in the correct directory or marketplace not added.

**Solution:**
```bash
# Verify plugin directory exists
ls -la ~/Downloads/squadron-comms-plugin/.claude-plugin/

# Check plugin.json is present
cat ~/Downloads/squadron-comms-plugin/.claude-plugin/plugin.json

# Try loading with explicit path
claude --plugin-dir ~/Downloads/squadron-comms-plugin
```

### Issue: "ELEVENLABS_API_KEY not set"

**Cause:** Environment variable not configured.

**Solution:**
```bash
# Check if set
echo $ELEVENLABS_API_KEY

# If empty, set it
export ELEVENLABS_API_KEY="your_key_here"

# Verify
echo $ELEVENLABS_API_KEY
```

### Issue: "mpv: command not found"

**Cause:** MPV not installed or not in PATH.

**Solution:**
```bash
# Check if installed
which mpv

# If not found, install (see Prerequisites section)

# macOS
brew install mpv

# Linux
sudo apt install mpv  # Ubuntu/Debian
```

### Issue: "No audio output"

**Cause:** MPV configuration or audio device issues.

**Solution:**
```bash
# Test MPV directly
mpv https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3

# Check audio devices
mpv --audio-device=help

# Try specifying device
mpv --audio-device=alsa/default [audio_file]
```

### Issue: "Rate limit exceeded"

**Cause:** Too many TTS requests to ElevenLabs.

**Solution:**
- Wait 60 seconds before making more broadcasts
- Check your ElevenLabs plan limits
- Consider upgrading your ElevenLabs plan for higher limits

### Issue: "Agent voices not working"

**Cause:** Voice IDs may not be valid for your ElevenLabs account.

**Solution:**
```bash
# In Claude, list available voices
Can you list my ElevenLabs voices?

# Verify the squadron voice IDs are in your account:
# - Daniel (onwK4e9ZLuTAKqWW03F9)
# - Joseph (Zlb1dXrM653N07WRdFW3)
# - Jeremy (bVMeCyTHy58xNoL34h3p)
# - Matilda (XrExE9yKIg1WjnnlVkGX)
# - Bill (pqHfZKP75CvOlQylNhV4)
```

If voices aren't available, you can:
1. Use the voice library in ElevenLabs to add them
2. Or modify the agent files to use different voice IDs from your account

## Updating the Plugin

### GitHub Marketplace Method

```bash
# Update all marketplaces
/plugin marketplace update

# Reinstall plugin
/plugin install squadron-comms
```

### Manual Update (Git Clone)

```bash
cd ~/Downloads/squadron-comms-plugin
git pull origin main
```

Then restart Claude Code.

## Uninstallation

### Remove from Claude Code

```
/plugin uninstall squadron-comms
```

### Remove Marketplace

```
/plugin marketplace remove squadron-comms
```

### Delete Local Files

```bash
rm -rf ~/Downloads/squadron-comms-plugin
```

### Remove Environment Variable

Edit your shell profile (`~/.bashrc`, `~/.zshrc`) and remove the line:
```bash
export ELEVENLABS_API_KEY="..."
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

## Next Steps

After successful installation:

1. Read the [README.md](README.md) for usage examples
2. Check [skills/comms/examples/broadcast-examples.md](skills/comms/examples/broadcast-examples.md) for detailed broadcast patterns
3. Try spawning squadron agents for different tasks
4. Review the [CHANGELOG.md](CHANGELOG.md) for version history

## Getting Help

If you encounter issues not covered here:

- **GitHub Issues**: [Report a bug](https://github.com/1Shot-Labs/squadron-comms-plugin/issues)
- **Discussions**: [Ask questions](https://github.com/1Shot-Labs/squadron-comms-plugin/discussions)
- **Documentation**: [Wiki](https://github.com/1Shot-Labs/squadron-comms-plugin/wiki)

---

**Installation complete? Deploy your squadrons and start coordinating!** 🚀
