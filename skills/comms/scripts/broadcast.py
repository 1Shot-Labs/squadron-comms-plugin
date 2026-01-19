#!/usr/bin/env python3
"""
Self-locating broadcast wrapper for Squadron Comms Plugin.
Handles playback and logging with automatic path resolution.

Usage: python broadcast.py <audio_file_path> <call_sign> <squadron> <message>

Example:
  python broadcast.py /tmp/audio.mp3 "Red Leader" red "Mission starting"

This script automatically:
1. Locates itself and derives plugin paths (no env vars needed)
2. Plays audio with file locking (prevents overlap)
3. Logs broadcast to mission-log.jsonl

Agents should:
1. Generate TTS with mcp__elevenlabs__text_to_speech
2. Call this script with the returned audio file path
"""
import sys
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone


# Self-locate: derive all paths from script location
SCRIPT_DIR = Path(__file__).parent.resolve()
COMMS_DIR = SCRIPT_DIR.parent
AUDIO_DIR = COMMS_DIR / ".audio"
LOG_FILE = COMMS_DIR / "mission-log.jsonl"
PLAY_SCRIPT = SCRIPT_DIR / "play_with_lock.py"

# Ensure directories exist
AUDIO_DIR.mkdir(exist_ok=True)




def play_audio_with_lock(audio_file):
    """Play audio using the file-locked playback script."""
    if not audio_file.exists():
        print(f"[ERROR] Audio file not found: {audio_file}", file=sys.stderr)
        return False

    try:
        # Use the self-located play_with_lock.py script
        result = subprocess.run(
            [sys.executable, str(PLAY_SCRIPT), str(audio_file)],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"[PLAY] Audio played successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to play audio: {e.stderr}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"[ERROR] Unexpected error during playback: {e}", file=sys.stderr)
        return False


def log_broadcast(call_sign, squadron, message):
    """Log broadcast to mission-log.jsonl."""
    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    log_entry = {
        "timestamp": timestamp,
        "callSign": call_sign,
        "squadron": squadron,
        "message": message
    }

    try:
        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        print(f"[LOG] Broadcast logged to mission-log.jsonl")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to log broadcast: {e}", file=sys.stderr)
        return False


def broadcast(audio_file_path, call_sign, squadron, message):
    """
    Complete broadcast process: Audio playback → Mission logging.

    Args:
        audio_file_path: Path to pre-generated TTS audio file
        call_sign: Agent's call sign (e.g., "Red Leader")
        squadron: Squadron name (e.g., "red")
        message: The message that was spoken

    Returns:
        bool: True if successful, False otherwise
    """
    audio_file = Path(audio_file_path)

    print(f"\n{'='*70}")
    print(f"Squadron Comms Broadcast")
    print(f"{'='*70}")
    print(f"Squadron:  {squadron}")
    print(f"Call Sign: {call_sign}")
    print(f"Message:   {message}")
    print(f"Audio:     {audio_file}")
    print(f"{'='*70}\n")

    # Step 1: Play audio with locking
    print("[STEP 1/2] Playing audio with file locking...")
    if not play_audio_with_lock(audio_file):
        print("[FAILED] Broadcast aborted - audio playback failed", file=sys.stderr)
        return False

    # Step 2: Log to mission log
    print("[STEP 2/2] Logging broadcast...")
    if not log_broadcast(call_sign, squadron, message):
        print("[WARNING] Broadcast completed but logging failed", file=sys.stderr)
        # Don't fail the whole broadcast if logging fails

    print(f"\n[SUCCESS] Broadcast completed successfully")
    print(f"{'='*70}\n")

    return True


def main():
    """Main entry point."""
    if len(sys.argv) < 5:
        print("Usage: python broadcast.py <audio_file_path> <call_sign> <squadron> <message>", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print('  python broadcast.py /tmp/audio.mp3 "Red Leader" red "Mission starting"', file=sys.stderr)
        print("\nNote: Generate TTS audio first with mcp__elevenlabs__text_to_speech", file=sys.stderr)
        sys.exit(1)

    audio_file_path = sys.argv[1]
    call_sign = sys.argv[2]
    squadron = sys.argv[3]
    message = sys.argv[4]

    # Validate audio file exists
    if not Path(audio_file_path).exists():
        print(f"Error: Audio file not found: {audio_file_path}", file=sys.stderr)
        sys.exit(1)

    # Validate squadron
    valid_squadrons = ['red', 'gold', 'blue', 'green', 'commander']
    if squadron.lower() not in valid_squadrons:
        print(f"Error: Invalid squadron '{squadron}'", file=sys.stderr)
        print(f"Valid squadrons: {', '.join(valid_squadrons)}", file=sys.stderr)
        sys.exit(1)

    # Execute broadcast
    success = broadcast(audio_file_path, call_sign, squadron, message)

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
