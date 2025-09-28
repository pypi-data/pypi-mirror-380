#!/usr/bin/env python3

import argparse
import subprocess
import json
import sys
import shutil

# Metadata
__version__ = "0.2.0"
__author__ = "Mallik Mohammad Musaddiq"
__email__ = "mallikmusaddiq1@gmail.com"
__github__ = "https://github.com/mallikmusaddiq1/yt-chap"

def seconds_to_hms(seconds: float | None) -> str:
    """Converts seconds to HH:MM:SS.mmm format or 'N/A' if None."""
    if seconds is None:
        return "N/A"
    if seconds < 0:
        seconds = 0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    whole_s = int(s)
    ms = int(round((s - whole_s) * 1000))
    return f"{h:02}:{m:02}:{whole_s:02}.{ms:03}"

def print_chapters(chapters: list, url: str):
    """Prints chapters in a table format."""
    print(f"[info] Chapters from: {url}\n")
    print(f"{'No.':<4} | {'Start':<13} | {'End':<13} | {'Duration':<13} | Title")
    print("-" * 80)

    for i, chap in enumerate(chapters, 1):
        start_time = chap.get("start_time")
        end_time = chap.get("end_time")
        title = chap.get("title", "No Title")
        start = seconds_to_hms(start_time)
        if end_time is None:
            end = "N/A"
            duration = "N/A"
        else:
            end = seconds_to_hms(end_time)
            duration_sec = end_time - (start_time or 0)
            duration = seconds_to_hms(max(duration_sec, 0))
        print(f"{i:<4} | {start:<13} | {end:<13} | {duration:<13} | {title}")

def run_yt_dlp(extra_args: list, url: str):
    """Runs yt-dlp with the given extra args."""
    cmd = ['yt-dlp'] + extra_args + ['--no-warnings']
    try:
        result = subprocess.run(
            cmd + [url],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e}", file=sys.stderr)
        if e.stderr:
            print(f"yt-dlp error:\n{e.stderr.strip()}", file=sys.stderr)
        raise

def main():
    """Main entry point of the script."""
    # Check if yt-dlp is installed
    if not shutil.which('yt-dlp'):
        print("Error: 'yt-dlp' not found.", file=sys.stderr)
        print("Please install yt-dlp to use yt-chap.", file=sys.stderr)
        print("\nInstallation options:")
        print("Install via pip (latest version, may require sudo or --user):")
        print("   pip install yt-dlp")
        print("\nInstall via package manager (stable version):")
        print("   - On Termux           : pkg install python-yt-dlp")
        print("   - On Debian/Ubuntu    : sudo apt install yt-dlp")
        print("   - On Fedora           : sudo dnf install yt-dlp")
        print("   - On Arch Linux       : sudo pacman -S yt-dlp")
        print("   - On macOS (Homebrew) : brew install yt-dlp")
        print("   - On Windows (winget) : winget install yt-dlp")
        print("   - On Windows (scoop)  : scoop install yt-dlp")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="yt-chap - Fetch and display video chapters from any yt-dlp supported URL.",
    )
    parser.add_argument("url", nargs="?", help="Video URL (from any yt-dlp supported site)")
    parser.add_argument("--version", "-v", action="store_true", help="show version and author info")
    args = parser.parse_args()

    if args.version:
        print(f"yt-chap v{__version__}")
        print(f"\nAuthor : {__author__}")
        print(f"Email  : {__email__}")
        print(f"GitHub : {__github__}")
        sys.exit(0)

    if not args.url:
        parser.print_help()
        sys.exit(1)

    url = args.url

    print(f"\n[info] Fetching metadata for {url}...")

    try:
        json_out = run_yt_dlp(['--dump-json'], url)
        lines = json_out.splitlines()
        if len(lines) > 1:
            print("\n[warning] Multiple entries detected (possibly a playlist). Using the first entry.\n", file=sys.stderr)
            info_str = lines[0]
        else:
            info_str = json_out
        info = json.loads(info_str)

        chapters = info.get('chapters') or []
        if not isinstance(chapters, list):
            raise ValueError("Chapters data is not a list.")

        if not chapters:
            duration = info.get('duration')
            if not isinstance(duration, (int, float)) or duration <= 0:
                raise ValueError("Duration unavailable or invalid.")
            print("\n[info] No chapter metadata found.\n\n[info] Using video duration from metadata.\n")
            chapters = [{
                "start_time": 0.0,
                "end_time": duration,
                "title": "Full Video"
            }]

        print_chapters(chapters, url)

    except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError, KeyError) as e:
        print(f"\n[error] Failed to process metadata for '{url}': {e}\n", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[error] An unexpected error occurred: {e}\n", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()