---
description: Display recent squadron voice broadcasts from the mission log
---

Read and display the recent voice broadcasts from the squadron comms mission log.

Show the last 10 broadcasts in a formatted table with:
- Timestamp
- Call Sign
- Squadron
- Message

Use the mission log file at: `${CLAUDE_PLUGIN_ROOT}/skills/comms/mission-log.jsonl`

If the log doesn't exist or is empty, inform the user that no broadcasts have been made yet.

Format the output clearly with proper spacing and make it easy to read.
