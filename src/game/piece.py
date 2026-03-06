from utils.constants import PIECE_TYPES, COLOR, BOARD_SIZE, FILES, RANKS, PIECE_SYMBOLS

color = COLOR
type = PIECE_TYPES
posistion = {
    "file": FILES,
    "rank": RANKS
}
piece_symbols = PIECE_SYMBOLS

class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.type = None
        self.has_moved = False

    def __str__(self):
        return f"{piece_symbols[self.color][self.type]} at {self.position}"

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["pawn"]

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["knight"]

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["bishop"]

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["rook"]

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["queen"]

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = type["king"]