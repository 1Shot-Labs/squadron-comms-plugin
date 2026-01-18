# Release Checklist for Squadron Comms Plugin v1.0.0

Complete checklist to ensure the plugin is ready for public release.

## ✅ Pre-Release Verification

### Repository Setup
- [x] Git repository initialized
- [x] Main branch created
- [x] Remote origin configured: https://github.com/1Shot-Labs/squadron-comms-plugin.git
- [x] Initial commit created
- [x] Version tag v1.0.0 created
- [x] All files added and committed

### Code Quality
- [x] All JSON files are valid
- [x] Plugin manifest (plugin.json) complete
- [x] Marketplace manifest (marketplace.json) complete
- [x] MCP server configuration (.mcp.json) correct
- [x] All agent definitions complete
- [x] Comms skill documented
- [x] Commands defined
- [x] Scripts have executable permissions

### Documentation
- [x] README.md comprehensive with badges
- [x] QUICKSTART.md for 5-minute setup
- [x] INSTALL.md with detailed installation
- [x] CONTRIBUTING.md for contributors
- [x] CHANGELOG.md with version history
- [x] LICENSE file (MIT)
- [x] DEPLOYMENT.md with push instructions
- [x] Skill documentation complete
- [x] Broadcast examples provided

### Project Structure
- [x] .claude-plugin/ directory with manifests
- [x] agents/ directory with all 4 squadron agents
- [x] skills/comms/ with SKILL.md and examples
- [x] commands/ with mission-status command
- [x] .github/workflows/ with CI validation
- [x] .gitignore configured
- [x] .env.example template provided

### Branding
- [x] All references updated to "1Shot-Labs" (not "1-shot-labs")
- [x] Consistent organization name throughout
- [x] GitHub URLs correct
- [x] Email addresses correct
- [x] Version badges in README

## 🚀 GitHub Deployment Steps

### 1. Create GitHub Repository

**Go to:** https://github.com/1Shot-Labs

1. Click "New repository"
2. Repository name: `squadron-comms-plugin`
3. Description: "Voice communication system with ElevenLabs TTS for multi-agent coordination in Claude Code"
4. Visibility: **Public**
5. **DO NOT** initialize with README, .gitignore, or license
6. Click "Create repository"

### 2. Push to GitHub

```bash
cd /home/charles/projects/squadron-comms-plugin

# Push main branch
git push -u origin main

# Push tags
git push origin --tags
```

Expected: Both main branch and v1.0.0 tag pushed successfully

### 3. Create GitHub Release

1. Go to: https://github.com/1Shot-Labs/squadron-comms-plugin/releases
2. Click "Draft a new release"
3. Choose tag: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Copy description from DEPLOYMENT.md
6. Check "Set as the latest release"
7. Click "Publish release"

### 4. Verify Repository

- [ ] Visit https://github.com/1Shot-Labs/squadron-comms-plugin
- [ ] Verify README displays with badges
- [ ] Check all files are present
- [ ] Verify tag and release are visible
- [ ] Test Actions workflow passes

## 📦 Plugin Distribution

### Test Installation

From a clean Claude Code session:

```bash
# Add marketplace
/plugin marketplace add 1Shot-Labs/squadron-comms-plugin

# Install plugin
/plugin install squadron-comms

# Verify agents available
/agents
```

Expected output should include:
- red-agent
- gold-agent
- blue-agent
- green-agent

### Test Voice Broadcast

With `ELEVENLABS_API_KEY` set:

```bash
export ELEVENLABS_API_KEY="your_key_here"
claude
```

Then in Claude:
```
Spawn Red Squadron and have them announce "Test successful"
```

Should hear audio broadcast in Daniel's British voice.

## 📢 Announcement

### Update Project README

Add installation instructions to main project documentation if needed.

### Share with Community

Consider sharing in:
- Claude Code community channels
- GitHub discussions
- Social media (Twitter, LinkedIn)
- Developer forums

### Example Announcement

```
🚀 Just released Squadron Comms Plugin v1.0.0!

Voice communication system for Claude Code with:
• 4 specialized squadron agents with unique voices
• Real-time TTS broadcasts using ElevenLabs
• Mission logging and coordination
• Multi-agent parallel operations

Install: /plugin marketplace add 1Shot-Labs/squadron-comms-plugin

https://github.com/1Shot-Labs/squadron-comms-plugin
```

## 🔍 Post-Release Verification

- [ ] Plugin installs successfully from GitHub marketplace
- [ ] All agents load correctly
- [ ] Voice broadcasts work
- [ ] Mission logging functions
- [ ] Commands execute properly
- [ ] Documentation links work
- [ ] CI workflow passes

## 🐛 Issue Tracking

- [ ] Enable GitHub Issues
- [ ] Enable GitHub Discussions
- [ ] Create issue templates (bug, feature request)
- [ ] Set up project board (optional)

## 📈 Monitoring

Track:
- GitHub stars and forks
- Installation metrics (if available)
- Issues and bug reports
- Feature requests
- Community feedback

## 🎯 Next Steps

After successful release:

1. Monitor for issues in first 24-48 hours
2. Respond to community feedback
3. Plan v1.1.0 features based on usage
4. Consider additional squadron types
5. Explore integration with other tools

---

## Quick Command Reference

```bash
# Navigate to plugin directory
cd /home/charles/projects/squadron-comms-plugin

# Check status
git status

# View commit history
git log --oneline

# Push to GitHub
git push origin main
git push origin --tags

# Create new release
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0
```

---

**Everything is ready for release!** 🎉

Just follow the GitHub Deployment Steps section to push to GitHub and create the release.
