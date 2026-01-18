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

### 2. Python 3.8+

The plugin requires Python for cross-platform file locking.

**Check if Python is installed:**
```bash
python3 --version
# or on Windows:
python --version
```

**Install Python if needed:**
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` or download from python.org
- **Linux**: Usually pre-installed, or `sudo apt install python3` (Ubuntu/Debian)

**Install filelock library:**
```bash
pip install filelock
```

### 3. ElevenLabs API Key

1. Sign up for an ElevenLabs account at [elevenlabs.io](https://elevenlabs.io)
2. Navigate to your profile settings
3. Generate an API key
4. Copy the API key (you'll need it in step 4 of installation)

### 4. MPV Media Player

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

Option 1 - Using Scoop (Recommended):
```powershell
# Install Scoop if not already installed
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Install mpv
scoop install mpv
```

Option 2 - Using Chocolatey:
```powershell
# Run as Administrator
choco install mpv
```

Option 3 - Manual Installation:
1. Download mpv from [mpv.io/installation](https://mpv.io/installation/)
2. Extract to `C:\Program Files\mpv`
3. Add to PATH via System Properties → Environment Variables
4. Add new System variable Path entry: `C:\Program Files\mpv`

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
/plugin marketplace add 1Shot-Labs/marketplace
```

**Step 2: Install the plugin**
```
/plugin install squadron-comms
```

**Step 3: Install Python dependencies**
```bash
pip install filelock
```

Or install from the plugin's requirements file:
```bash
pip install -r ~/.claude/plugins/squadron-comms/requirements.txt
```

**Step 4: Configure ElevenLabs API key**

**macOS / Linux:**
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

**Windows:**

PowerShell (temporary):
```powershell
$env:ELEVENLABS_API_KEY="your_api_key_here"
```

PowerShell (permanent):
```powershell
[System.Environment]::SetEnvironmentVariable('ELEVENLABS_API_KEY', 'your_api_key_here', 'User')
# Restart Claude Code for changes to take effect
```

Or set via GUI:
1. Start Menu → Search "Environment Variables"
2. "Edit environment variables for your account"
3. New → Variable name: `ELEVENLABS_API_KEY`
4. Variable value: your API key
5. Click OK
6. Restart Claude Code

**Step 5: Verify installation**

**Important:** Restart Claude Code after installing the plugin for agents to load.

```bash
# Exit Claude Code if running (Ctrl+D or type 'exit')
# Then start it again
claude
```

Run the setup verification command:
```
/squadron-comms:verify-setup
```

This comprehensive check will verify:
- ELEVENLABS_API_KEY is set
- MPV is installed and working
- Python and filelock are available
- ElevenLabs API connection works
- Squadron voice profiles are accessible
- File permissions are correct

Then check agents are loaded:
```
/agents
```

You should see: `red-agent`, `gold-agent`, `blue-agent`, `green-agent`

> **Note:** Agents are loaded at session start. If you installed the plugin while Claude Code was running, you must restart for the agents to appear.

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
    "1shot": {
      "source": {
        "source": "github",
        "repo": "1Shot-Labs/marketplace"
      }
    }
  },
  "enabledPlugins": {
    "squadron-comms@1shot": true
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

### Issue: "Agents not showing up after installation"

**Cause:** Agents are loaded at session start and not dynamically loaded when plugins are installed.

**Solution:**
```bash
# Exit Claude Code completely
# Press Ctrl+D or type 'exit'

# Start Claude Code again
claude

# Check agents
/agents
```

You should now see all four squadron agents: `red-agent`, `gold-agent`, `blue-agent`, `green-agent`

**Important:** Always restart Claude Code after installing or updating plugins that include agents.

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
/plugin marketplace remove 1shot
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
