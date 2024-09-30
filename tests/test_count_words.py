from lib.count_words import *


def test_count_words_return_num():
    result = count_words("there are seven words in this string")
    assert result == 7



import pytest
def test_count_words_str_input():
    with pytest.raises(TypeError):
        count_words(123)
    with pytest.raises(TypeError):
        count_words(['joshua','blackmore'])