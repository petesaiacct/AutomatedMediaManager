# tests/test_torrent_manager.py
import pytest
from automated_media_manager.torrent.torrent_manager.py import TorrentManager

@pytest.fixture
def torrent_manager():
    return TorrentManager()

def test_add_torrent(torrent_manager):
    test_magnet_link = "magnet:?xt=urn:btih:example"
    result = torrent_manager.add_torrent(test_magnet_link)
    assert isinstance(result, str)
    assert result.startswith("torrent added")

def test_get_torrents(torrent_manager):
    result = torrent_manager.get_torrents()
    assert isinstance(result, list)
