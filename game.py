import pygame
from halma.board import Board
from halma.constants import *


class Game:
   
    def __init__(self, win):
       
        self._init()
        self.win = win

    def update(self):
        
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_selected(self.selected)
        pygame.display.update()

    def _init(self):
        
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = []

    def get_board(self):
        
        return self.board

    def reset(self):
       
        self._init()

    def select(self, row, col):
       
        # If a piece has already been selected
        if self.selected:

            # Try to move the piece to the new location
            result = self._move(row, col)

            # If move is not valid, reset the selection and try again
            if not result:
                self.selected = None
                self.select(row, col)       # If not, reselect piece and attempt new move

        # If no piece has been selected yet
        else:
            piece = self.board.get_piece(row, col)

        # Check if user selects a valid piece on their turn
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def draw_selected(self, selected):
       

        if self.selected:
            pygame.draw.circle(self.win, LIGHT_GREEN, (selected.x, selected.y), 47, 10)

    def _move(self, row, col):
        

        piece = self.board.get_piece(row, col)

        # If selected piece can be moved to new location
        if self.selected and piece == 0 and (row, col) in self.valid_moves:

            # Move the piece
            self.board.move(self.selected, row, col)

            # Switch the turn to the other player
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):

        # loop through each valid move and draw a blue circle on the board to represent it
        for move in moves:
            row, col = move

            # the circle is centered at the middle of the square and has a radius of 15 pixels
            pygame.draw.circle(
                self.win,
                EMERALD,
                (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                15
            )

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def change_turn(self):
        # clear the list of valid moves for the previous player
        self.valid_moves = []

        # clear the selected piece for the previous player
        self.selected = None

        # change the turn to the other player and increment turns counter
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def winner(self):
        return self.board.winner()

