# Contributing to Squadron Comms Plugin

Thank you for your interest in contributing to Squadron Comms Plugin! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/1shot-labs/squadron-comms-plugin/issues)
2. If not, create a new issue with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (OS, Claude Code version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Check [Discussions](https://github.com/1shot-labs/squadron-comms-plugin/discussions) for similar ideas
2. Create a new discussion with:
   - Clear description of the feature
   - Use case and benefits
   - Potential implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/squadron-comms-plugin.git
   cd squadron-comms-plugin
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow the coding standards (see below)
   - Test your changes thoroughly
   - Update documentation if needed

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

   Use conventional commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for test additions
   - `chore:` for maintenance tasks

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with:
     - Description of changes
     - Related issue numbers
     - Testing performed
     - Screenshots (if applicable)

## Development Setup

### Prerequisites

- Claude Code CLI
- ElevenLabs API key
- MPV media player
- Git

### Local Development

1. **Clone and setup**
   ```bash
   git clone https://github.com/YOUR_USERNAME/squadron-comms-plugin.git
   cd squadron-comms-plugin
   ```

2. **Set up environment**
   ```bash
   export ELEVENLABS_API_KEY="your_key_here"
   ```

3. **Test the plugin**
   ```bash
   claude --plugin-dir .
   ```

4. **Make changes**
   - Edit agent files in `agents/`
   - Update skill in `skills/comms/`
   - Modify commands in `commands/`

5. **Test changes**
   ```bash
   # Restart Claude with plugin
   claude --plugin-dir .

   # Test in Claude:
   /agents  # Verify agents load
   /squadron-comms:mission-status  # Test commands
   ```

## Project Structure

```
squadron-comms-plugin/
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest - edit version here
│   └── marketplace.json     # Marketplace config
├── agents/                  # Agent definitions
│   ├── red-agent.md        # Each agent has a .md file
│   ├── gold-agent.md
│   ├── blue-agent.md
│   └── green-agent.md
├── skills/                  # Skills
│   └── comms/
│       ├── SKILL.md        # Main skill documentation
│       ├── scripts/        # Helper scripts
│       └── examples/       # Usage examples
├── commands/                # Slash commands
│   └── mission-status.md
└── [documentation files]
```

## Coding Standards

### Agent Files

- Use frontmatter for metadata
- Include `name`, `description`, `color`, `model`
- Provide clear examples in description
- Use consistent voice profile format
- Keep agent personas professional and on-brand

**Example:**
```markdown
---
name: my-agent
description: |
  Description of when to use this agent.

  Examples:

  <example>
  user: "Do something"
  assistant: "I'll use my-agent"
  </example>

color: red
model: sonnet
---

# Agent Name

Your agent instructions here...
```

### Skill Files

- Use frontmatter with `name`, `description`, `version`
- Provide comprehensive documentation
- Include usage examples
- Document all parameters and options

### Commands

- Use frontmatter with `description`
- Keep command logic clear and focused
- Document expected behavior

### Documentation

- Use clear, concise language
- Provide examples for all features
- Keep README.md up to date
- Update CHANGELOG.md for all changes

## Testing Guidelines

### Manual Testing Checklist

Before submitting a PR, verify:

- [ ] All squadron agents load correctly
- [ ] Voice broadcasts work for each squadron
- [ ] Mission log updates correctly
- [ ] Commands execute without errors
- [ ] Documentation is accurate
- [ ] No broken links in documentation
- [ ] Examples work as described

### Test Commands

```bash
# In Claude:

# Test agent loading
/agents

# Test mission status command
/squadron-comms:mission-status

# Test voice broadcast
Spawn Red Squadron and have them announce a test message

# Test each squadron
[Test Red, Gold, Blue, Green squadrons individually]

# Test parallel operations
Run two tasks in parallel with different squadrons
```

## Adding New Features

### New Squadron Agent

1. Create new agent file in `agents/`
2. Define voice profile (voice ID, call sign, speed)
3. Update README.md with new squadron info
4. Update voice profiles table in `skills/comms/SKILL.md`
5. Test voice broadcasts

### New Command

1. Create `.md` file in `commands/`
2. Add frontmatter with description
3. Document in README.md
4. Test command execution

### New Skill

1. Create directory in `skills/`
2. Add `SKILL.md` with frontmatter
3. Include examples and documentation
4. Update plugin.json if needed
5. Test skill functionality

## Versioning

We use [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.x.x): Breaking changes
- **MINOR** (x.1.x): New features, backward compatible
- **PATCH** (x.x.1): Bug fixes, backward compatible

Update version in:
1. `.claude-plugin/plugin.json`
2. `.claude-plugin/marketplace.json`
3. `CHANGELOG.md`

## Documentation Updates

When adding features:

1. Update README.md with usage examples
2. Add entry to CHANGELOG.md
3. Update relevant skill documentation
4. Add examples if applicable
5. Update INSTALL.md if setup changes

## Release Process

Maintainers will:

1. Review and merge PR
2. Update version in plugin.json and marketplace.json
3. Update CHANGELOG.md
4. Create GitHub release with tag (e.g., `v1.1.0`)
5. Announce in Discussions

## Questions?

- Open a [Discussion](https://github.com/1shot-labs/squadron-comms-plugin/discussions)
- Ask in your PR
- Check existing [Issues](https://github.com/1shot-labs/squadron-comms-plugin/issues)

## Recognition

Contributors will be:
- Listed in release notes
- Mentioned in CHANGELOG.md
- Acknowledged in README.md (for significant contributions)

Thank you for contributing to Squadron Comms Plugin! 🚀
