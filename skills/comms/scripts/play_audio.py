#!/usr/bin/env python3
"""
Cross-platform audio playback with file locking for Squadron Comms.

This script provides atomic audio playback with file locking to prevent
concurrent broadcasts from overlapping. Works on Windows, macOS, and Linux.

Usage:
    python play_audio.py <audio_file> <lock_file> <log_file> <call_sign> <squadron> <message>

Requirements:
    - filelock>=3.20.0
    - mpv installed and in PATH
"""

import sys
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

try:
    from filelock import FileLock
except ImportError:
    print("Error: filelock library not installed", file=sys.stderr)
    print("Install with: pip install filelock", file=sys.stderr)
    sys.exit(1)


def play_audio_with_lock(audio_file: str, lock_file: str, log_file: str,
                         call_sign: str, squadron: str, message: str) -> None:
    """
    Play audio file with file locking and log to mission log.

    Args:
        audio_file: Path to the audio file to play
        lock_file: Path to the lock file for synchronization
        log_file: Path to the mission log JSONL file
        call_sign: Squadron call sign (e.g., "Red Leader")
        squadron: Squadron identifier (e.g., "red")
        message: The broadcast message
    """
    # Convert paths to Path objects
    audio_path = Path(audio_file)
    lock_path = Path(lock_file)
    log_path = Path(log_file)

    # Ensure audio file exists
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_file}", file=sys.stderr)
        sys.exit(1)

    # Create lock file parent directory if needed
    lock_path.parent.mkdir(parents=True, exist_ok=True)

    # Create log file parent directory if needed
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Acquire lock and play audio
    lock = FileLock(str(lock_path), timeout=30)

    try:
        with lock:
            # Play audio with mpv
            result = subprocess.run(
                ["mpv", "--no-video", "--really-quiet", str(audio_path)],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"Warning: mpv exited with code {result.returncode}", file=sys.stderr)
                if result.stderr:
                    print(f"mpv error: {result.stderr}", file=sys.stderr)

            # Log the broadcast
            timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
            log_entry = {
                "timestamp": timestamp,
                "callSign": call_sign,
                "squadron": squadron,
                "message": message
            }

            # Append to mission log
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + '\n')

    except Exception as e:
        print(f"Error during broadcast: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) != 7:
        print("Usage: play_audio.py <audio_file> <lock_file> <log_file> <call_sign> <squadron> <message>",
              file=sys.stderr)
        sys.exit(1)

    audio_file = sys.argv[1]
    lock_file = sys.argv[2]
    log_file = sys.argv[3]
    call_sign = sys.argv[4]
    squadron = sys.argv[5]
    message = sys.argv[6]

    play_audio_with_lock(audio_file, lock_file, log_file, call_sign, squadron, message)


if __name__ == "__main__":
    main()
