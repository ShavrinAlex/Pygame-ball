import sys
import random
import pygame as pg


pg.init()

window_width = 500
window_height = 500

pg.display.set_mode((window_width, window_height))

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()


