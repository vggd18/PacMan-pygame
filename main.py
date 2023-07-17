# eu amo cecilia
import pygame as pg
from board import boards
import math

# VARIÁVEIS GERAIS
largura = 900
altura = 950
PI = math.pi
color = 'blue'
px = 30
counter = 0
player_x = 450
player_y = 665
direction = 0

# PLAYER SPRITES
player_images = []
for i in range (1,8):
    player_images.append(pg.transform.scale(pg.image.load(f'sprites/pacman/PacMan{i}.png'), (30,30)))

pg.init()
screen = pg.display.set_mode((largura,altura))
timer = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 20)
level = boards

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

def draw_player():
    if direction == 0:          #LEFT
        screen.blit(player_images[counter//10], (player_x, player_y))
    if direction == 1:          #RIGHT
        screen.blit(player_images[2+counter//10], (player_x, player_y))
    if direction == 2:          #UP
        screen.blit(player_images[4+counter//10], (player_x, player_y))
    if direction == 3:          #DOWN
        screen.blit(player_images[6+counter//10], (player_x, player_y))

while True:
    timer.tick(60)

    if counter < 19:
        counter += 1
    else:
        counter = 0

    draw_board(level)
    draw_player()

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        #if event.type == pg.KEYDOWN:


    pg.display.flip()