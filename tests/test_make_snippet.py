from lib.make_snippet import *

def test_make_snippet_more_than_five_words():
    result = make_snippet('more than five words will give dots after')
    assert result == "more than five words will give dots after..."
    
    
    
def test_make_snippet_less_than_five_words():
    result = make_snippet('less than five')
    assert result == "less than five"