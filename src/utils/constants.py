
PIECE_TYPES = {
    "pawn": "P",
    "knight": "N",
    "bishop": "B",
    "rook": "R",
    "queen": "Q",
    "king": "K"
}

COLOR = {
    "white": "W",
    "black": "B"
}

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8']

PIECE_SYMBOLS = {
    "W": {
        "P": "♙",
        "N": "♘",
        "B": "♗",
        "R": "♖",
        "Q": "♕",
        "K": "♔"
    },
    "B": {
        "P": "♟",
        "N": "♞",
        "B": "♝",
        "R": "♜",
        "Q": "♛",
        "K": "♚"
    }
}

GLOBAL_BUTTON_STYLE = {
    "configure": {
        "background": "#06051D",
        "foreground": "#E0E0E0",
    },
    "map": {
        "background": [("active", "#12103B"), ("pressed", "#272641"), ("hover", "#201F3D")],
        "foreground": [("disabled", "#8A8A8A")]
    }
}