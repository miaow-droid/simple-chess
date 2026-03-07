import unittest

from game.board import ChessBoard
from game.standard_chess_rules import StandardChessRules
from utils.constants import COLOR


class TestStandardChessRules(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard()
        self.rules = StandardChessRules(self.board)

    def test_pawn_initial_two_square_move_valid(self):
        self.assertTrue(self.rules.is_valid_move("e2", "e4"))

    def test_pawn_cannot_move_backwards(self):
        self.assertFalse(self.rules.is_valid_move("e2", "e1"))

    def test_knight_can_jump_over_pieces(self):
        self.assertTrue(self.rules.is_valid_move("b1", "c3"))

    def test_bishop_move_blocked_by_piece(self):
        self.assertFalse(self.rules.is_valid_move("c1", "h6"))

    def test_queen_move_blocked_by_piece(self):
        self.assertFalse(self.rules.is_valid_move("d1", "d3"))

    def test_cannot_capture_own_piece(self):
        self.assertFalse(self.rules.is_valid_move("b1", "d2"))

    def test_king_cannot_move_two_squares_without_castling(self):
        self.assertFalse(self.rules.is_valid_move("e1", "e3"))

    def test_black_pawn_initial_two_square_move_valid(self):
        self.assertTrue(self.rules.is_valid_move("e7", "e5"))

    def test_move_to_out_of_bounds_rank_is_invalid(self):
        self.assertFalse(self.rules.is_valid_move("e2", "e9"))

    def test_knight_move_off_board_is_invalid(self):
        self.assertFalse(self.rules.is_valid_move("b1", "a0"))

    @unittest.skip("TODO: Implement castling logic")
    def test_castling_kingside_white(self):
        self.assertTrue(self.rules.is_valid_move("e1", "g1"))

    @unittest.skip("TODO: Implement en passant logic")
    def test_en_passant_white_capture(self):
        # Placeholder for an en passant scenario once last-move tracking exists.
        self.assertTrue(self.rules.is_valid_move("e5", "d6"))

    @unittest.skip("TODO: Implement promotion handling")
    def test_pawn_promotion_trigger(self):
        self.assertTrue(self.rules.is_valid_move("e7", "e8"))


if __name__ == "__main__":
    unittest.main()
