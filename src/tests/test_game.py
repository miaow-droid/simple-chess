import unittest

from game.game import Game
from utils.constants import COLOR


class TestGameFlow(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_turn_is_white(self):
        self.assertEqual(self.game.current_turn, COLOR["white"])

    def test_valid_move_updates_board_and_turn(self):
        self.game.make_move("e2", "e4")

        moved_piece = self.game.board.get_piece_at("e4")
        self.assertIsNotNone(moved_piece)
        self.assertEqual(moved_piece.type, "P")
        self.assertEqual(moved_piece.color, COLOR["white"])
        self.assertTrue(moved_piece.has_moved)

        self.assertIsNone(self.game.board.get_piece_at("e2"))
        self.assertEqual(self.game.current_turn, COLOR["black"])

    def test_wrong_turn_raises_error(self):
        with self.assertRaises(ValueError):
            self.game.make_move("e7", "e5")

    def test_illegal_rook_move_raises_error(self):
        with self.assertRaises(ValueError):
            self.game.make_move("a1", "a3")

    def test_pawn_capture_updates_board_state(self):
        # e2 -> e4, d7 -> d5, e4 x d5
        self.game.make_move("e2", "e4")
        self.game.make_move("d7", "d5")
        self.game.make_move("e4", "d5")

        captured_square_piece = self.game.board.get_piece_at("d5")
        self.assertIsNotNone(captured_square_piece)
        self.assertEqual(captured_square_piece.type, "P")
        self.assertEqual(captured_square_piece.color, COLOR["white"])
        self.assertIsNone(self.game.board.get_piece_at("e4"))

    def test_turn_sequence_across_multiple_moves(self):
        self.assertEqual(self.game.current_turn, COLOR["white"])

        self.game.make_move("g1", "f3")
        self.assertEqual(self.game.current_turn, COLOR["black"])

        self.game.make_move("g8", "f6")
        self.assertEqual(self.game.current_turn, COLOR["white"])

        self.game.make_move("b1", "c3")
        self.assertEqual(self.game.current_turn, COLOR["black"])

    def test_invalid_destination_square_raises_error(self):
        with self.assertRaises(ValueError):
            self.game.make_move("e2", "e9")


if __name__ == "__main__":
    unittest.main()
