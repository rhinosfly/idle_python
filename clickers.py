import pyray as pr
from buttons import Button

class Clicker:
    color = pr.WHITE
    List = []

    def init():
       Button.Dict["AddClicker"] = Button(20,140,50,20,pr.BLUE, "100: clickers +1", Clicker.add)
    def __init__(self, x, y):
       self.position = pr.Vector2(x,y)
    def add():
        Clicker.List.append(Clicker(pr.get_random_value(100,700), pr.get_random_value(50,350)))
    def draw(self):
        pr.draw_circle(int(self.position.x), int(self.position.y), 10, Clicker.color)

