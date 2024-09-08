#Clicker class definition

import pyray as pr
import data

class Clicker:
    color = pr.WHITE
    def __init__(self, x, y):
       self.position = pr.Vector2(x,y)
    def draw(self):
        pr.draw_circle(int(self.position.x), int(self.position.y), 10, Clicker.color)

List = []
