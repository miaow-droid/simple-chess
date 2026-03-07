from utils.constants import PIECE_TYPES, PIECE_SYMBOLS

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
        self.type = PIECE_TYPES["pawn"]

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = PIECE_TYPES["knight"]

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = PIECE_TYPES["bishop"]

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = PIECE_TYPES["rook"]

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = PIECE_TYPES["queen"]

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.type = PIECE_TYPES["king"]