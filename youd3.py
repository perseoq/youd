import argparse
import subprocess

def download_mp3(url):
    command = ['yt-dlp', '--extract-audio', '--audio-format', 'mp3', url]
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description='YouTube MP3 Downloader')
    parser.add_argument('url', help='URL del video de YouTube')
    args = parser.parse_args()

    download_mp3(args.url)

if __name__ == '__main__':
    main()
