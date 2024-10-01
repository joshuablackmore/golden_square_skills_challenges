from lib.design_recipes import *

def test_reading_time_200_words():
    result = reading_time(200)
    assert result == '1.0 minutes'
    
def test_reading_time_100_words():
    result = reading_time(100)
    assert result == '0.5 minutes'
    
    
def test_verify_grammar_True():
    result = verify_grammar('Hello there.')
    assert result == True
    
    
    
def test_verify_grammar_False():
    result = verify_grammar("Hello there")
    assert result == False