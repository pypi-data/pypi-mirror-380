# YT-CHAP

**yt-chap** is a simple CLI tool to fetch and display video chapters from **any URL supported by yt-dlp** in a clean, human-readable format.

---

## 🚀 Features

-   Parses video chapter metadata using `yt-dlp`.
-   Displays output in a clear table format (Start, End, Duration, Title).
-   Gracefully falls back to a single "Full Video" entry if no chapters are found.
-   Checks for `yt-dlp` installation and provides guidance if not found.
-   Lightweight and terminal-friendly.
-   Includes `--version` / `-v` flag for author and version info.

---

## 📦 Installation

1.  **Install `yt-dlp`**:
    `yt-chap` relies on `yt-dlp` to fetch video information. If you don't have it installed, please follow the official installation instructions:
    [yt-dlp Installation Guide](https://github.com/yt-dlp/yt-dlp#installation)

    For example, using `pip`:
    ```bash
    pip install yt-dlp
    ```

2.  **Install `yt-chap`**:
    You can install `yt-chap` from its source directory:
    ```bash
    git clone [https://github.com/mallikmusaddiq1/yt-chap.git](https://github.com/mallikmusaddiq1/yt-chap.git)
    cd yt-chap
    pip install .
    ```

---

## 📄 Usage

Run `yt-chap` followed by the video URL you want to inspect:

```bash
yt-chap <VIDEO_URL>

Example:
yt-chap https://www.youtube.com/watch?v=xyz

Example Output:

No.  | Start      | End        | Duration   | Title
-----|------------|------------|------------|---------------------------------------------
1    | 00:00:00   | 00:00:30   | 00:00:30   | Opening Scene
2    | 00:00:30   | 00:01:15   | 00:00:45   | Main Theme
3    | 00:01:15   | 00:02:00   | 00:00:45   | Bridge
4    | 00:02:00   | 00:03:30   | 00:01:30   | Conclusion

To view version and author info:
yt-chap --version
```

---

🔧 Requirements
 * Python 3.6+
 * yt-dlp (must be installed separately and accessible in your system's PATH)

---

👤 Author
Mallik Mohammad Musaddiq
GitHub: mallikmusaddiq1/yt-chap
Email: mallikmusaddiq1@gmail.com

---

📜 License
MIT License — see [LICENSE](LICENSE) file.