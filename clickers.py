#Clicker class definition

import pyray as pr
import data

class Clicker:
    color = pr.WHITE
    def __init__(self, x, y):
       self.position = pr.Vector2(x,y)
    def add():
        List.append(Clicker(pr.get_random_value(100,700), pr.get_random_value(50,350)))
    def draw(self):
        pr.draw_circle(int(self.position.x), int(self.position.y), 10, Clicker.color)

List = []
