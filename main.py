import sys
from random import randrange, choice
import pygame as pg


class Ball():
    def __init__(self, window):
        self.window = window
        self.pos_x = pg.display.get_window_size()[0] // 2
        self.pos_y = pg.display.get_window_size()[1] // 2
        self.radius = 20
        self.speed = list(range(-10,0)) + list(range(1, 11))
        self.speed_x = choice(self.speed)
        self.speed_y = choice(self.speed)


    def draw(self):
        self.set_color()
        pg.draw.circle(self.window, self.color, (self.pos_x, self.pos_y), self.radius)


    def move(self):
        self.check_collision()
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y


    def check_collision(self):
        if self.pos_x + self.radius >= pg.display.get_window_size()[0] or\
            self.pos_x - self.radius <= 0:
            self.speed_x = -self.speed_x
        if self.pos_y + self.radius >= pg.display.get_window_size()[1] or\
            self.pos_y - self.radius <= 0:
            self.speed_y = -self.speed_y
      

    def set_color(self):
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))     
pg.init()

window_width = int(1000 / 1.5)
window_height = int(1000 / 1.5)
window_fps = 30
window_clock = pg.time.Clock()
window = pg.display.set_mode((window_width, window_height))

balls = [Ball(window) for i in range(200)]

while True:
    [sys.exit() for i in pg.event.get() if i.type == pg.QUIT]
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        sys.exit()

    window.fill((0, 0, 0))
    for ball in balls:
        ball.move()
        ball.draw()
    
    pg.display.update()
    window_clock.tick(window_fps)
