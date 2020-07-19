import pygame
import sys
import math
import os

pygame.init()
winLength = 450
SCREEN = pygame.display.set_mode((winLength, winLength))
CLOCK = pygame.time.Clock()
SCREEN.fill((255, 255, 255))
pygame.display.set_caption("Sudoku Solver")

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables
run = True
algorithm = False
board = []
blockSize = winLength // 9


# Functions
def boardInit(fileName):
    file = open(fileName, "r")
    count = 0
    for line in file.readlines():
        board.append([])
        for i in line:
            if str(i) != '\n':
                board[count].append(str(i))
        count += 1

def drawBoard():
    print(board)

# Init Functions
boardInit(os.path.dirname(os.path.realpath(__file__)) + '/board.txt')

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