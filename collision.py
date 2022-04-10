import pygame as pg
import sys


pg.init()

FPS = 120
window_width = 600
window_height = 400

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

r = 50
width_rect = 150
height_rect = 100

width_rect1 = 150
height_rect1 = 100

x, y = 100, 300
direct_x= 1

x1, y1 = 100, 300
direct_x1 = 1

x_rect = window_width // 2 - width_rect // 2
y_rect = window_height // 2 - height_rect // 2

x_rect1 =(window_width // 2 - width_rect // 2) + 160
y_rect1 = window_height // 2 - height_rect // 2

screen = pg.display.set_mode()
var = (window_width, window_height)

clock = pg.time.Clock()

run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            with open('scores.txt', 'w') as score:
                score.write(f'Количество столкновений: {count_of_collision}')
            sys.exit()

clock.tick(FPS)
screen.fill(white)

# ball_1 = pg.draw.circle(screen, red, (x, y), r)
# ball_2 = pg.draw.circle(screen, black, (x1, y1), r)

pg.draw.rect(screen, red,
            (x_rect, y_rect, width_rect, height_rect)
             )
pg.draw.rect(screen, red,
            ((window_width // 2 - width_rect // 2) + 160, window_height // 2 - height_rect // 2, width_rect, height_rect)
             )




x_rect += direct_x
if x_rect >= window_width - width_rect  or x < 0 + width_rect1:
    direct_x = -direct_x


x_rect1 += -direct_x1
if x_rect1 >= window_width - height_rect or x1 < 0 + height_rect1:
    direct_x1 = -direct_x1

if x_rect1 + (width_rect1 // 2) == x_rect - (width_rect // 2):
    direct_x = -direct_x
    direct_x1 = -direct_x1


pg.display.update()