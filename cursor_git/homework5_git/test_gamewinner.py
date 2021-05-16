import unittest
from unittest.mock import patch
from game import TicTacToe, play


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.games = TicTacToe()
        self.games.board = ['O', 'O', 'X', 'O', 'X', ' ', 'X', ' ', 'X']

    def test_winner(self):
        self.assertTrue(self.games.winner(6, 'X') == True)

    # It`s to easy
    #  ^
    # /|\
    # Check function play()
    def get_move(game):
        return 6

    @patch('game.HumanPlayer', get_move=get_move)
    @patch('game.GeniusComputerPlayer', get_move=get_move)
    def test_play(self, CompMock, HumMock):
        self.games.board = ['O', 'O', 'X', 'O', 'X', ' ', ' ', ' ', 'X']
        playerx = HumMock
        playero = CompMock
        self.assertTrue(play(self.games, playerx, playero, print_game=False) == 'X')

if __name__ == '__main__':
    unittest.main()
