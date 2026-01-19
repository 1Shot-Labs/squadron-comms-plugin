#!/usr/bin/env python3
"""
Cross-platform audio playback with file locking.
Prevents multiple agents from playing audio simultaneously.

Usage: python play_with_lock.py <audio_file>
Example: python play_with_lock.py /path/to/audio.mp3

Dependencies:
- sounddevice: Cross-platform audio playback
- soundfile: Audio file reading
- filelock: Cross-platform file locking
"""
import sys
import os
from pathlib import Path
from filelock import FileLock
import sounddevice as sd
import soundfile as sf


def play_audio_with_lock(audio_file):
    """Play audio file with exclusive file lock to prevent overlapping playback."""

    # Get lock file path (in comms directory)
    script_dir = Path(__file__).parent
    comms_dir = script_dir.parent
    lock_path = comms_dir / ".audio.lock"

    # Create parent directory if needed
    lock_path.parent.mkdir(parents=True, exist_ok=True)

    # Acquire lock and play audio
    with FileLock(str(lock_path), timeout=300):  # Wait up to 5 minutes
        # Read audio file
        data, samplerate = sf.read(audio_file)

        # Play audio (blocking=True waits for playback to complete)
        sd.play(data, samplerate, blocking=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python play_with_lock.py <audio_file>", file=sys.stderr)
        sys.exit(1)

    audio_file = sys.argv[1]

    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found: {audio_file}", file=sys.stderr)
        sys.exit(1)

    try:
        play_audio_with_lock(audio_file)
    except Exception as e:
        print(f"Error playing audio: {e}", file=sys.stderr)
        sys.exit(1)
