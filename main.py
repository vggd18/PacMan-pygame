import pygame
from board import boards
import math

largura = 900
altura = 950
PI = math.pi
color = 'blue'

pygame.init()

screen = pygame.display.set_mode([largura,altura])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards

def draw_board(lvl):
    posx = largura // 30 # num2
    posy = (altura - 50) // 32 # num1

    for i in range (len(lvl)):
        for j in range (len(lvl[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, '#fdfd96', ((j * posx + (0.5 * posx)), (i * posy + (0.5 * posy))), 4)
            elif level[i][j] == 2:
                pygame.draw.circle(screen, '#fdfd96', ((j * posx + (0.5 * posx)), (i * posy + (0.5 * posy))), 8)
            elif level[i][j] == 3:
                pygame.draw.line(screen, color, ((j * posx + (0.5 * posx)), i * posy), 
                                                 ((j * posx + (0.5 * posx)), i*posy + posy), 3) 
            elif level[i][j] == 4:
                pygame.draw.line(screen, color, (j * posx, i * posy + (0.5 * posy)),
                                                 (j * posx + posx, i * posy + (0.5 * posy)), 3)

            elif level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * posx - (0.4 * posx)-2), i * posy + (0.5 * posy), posx, posy], 0, PI/2, 3)

            elif level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * posx + (0.5 * posx)), i * posy + (0.5 * posy), posx, posy], PI/2, PI, 3)
            elif level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * posx + (0.5 * posx)), i * posy - (0.5 * posy), posx, posy], PI, 3*PI/2, 3)
            elif level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * posx - (0.4 * posx)-2), i * posy - (0.5 * posy), posx, posy], 3*PI/2, 2* PI, 3)
            elif level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * posx, i * posy + (0.5 * posy)),
                                                 (j * posx + posx, i * posy + (0.5 * posy)), 3)

while True:
    timer.tick(60)
    screen.fill('black')
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()