import pytest
from main import *
class TestPytestMain:
    def setup_method(self):
        self.emp1 = Connect4()
    # Ran perfectly on first test
    def test_sp(self):
        assert self.emp1.current_player == 'P'
        self.emp1.switch_player()
        assert self.emp1.current_player == 'O'
    #1. Error(Used Unittest language)
    #2. Using W3CSCHOOLS and class examples I found the right language to use during testing
    def test_full(self):
        for col in range(self.emp1.COLS):
            for rows in range(self.emp1.ROWS):
                self.emp1.drop_chip(col)
        assert self.emp1.is_full() is True
        #1. Error. I tried flooding a column by hand and it didnt work
        #2. Error. Takes 2 arguements but 1 were given
        #3. Using W3CSCHOOLS and the unittest file I used 'is True' in the same was assertTrue would be used in a unittest file.

