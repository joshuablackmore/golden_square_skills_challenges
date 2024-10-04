from lib.music_library import MusicLibrary
from lib.track import Track

def test_music_library_integration():
    library = MusicLibrary()
    track_1 = Track("Front Pocket", "Joshua Blackmore")
    track_2 = Track("Deeper underground", "Jamiriqui")
    library.add(track_1)
    library.add(track_2)
    assert library._tracks == [track_1, track_2]


def test_add_two_tracks_search_for_word_in_track_returns_correct_track():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("ay") == [track_1]
    
def test_track_format_correctly_formats_library_entries():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1.format())
    library.add(track_2)
    assert library._tracks == ['Always The Hard Way by Terror', track_2]