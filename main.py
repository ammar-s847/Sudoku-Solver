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
algorithm = False
board = [[0 for x in range(9)] for y in range(9)]

# Functions
def boardInit(fileName):
    file = open(fileName, "r")
    

# PyGame Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: # Press "SPACE" key to start the Algorithm.
                if not algorithm:
                    algorithm = True
                    print("Algorithm Started!")
    
    pygame.display.update()

if not run:
    pygame.quit()
    sys.exit()