# eu amo cecilia

import pygame as pg
from board import boards
import math

largura = 900
altura = 950
PI = math.pi
color = 'blue'
px = 30
animation = 0

pg.init()
screen = pg.display.set_mode((largura,altura))
timer = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 20)
level = boards
sprite = pg.image.load("PacMan_sprites.png")

def draw_board(lvl):
    posx = largura // 30 # num2
    posy = (altura - 50) // 32 # num1

    for i in range (len(lvl)):
        for j in range (len(lvl[i])):
            if level[i][j] == 1:
                pg.draw.circle(screen, '#fdfd96', ((j * posx + (0.5 * posx)), (i * posy + (0.5 * posy))), 4)
            elif level[i][j] == 2:
                pg.draw.circle(screen, '#fdfd96', ((j * posx + (0.5 * posx)), (i * posy + (0.5 * posy))), 8)
            elif level[i][j] == 3:
                pg.draw.line(screen, color, ((j * posx + (0.5 * posx)), i * posy), 
                                                 ((j * posx + (0.5 * posx)), i*posy + posy), 3) 
            elif level[i][j] == 4:
                pg.draw.line(screen, color, (j * posx, i * posy + (0.5 * posy)),
                                                 (j * posx + posx, i * posy + (0.5 * posy)), 3)

            elif level[i][j] == 5:
                pg.draw.arc(screen, color, [(j * posx - (0.4 * posx)-2), i * posy + (0.5 * posy), posx, posy], 0, PI/2, 3)

            elif level[i][j] == 6:
                pg.draw.arc(screen, color, [(j * posx + (0.5 * posx)), i * posy + (0.5 * posy), posx, posy], PI/2, PI, 3)
            elif level[i][j] == 7:
                pg.draw.arc(screen, color, [(j * posx + (0.5 * posx)), i * posy - (0.5 * posy), posx, posy], PI, 3*PI/2, 3)
            elif level[i][j] == 8:
                pg.draw.arc(screen, color, [(j * posx - (0.4 * posx)-2), i * posy - (0.5 * posy), posx, posy], 3*PI/2, 2* PI, 3)
            elif level[i][j] == 9:
                pg.draw.line(screen, 'white', (j * posx, i * posy + (0.5 * posy)),
                                                 (j * posx + posx, i * posy + (0.5 * posy)), 3)

def draw_player(direction, move):
    if direction == 0:      #direita
        screen.blit(sprite, (55,55),(911 + (30 * move), (0), px, px))
    if direction == 1:      #esquerda  
        screen.blit(sprite, (55,55),(911 + (30 * move), (31), px, px))
    if direction == 2:      #cima
        screen.blit(sprite, (55,55),(911 + (30 * move), (62), px, px))
    if direction == 3:      #baixo
        screen.blit(sprite, (55,55),(911 + (30 * move), (93), px, px))

while True:
    timer.tick(60)
    
    #animation += 1
    #if animation > 20:
    #    animation = 0
        

    draw_board(level)
    print()
    draw_player(0, animation//10)

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.flip()