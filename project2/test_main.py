import unittest
from main import *
class TestMain(unittest.TestCase):
    def setUp(self):
        self.emp1 = Connect4()
    def test_Hwins(self):
        self.emp1.board[0][0] = 'P'
        self.emp1.board[0][1] = 'P'
        self.emp1.board[0][2] = 'P'
        self.emp1.board[0][3] = 'P'
        self.assertTrue(self.emp1.check_win('P'))
    def test_Vwins(self):
        self.emp1.board[0][0] = 'P'
        self.emp1.board[1][0] = 'P'
        self.emp1.board[2][0] = 'P'
        self.emp1.board[3][0] = 'P'
        self.assertTrue(self.emp1.check_win('P'))
    def test_Dwins(self):
        self.emp1.board[0][0] = 'P'
        self.emp1.board[1][1] = 'P'
        self.emp1.board[2][2] = 'P'
        self.emp1.board[3][3] = 'P'
        self.assertTrue(self.emp1.check_win('P'))
    def test_N0win(self):
        self.assertFalse(self.emp1.check_win('P'))
        self.assertFalse(self.emp1.check_win('O'))
if __name__ =="__main__":
    unittest.main()