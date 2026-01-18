# Voice Broadcast Examples

This document shows practical examples of using the comms skill for voice broadcasting.

## Basic Examples

### Example 1: Red Squadron Mission Start

**Scenario:** Starting a code analysis task

**Message:**
```
Red Leader here. Beginning code analysis of authentication module.
```

**Implementation:**
```
1. Generate TTS:
   mcp__elevenlabs__text_to_speech(
     text="Red Leader here. Beginning code analysis of authentication module.",
     voice_id="onwK4e9ZLuTAKqWW03F9",
     speed=1.1
   )

2. Play & Log:
   flock ${CLAUDE_PLUGIN_ROOT}/skills/comms/.audio.lock \
     mpv --no-video --really-quiet /path/to/audio.mp3 && \
     echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%S.000Z)'","callSign":"Red Leader","squadron":"red","message":"Red Leader here. Beginning code analysis of authentication module."}' >> \
     ${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl
```

### Example 2: Gold Squadron Progress Update

**Scenario:** Reporting findings during analysis

**Message:**
```
Gold Leader reporting. Discovered critical dependency on legacy API in authentication module.
```

**Implementation:**
```
1. Generate TTS:
   mcp__elevenlabs__text_to_speech(
     text="Gold Leader reporting. Discovered critical dependency on legacy API in authentication module.",
     voice_id="Zlb1dXrM653N07WRdFW3",
     speed=1.1
   )

2. Play & Log:
   [Same pattern as Example 1, using Gold's voice ID and call sign]
```

### Example 3: Blue Squadron Completion

**Scenario:** Completing a performance optimization

**Message:**
```
Blue Leader. Optimization complete. Achieved 65% reduction in bundle size.
```

**Implementation:**
```
1. Generate TTS:
   mcp__elevenlabs__text_to_speech(
     text="Blue Leader. Optimization complete. Achieved 65 percent reduction in bundle size.",
     voice_id="bVMeCyTHy58xNoL34h3p",
     speed=1.1
   )

2. Play & Log:
   [Same pattern, using Blue's voice ID and call sign]
```

### Example 4: Green Squadron Alert

**Scenario:** Identifying accessibility issues

**Message:**
```
Green Leader. Identified 12 accessibility issues. Beginning remediation.
```

**Implementation:**
```
1. Generate TTS:
   mcp__elevenlabs__text_to_speech(
     text="Green Leader. Identified 12 accessibility issues. Beginning remediation.",
     voice_id="XrExE9yKIg1WjnnlVkGX",
     speed=1.1
   )

2. Play & Log:
   [Same pattern, using Green's voice ID and call sign]
```

## Advanced Examples

### Example 5: Multi-Squadron Coordination

**Scenario:** Gold Squadron alerts Blue Squadron about performance issues

**Gold Leader Broadcast:**
```
Gold Leader to Blue Leader. Security analysis reveals performance impact from encryption overhead.
```

**Blue Leader Response:**
```
Blue Leader acknowledging. Will optimize encryption performance.
```

### Example 6: Commander Broadcast

**Scenario:** Commander coordinating multiple squadrons

**Message:**
```
Commander here. Deploying Red and Gold squadrons for parallel analysis. Blue and Green on standby.
```

**Implementation:**
```
1. Generate TTS:
   mcp__elevenlabs__text_to_speech(
     text="Commander here. Deploying Red and Gold squadrons for parallel analysis. Blue and Green on standby.",
     voice_id="pqHfZKP75CvOlQylNhV4",
     speed=1.2
   )

2. Play & Log:
   [Same pattern, using Commander's voice ID and call sign]
```

### Example 7: Detailed Progress Report

**Scenario:** Red Squadron providing detailed findings

**Message:**
```
Red Leader reporting. Analyzed 47 functions. Found 3 potential race conditions in session handling.
```

### Example 8: Urgent Alert

**Scenario:** Blue Squadron discovers critical issue

**Message:**
```
Blue Leader. Critical: Memory leak detected in user session handler. Requires immediate attention.
```

## Message Patterns

### Mission Lifecycle

**Start:**
```
[Call Sign] here. [Brief mission description]
```

**Progress:**
```
[Call Sign] reporting. [Progress update with specifics]
```

**Complete:**
```
[Call Sign]. Mission complete. [Summary of results]
```

**Issue:**
```
[Call Sign]. [Issue description and severity]
```

### Coordination

**Request:**
```
[Call Sign] to [Other Squadron]. [Request or information]
```

**Acknowledgment:**
```
[Call Sign] acknowledging. [Response or action]
```

**Handoff:**
```
[Call Sign] to [Other Squadron]. [Handoff details]. Standing by.
```

## Tips for Effective Broadcasting

1. **Be Specific**: Include numbers, metrics, and concrete details
   - Good: "Found 3 race conditions"
   - Poor: "Found some issues"

2. **Use Professional Tone**: Military-style brevity and clarity
   - Good: "Red Leader. Mission complete."
   - Poor: "Hey, I finished the thing."

3. **Include Context**: Make broadcasts understandable standalone
   - Good: "Blue Leader reporting. Reduced database query time from 450ms to 80ms."
   - Poor: "It's faster now."

4. **Coordinate Properly**: Reference other squadrons when relevant
   - Good: "Gold Leader to Blue Leader. Analysis complete."
   - Poor: "Sending you the results."

5. **Appropriate Frequency**: Broadcast at milestones, not continuously
   - Good: Start, major milestones, completion
   - Poor: Every tiny step

## Common Mistakes to Avoid

❌ **Too Verbose**
```
Red Leader here. I'm starting to analyze the authentication module. This will involve reading multiple files and understanding the flow...
```

✅ **Concise**
```
Red Leader here. Beginning authentication module analysis.
```

---

❌ **No Call Sign**
```
Starting the analysis now.
```

✅ **With Call Sign**
```
Red Leader here. Beginning analysis.
```

---

❌ **Vague Information**
```
Blue Leader. Made it better.
```

✅ **Specific Metrics**
```
Blue Leader. Reduced load time from 3.2 seconds to 1.1 seconds.
```

---

❌ **Breaking Character**
```
Red Leader here lol just finished analyzing the code!!!
```

✅ **Professional Tone**
```
Red Leader. Analysis complete. Results ready for review.
```
