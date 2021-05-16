from game import TicTacToe
game = TicTacToe()
game.board[5]='X'
game.board[3]='O'

def test_available_moves():
    assert 4 in game.available_moves()
    assert 5 not in game.available_moves()

def test_make_move():
    assert game.make_move(4,'X')==True
    assert game.make_move(5, 'O')==False
    assert game.make_move(6, 'O')==True