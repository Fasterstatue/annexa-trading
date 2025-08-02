#!/usr/bin/env python3

"""
Simple command‑line interface to transcribe an audio file using OpenAI's Whisper.

This script loads the "base" Whisper model by default and prints the
transcription to stdout. It assumes the audio file is in a format supported
by Whisper (e.g. WAV, MP3, M4A). You can mount a host directory containing
audio files into the container and run this script on any file inside it.

Usage:
    python transcribe.py path/to/audio.wav

This module is intended to be called by the n8n workflow in future phases.
"""

import argparse
import os

try:
    import whisper  # type: ignore
except ImportError as e:
    raise SystemExit(
        "Whisper library is not installed. Please ensure openai-whisper is in your requirements."
    ) from e


def transcribe_file(audio_path: str) -> str:
    """Transcribe the given audio file and return the transcribed text."""
    # Load the base model. You can switch to 'small', 'medium', etc. for better accuracy at the cost of speed.
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result.get("text", "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper")
    parser.add_argument(
        "file",
        type=str,
        help="Path to the audio file to transcribe",
    )
    args = parser.parse_args()
    audio_path = args.file

    if not os.path.isfile(audio_path):
        raise SystemExit(f"File not found: {audio_path}")

    text = transcribe_file(audio_path)
    print(text)


if __name__ == "__main__":
    main()