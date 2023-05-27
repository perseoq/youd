import argparse
import yt_dlp


def download_playlist(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(playlist_index)s_%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    parser = argparse.ArgumentParser(description='YouTube Playlist Downloader')
    parser.add_argument('url', type=str, help='URL of the YouTube playlist')
    args = parser.parse_args()

    playlist_url = args.url
    download_playlist(playlist_url)


if __name__ == '__main__':
    main()
