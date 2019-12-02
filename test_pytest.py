from hello import YearRangePlaylist

def test_30sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().thirtiesPlaylist() == 30

def test_40sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().fourtiesPlaylist() == 30

def test_50sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().fiftiesPlaylist() == 30

def test_60sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().sixtiesPlaylist() == 30

def test_80sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().eightiesPlaylist() == 30
    
def test_70sPlaylist():
    assert YearRangePlaylist.yearRangePlaylistClass().SeventiesPlaylist() == 30