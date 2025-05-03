import pygame
from halma.constants import *


class Piece:
    #A class representing a piece on the Halma board.
    Attributes:
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def position(self):
        """
        Returns the current position of the piece as a tuple (row, col).
        Returns:
            A tuple representing the current position of the piece, with the row
            and column indices as the first and second elements of the tuple, respectively.
        """
        return (self.row, self.col)

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, win):
       
             #win (pygame.Surface): The window surface to draw on.
        radius = SQUARE_SIZE//2 - PADDING

        pygame.draw.circle(win, GREY, (self.x, self.y), radius + OUTLINE)

        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        #Returns a string representation of the piece's color.
            #str: The string representation of the piece's color.

        return str(self.color)
