#!/bin/bash
# Simple mission log appender for Squadron Comms
# Usage: ./log_broadcast.sh <call_sign> <squadron> <message>

set -e

CALL_SIGN="$1"
SQUADRON="$2"
MESSAGE="$3"

# Get plugin root
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
LOG_FILE="${PLUGIN_ROOT}/skills/comms/mission-log.jsonl"

# Create log file parent directory if needed
mkdir -p "$(dirname "$LOG_FILE")"

# Generate timestamp (ISO 8601 UTC)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows (Git Bash or similar)
    TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.000Z)
else
    # Unix (macOS, Linux)
    TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%S.000Z)
fi

# Append to mission log
echo "{\"timestamp\":\"$TIMESTAMP\",\"callSign\":\"$CALL_SIGN\",\"squadron\":\"$SQUADRON\",\"message\":\"$MESSAGE\"}" >> "$LOG_FILE"
