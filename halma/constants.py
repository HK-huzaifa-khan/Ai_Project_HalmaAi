# Board dimensions
ROWS, COLS = 8, 8
SQUARE_SIZE = 60  # Reduced from 80 to make the window smaller
WIDTH, HEIGHT = COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE  # Window size matches board size

# Starting zones
BLACK_START = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]
WHITE_START = [(4, 7), (5, 6), (5, 7), (6, 5), (6, 6), (6, 7), (7, 4), (7, 5), (7, 6), (7, 7)]

# Dark spaces in starting zones
WHITE_DARK = [(4, 7), (5, 6), (6, 5), (7, 4), (6, 7), (7, 6)]
BLACK_DARK = [(1, 0), (0, 1), (3, 0), (2, 1), (1, 2), (0, 3)]

# Board Colors 
DARK = (153, 91, 34)
LIGHT = (223, 169, 109)

# Piece colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Movement colors 
LIGHT_GREEN = (93, 187, 99)
EMERALD = (2, 138, 15)  # Move marker

# Piece sizing
PADDING = 15  # Larger padding = smaller pieces
OUTLINE = 2
