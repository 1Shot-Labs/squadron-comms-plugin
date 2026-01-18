# Deployment Guide

Instructions for pushing the plugin to GitHub and creating releases.

## Prerequisites

- Git configured with your GitHub credentials
- GitHub repository created at: https://github.com/1shot-labs/squadron-comms-plugin

## Initial Push to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com/1shot-labs
2. Click "New repository"
3. Name: `squadron-comms-plugin`
4. Description: "Voice communication system with ElevenLabs TTS for multi-agent coordination in Claude Code"
5. Choose "Public"
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Step 2: Push to GitHub

```bash
cd /home/charles/projects/squadron-comms-plugin

# Push main branch
git push -u origin main

# Push tags
git push origin --tags
```

Expected output:
```
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 8 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), XX.XX KiB | XX.XX MiB/s, done.
Total 20 (delta X), reused 0 (delta 0), pack-reused 0
To https://github.com/1shot-labs/squadron-comms-plugin.git
 * [new branch]      main -> main
 * [new tag]         v1.0.0 -> v1.0.0
```

### Step 3: Verify on GitHub

Visit https://github.com/1shot-labs/squadron-comms-plugin and verify:
- All files are present
- README displays correctly
- Badges show up
- Tag v1.0.0 is visible in releases

## Creating a Release

### Step 1: Navigate to Releases

1. Go to https://github.com/1shot-labs/squadron-comms-plugin
2. Click "Releases" in the right sidebar
3. Click "Draft a new release"

### Step 2: Release Information

**Choose a tag:** Select `v1.0.0` from dropdown

**Release title:** `v1.0.0 - Initial Release`

**Description:**
```markdown
# Squadron Comms Plugin v1.0.0

Initial release of the Squadron Comms Plugin for Claude Code! 🚀

## What's New

Voice communication system with ElevenLabs TTS for multi-agent coordination.

### Features

- **Four Specialized Squadron Agents**
  - Red Squadron (General Purpose) - Daniel voice
  - Gold Squadron (Analysis & Research) - Joseph voice
  - Blue Squadron (Performance & Optimization) - Jeremy voice
  - Green Squadron (Polish & UX) - Matilda voice

- **Voice Broadcasting** - Real-time TTS announcements using ElevenLabs
- **Mission Logging** - All broadcasts logged to JSONL format
- **Concurrent Safe** - File locking prevents audio overlap
- **Color-Coded Squadrons** - Visual identification in Claude Code
- **Commander Role** - Main agent coordination capabilities

## Installation

```bash
# Add the marketplace
/plugin marketplace add 1shot-labs/squadron-comms-plugin

# Install the plugin
/plugin install squadron-comms
```

See [INSTALL.md](https://github.com/1shot-labs/squadron-comms-plugin/blob/main/INSTALL.md) for detailed installation instructions.

## Quick Start

See [QUICKSTART.md](https://github.com/1shot-labs/squadron-comms-plugin/blob/main/QUICKSTART.md) for a 5-minute setup guide.

## Documentation

- [README.md](https://github.com/1shot-labs/squadron-comms-plugin/blob/main/README.md) - Complete usage guide
- [SKILL.md](https://github.com/1shot-labs/squadron-comms-plugin/blob/main/skills/comms/SKILL.md) - Comms skill documentation
- [Examples](https://github.com/1shot-labs/squadron-comms-plugin/blob/main/skills/comms/examples/broadcast-examples.md) - Broadcast examples

## Requirements

- Claude Code CLI
- ElevenLabs API key
- MPV media player

---

**Full Changelog**: https://github.com/1shot-labs/squadron-comms-plugin/blob/main/CHANGELOG.md
```

**Check:** ✅ Set as the latest release

**Click:** "Publish release"

## Post-Release Checklist

After publishing the release:

- [ ] Verify release appears on GitHub
- [ ] Test installation from marketplace
- [ ] Share in Claude Code community
- [ ] Update any documentation links if needed

## Future Releases

For subsequent releases:

### 1. Make Changes

```bash
cd /home/charles/projects/squadron-comms-plugin

# Make your changes...
git add .
git commit -m "feat: add new feature"
```

### 2. Update Version

Update version number in:
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `CHANGELOG.md`
- README.md badges

### 3. Create Tag

```bash
# For feature releases (1.1.0, 1.2.0)
git tag -a v1.1.0 -m "Release v1.1.0 - Description"

# For patches (1.0.1, 1.0.2)
git tag -a v1.0.1 -m "Release v1.0.1 - Bug fixes"
```

### 4. Push

```bash
git push origin main
git push origin --tags
```

### 5. Create GitHub Release

Follow the same process as above with updated version and changelog.

## Troubleshooting Deployment

### Authentication Issues

```bash
# If push fails due to authentication
gh auth login

# Or use personal access token
git remote set-url origin https://YOUR_TOKEN@github.com/1shot-labs/squadron-comms-plugin.git
```

### Tag Already Exists

```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin :refs/tags/v1.0.0

# Recreate tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### Force Push (Use with Caution)

```bash
# Only if absolutely necessary
git push -f origin main
```

## Distribution Verification

After deployment, verify users can install:

```bash
# In a clean Claude Code session
/plugin marketplace add 1shot-labs/squadron-comms-plugin
/plugin install squadron-comms
/agents
```

Should show: red-agent, gold-agent, blue-agent, green-agent

---

**Ready to deploy!** 🚀
