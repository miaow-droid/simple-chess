from .board import ChessBoard
from .standard_chess_rules import StandardChessRules
from utils.constants import COLOR
from game.piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

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
        
        if self.would_be_in_check_after_move(from_position, to_position):
            raise ValueError(f"Move from {from_position} to {to_position} would put {self.current_turn} in check.")
    
        
        self.board.move_piece(from_position, to_position)

        if self.in_check(self.opponent_color()):
            if self.checkmate(self.opponent_color()):
                self.game_over = True
                print(f"Checkmate! {self.current_turn} wins.")
            else:
                print(f"{self.opponent_color()} is in check.")
        
        if self.stalemate(self.opponent_color()):
            self.game_over = True
            print("Stalemate! The game is a draw.")
                
        if not self.game_over:
            self.switch_turn()

    def switch_turn(self):
        """Switch the turn to the other player."""
        self.current_turn = COLOR["black"] if self.current_turn == COLOR["white"] else COLOR["white"]

    def in_check(self, color):
        """Check if the specified color is in check."""
        king_pos = self.find_king(color)
        for position, piece in self.board.board.items():
            if piece and piece.color == self.opponent_color(color):
                if self.rules.is_valid_move(position, king_pos):
                    return True
        return False
    
    def checkmate(self, color):
        """Check if the specified color is in checkmate."""
        if not self.in_check(color):
            return False  # Not in check, so cannot be in checkmate
        valid_moves = self.get_all_valid_moves(color)
        return len(valid_moves) == 0
    
    def stalemate(self, color):
        """Check if the specified color is in stalemate."""
        if self.in_check(color):
            return False  # In check, so cannot be in stalemate
        valid_moves = self.get_all_valid_moves(color)
        return len(valid_moves) == 0
    
    def reset_game(self):
        """Reset the game to the initial state."""
        self.board = ChessBoard()
        self.rules = StandardChessRules(self.board)
        self.current_turn = COLOR["white"]
        self.game_over = False

    def find_king(self, color):
        """Find the king piece of the specified color."""
        for position, piece in self.board.board.items():
            if piece and piece.color == color and piece.type == "K":
                return position
        raise ValueError(f"No king found for color {color}.")
    
    def opponent_color(self, color=None):
        """Get the opponent's color."""
        if color is None:
            color = self.current_turn
        return COLOR["black"] if color == COLOR["white"] else COLOR["white"]
    
    def would_be_in_check_after_move(self, from_position, to_position):
        """Check if making a move would put the current player in check."""
        piece = self.board.get_piece_at(from_position)
        if piece is None:
            raise ValueError(f"No piece at position {from_position} to move.")
        
        # Save the current state of the board and piece positions
        original_piece_has_moved = piece.has_moved
        captured_piece = self.board.get_piece_at(to_position)
        
        # Temporarily make the move
        self.board.move_piece(from_position, to_position)
        
        in_check = self.in_check(piece.color)
        
        # Undo the move
        self.board.set_piece_at(from_position, piece)
        self.board.set_piece_at(to_position, captured_piece)
        piece.position = from_position
        piece.has_moved = original_piece_has_moved
        if captured_piece:
            captured_piece.position = to_position  # Restore captured piece's position if it was captured
        
        return in_check
    
    def get_all_valid_moves(self, color):
        """Get all valid moves for the specified color."""
        valid_moves = []
        for from_position, piece in self.board.board.items():
            if piece and piece.color == color:
                for to_position in self.board.board.keys():
                    if self.rules.is_valid_move(from_position, to_position):
                        if not self.would_be_in_check_after_move(from_position, to_position):
                            valid_moves.append((from_position, to_position))
        return valid_moves