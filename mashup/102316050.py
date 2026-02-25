import sys
import shutil
from pathlib import Path
from yt_dlp import YoutubeDL
from pydub import AudioSegment


def usage(prog):
    print('Usage: python <program.py> "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>')
    print(f'Example: python {prog} "Sharry Maan" 20 25 102316050-output.mp3')

def download_audios(query, n, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
    "quiet": True,
    "noplaylist": True,
    "format": "bestaudio/best",
    "outtmpl": str(out_dir / "%(id)s.%(ext)s"),
    "cookiefile": "cookies.txt",
    "js_runtimes": {"node": {"path": r"C:\Program Files\nodejs\node.exe"}},
    "postprocessors": [
        {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
    ],
    "retries": 3,
}

    search = f"ytsearch{n}:{query}"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(search, download=True)

    files = list(out_dir.glob("*.mp3"))
    if not files:
        raise RuntimeError("No MP3 files downloaded. Try changing singer/query.")
    return files


def trim_and_merge(files, duration, output_file):
    merged = AudioSegment.empty()
    duration_ms = duration * 1000

    for file in files:
        audio = AudioSegment.from_file(file)
        merged += audio[:duration_ms]

    merged.export(output_file, format="mp3")


def main():
    if len(sys.argv) != 5:
        usage(Path(sys.argv[0]).name)
        sys.exit(1)

    singer = sys.argv[1].strip()
    num = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4].strip()

    if num <= 10:
        print("Number of videos must be greater than 10")
        sys.exit(1)

    if duration <= 20:
        print("Audio duration must be greater than 20 seconds")
        sys.exit(1)

    if not output.lower().endswith(".mp3"):
        print("OutputFileName must end with .mp3")
        sys.exit(1)

    work_dir = Path("temp")

    if work_dir.exists():
        shutil.rmtree(work_dir, ignore_errors=True)

    work_dir.mkdir()

    try:
        print("Downloading videos...")
        files = download_audios(singer, num, work_dir)

        print("Processing audio...")
        trim_and_merge(files, duration, output)

        print("Mashup created successfully:", output)

    except Exception as e:
        print("Error:", e)

    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


if __name__ == "__main__":
    main()