# main.py
from automated_media_manager import config
from automated_media_manager.torrent.torrent_manager import TorrentManager

def main():
    """
    The Main Function for the Program
    """

    config = Config()
    torrent_manager = TorrentManager(config)
    # Add more logic here
    print("Automated Media Manager started")

if __name__ == "__main__":
   main()
