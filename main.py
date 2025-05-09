import pygame
import os
import time
from halma.constants import *
from halma.game import Game
from minimax.algorithm import get_best_move

# Initialize Pygame
pygame.init()

# Get screen resolution
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Set window size
WINDOW_WIDTH = min(COLS * SQUARE_SIZE, SCREEN_WIDTH - 100)
WINDOW_HEIGHT = min(ROWS * SQUARE_SIZE, SCREEN_HEIGHT - 100)

# Center window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
    (SCREEN_WIDTH - WINDOW_WIDTH) // 2,
    (SCREEN_HEIGHT - WINDOW_HEIGHT) // 2
)

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Halma")

FPS = 60
FONT = pygame.font.SysFont("comicsans", 50)

AI_DEPTH = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3
}

def draw_text(text, color, y_offset=0):
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + y_offset))
    WIN.blit(text_surface, text_rect)

def show_start_message():
    WIN.fill(DARK)
    draw_text("Let the game begin!!!", WHITE)
    pygame.display.update()
    pygame.time.delay(2000)

def show_end_message(winner):
    WIN.fill(DARK)
    if winner == "White wins":
        draw_text("You lose!", WHITE, -50)
        draw_text("AI wins!", WHITE, 50)
    else:
        draw_text("You win!", WHITE, -50)
        draw_text("Congratulations!", WHITE, 50)
    pygame.display.update()
    pygame.time.delay(3000)

def select_ai_difficulty():
    difficulties = ["Easy", "Medium", "Hard"]
    selected = 0

    while True:
        WIN.fill(DARK)
        for i, difficulty in enumerate(difficulties):
            color = WHITE if i == selected else GREY
            draw_text(difficulty, color, i * 50 - 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN:
                    return difficulties[selected]

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    ai_difficulty = select_ai_difficulty()
    if ai_difficulty is None:
        return

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    show_start_message()

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            new_board = get_best_move(game.get_board(), AI_DEPTH[ai_difficulty], game)
            game.ai_move(new_board)

        winner = game.winner()
        if winner is not None:
            show_end_message(winner)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
