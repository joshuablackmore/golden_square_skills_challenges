# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def reading_Time(wordsInt):
no side effects
return {time}minutes


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

def test_reading_time_200_words():
    result = reading_time(200)
    assert result == '1.0 minutes'
    
def test_reading_time_100_words():
    result = reading_time(100)
    assert result == '0.5 minutes'
    
    

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:


Ensure all test function names are unique, otherwise pytest will ignore them!
