#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import *
from random import randint,choice

scr = display.set_mode((480,485))
tiles = [scr.fill(randint(0,0xffffff),(x,y,20,20)) for x in range(5,480,25) for y in range(5,255,25)]
target = choice(tiles)
scr.fill(scr.get_at(choice(tiles).center),(205,300,75,75))
display.flip()
while len(tiles) > 1:
    ev = event.wait()
    if ev.type == MOUSEBUTTONDOWN:
        index = Rect(ev.pos,(0,0)).collidelist(tiles)
        if index > -1 and tiles[index] == target:
            display.update(scr.fill(0,tiles.pop(index)))
            target = choice(tiles)
            display.update(scr.fill(scr.get_at(target.center),(205,300,75,75)))
    elif ev.type == KEYDOWN and ev.key == K_SPACE:
        target = choice(tiles)
        display.update(scr.fill(scr.get_at(target.center),(205,300,75,75)))
    elif ev.type == QUIT: break
