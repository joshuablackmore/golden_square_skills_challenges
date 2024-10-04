from lib.track import Track

def test_Track():
    track = Track("Track 1","Artist 1")
    assert isinstance(track, Track)
    assert track.title == "Track 1"
    assert track.artist == "Artist 1"
    
    
def test_track_format():
    track = Track("tHunk", "Joshua Blackmore")
    assert track.format() == "tHunk by Joshua Blackmore"