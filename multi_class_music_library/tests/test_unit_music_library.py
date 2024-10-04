from lib.music_library import MusicLibrary

def test_music_library():
    library = MusicLibrary()
    assert isinstance(library, MusicLibrary)
    assert library._tracks == []
    