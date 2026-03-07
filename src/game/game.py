from .board import ChessBoard
from .standard_chess_rules import StandardChessRules
from utils.constants import COLOR

class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.rules = StandardChessRules(self.board)
        self.current_turn = COLOR["white"]  # White starts first
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
        self.current_turn = COLOR["black"] if self.current_turn == COLOR["white"] else COLOR["white"]

    def in_check(self, color):
        """Check if the specified color is in check."""
        # Placeholder for check detection logic
        return False
    
    def checkmate(self, color):
        """Check if the specified color is in checkmate."""
        # Placeholder for checkmate detection logic
        return False
    
    def stalemate(self, color):
        """Check if the specified color is in stalemate."""
        # Placeholder for stalemate detection logic
        return False
    
    def reset_game(self):
        """Reset the game to the initial state."""
        self.board = ChessBoard()
        self.rules = StandardChessRules(self.board)
        self.current_turn = COLOR["white"]
        self.game_over = False