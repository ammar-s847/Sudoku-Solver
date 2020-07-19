import pygame
import sys
import math

pygame.init()
winX, winY = 450, 450
SCREEN = pygame.display.set_mode((winX, winY))
CLOCK = pygame.time.Clock()
SCREEN.fill((0,0,0))
pygame.display.set_caption("Sudoku Solver")

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables
run = True


# PyGame Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

if not run:
    pygame.quit()
    sys.exit()