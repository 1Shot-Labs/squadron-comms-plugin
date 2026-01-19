#!/bin/bash
# Squadron Comms Broadcast Helper Script
# Usage: ./broadcast.sh <squadron> <message>
# Example: ./broadcast.sh red "Red Leader here. Mission starting."

set -e

# Get the plugin root directory
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
COMMS_DIR="${PLUGIN_ROOT}/skills/comms"
AUDIO_DIR="${COMMS_DIR}/.audio"
LOCK_FILE="${COMMS_DIR}/.audio.lock"
LOG_FILE="${COMMS_DIR}/mission-log.jsonl"

# Create directories if they don't exist
mkdir -p "${AUDIO_DIR}"

# Squadron voice configurations
declare -A VOICE_IDS=(
    ["commander"]="pqHfZKP75CvOlQylNhV4"
    ["red"]="onwK4e9ZLuTAKqWW03F9"
    ["gold"]="Zlb1dXrM653N07WRdFW3"
    ["blue"]="bVMeCyTHy58xNoL34h3p"
    ["green"]="XrExE9yKIg1WjnnlVkGX"
)

declare -A CALL_SIGNS=(
    ["commander"]="Commander"
    ["red"]="Red Leader"
    ["gold"]="Gold Leader"
    ["blue"]="Blue Leader"
    ["green"]="Green Leader"
)

declare -A SPEEDS=(
    ["commander"]="1.2"
    ["red"]="1.2"
    ["gold"]="1.2"
    ["blue"]="1.2"
    ["green"]="1.2"
)

# Validate arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <squadron> <message>"
    echo "Squadrons: commander, red, gold, blue, green"
    exit 1
fi

SQUADRON="$1"
MESSAGE="$2"

# Validate squadron
if [ -z "${VOICE_IDS[$SQUADRON]}" ]; then
    echo "Error: Invalid squadron '$SQUADRON'"
    echo "Valid squadrons: commander, red, gold, blue, green"
    exit 1
fi

VOICE_ID="${VOICE_IDS[$SQUADRON]}"
CALL_SIGN="${CALL_SIGNS[$SQUADRON]}"
SPEED="${SPEEDS[$SQUADRON]}"

# Generate timestamp
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%S.000Z)

# Output file
AUDIO_FILE="${AUDIO_DIR}/${SQUADRON}_${TIMESTAMP//[:.]/_}.mp3"

echo "Broadcasting as ${CALL_SIGN}..."
echo "Message: ${MESSAGE}"

# Note: This script demonstrates the concept
# In actual use, Claude would call the ElevenLabs MCP tool directly
# This is a helper for understanding the flow

# Log the broadcast
LOG_ENTRY=$(cat <<EOF
{"timestamp":"${TIMESTAMP}","callSign":"${CALL_SIGN}","squadron":"${SQUADRON}","message":"${MESSAGE}"}
EOF
)

echo "${LOG_ENTRY}" >> "${LOG_FILE}"

echo "Broadcast logged to mission-log.jsonl"
