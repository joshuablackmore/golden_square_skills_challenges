from lib.class_challenge import *

def test_check_with_capital_and_punctuation_returns_True():
    grammer_instance = GrammarStats()
    
    result = grammer_instance.check("Joshua loves to play drums.")
    
    assert result == True
    

def test_check_with_capitol_and_no_punctuation_returns_false():
    
    grammer_instance = GrammarStats()
    
    result = grammer_instance.check("Joshua loves to play the drums")
    
    assert result == False
    
    
    
def test_percentage_good_returns_50_with_2good_and_2bad_texts():
    
    grammer_instance = GrammarStats()

    grammer_instance.check("This is a good sentence.")
    grammer_instance.check("This is another good sentence.")
    grammer_instance.check("this is a bad sentence.")
    grammer_instance.check("this is another bad sentence")
    
    
    result = grammer_instance.percentage_good()
    
    assert result == 50
    
def test_percentage_good_returns_75_with_3good_and_1bad():
    grammer_instance = GrammarStats()
    grammer_instance.check("This is a good sentence.")
    grammer_instance.check("This is another good sentence.")
    grammer_instance.check("This is our third good sentence.")
    grammer_instance.check("this is our bad sentence")
    
    result = grammer_instance.percentage_good()
    
    assert result == 75