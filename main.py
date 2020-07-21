import pygame
import sys
import os

pygame.init()
pygame.font.init()
winLength = 450
SCREEN = pygame.display.set_mode((winLength, winLength))
CLOCK = pygame.time.Clock()
SCREEN.fill((255, 255, 255))
pygame.display.set_caption("Sudoku Solver")

# Colours and Fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("calibri", 32)

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

def printBoard():
    for i in board:
        string = ""
        for j in i:
            string = string + j
        print(string)

def drawBoard():
    for y in range(len(board)):
        for x in range(len(board[y])):
            textContent = board[y][x]
            if textContent == '0':
                textContent = ''
            text = FONT.render(textContent, False, BLACK)
            SCREEN.blit(text, (blockSize * x + 17, blockSize * y + 10))
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def check(value, x, y):
    for c in range(len(board[y])): # Check Row
        if board[y][c] == str(value) and c != x:
            return False
    
    for c in range(len(board)): # Check Column
        if board[c][x] == str(value) and c != y:
            return False

    # Check Sub-section (3*3 area)
    sectionX = x // 3
    sectionY = y // 3
    for v in range(sectionY * 3, sectionY * 3 + 3):
        for w in range(sectionX * 3, sectionX * 3 + 3):
            if board[v][w] == str(value) and [w, v] != [x, y]:
                return False

    return True

def main():
    empty = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '0' or board[y][x] == 0:
                empty = [x, y]
                break
        if len(empty) > 0:
            break
    
    if len(empty) == 0:
        print("Final Board:")
        printBoard()
        return True
    
    for b in range(1, 10): # all integers from 1-9
        if check(b, empty[0], empty[1]):
            board[empty[1]][empty[0]] = str(b)

            if main(): # Recursion
                return True

            board[empty[1]][empty[0]] = '0'

    return False

# Init Functions
boardInit(os.path.dirname(os.path.realpath(__file__)) + '/board.txt')
print("Current Board: ")
printBoard()

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
                    main()

    drawBoard()

    pygame.display.update()

if not run:
    pygame.quit()
    sys.exit()