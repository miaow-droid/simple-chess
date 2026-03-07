from .board import ChessBoard
from .standard_chess_rules import StandardChessRules

class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.rules = StandardChessRules(self.board)
        self.current_turn = "W"  # White starts first
        self.game_over = False

    def make_move(self, from_position, to_position):
        """Make a move on the board if it's valid."""
        if self.game_over:
            raise ValueError("The game is over. No more moves can be made.")
        
        piece = self.board.get_piece_at(from_position)
        if piece is None:
            raise ValueError(f"No piece at position {from_position} to move.")
        
        if piece.color != self.current_turn:
            raise ValueError(f"It's {self.current_turn}'s turn. Cannot move {piece.color}'s piece.")
        
        if not self.rules.is_valid_move(from_position, to_position):
            raise ValueError(f"Invalid move from {from_position} to {to_position}.")
        
        self.board.move_piece(from_position, to_position)
        self.switch_turn()

    def switch_turn(self):
        """Switch the turn to the other player."""
        self.current_turn = "B" if self.current_turn == "W" else "W"