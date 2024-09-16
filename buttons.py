import pyray as pr
from general_datas import General_Data

class Button:
    Dict = {}

    def __init__(self, x, y, width, height, color, name, function):
        self.rectangle = pr.Rectangle(x, y, width, height)
        self.color = color
        self.name = name
        self.function = function
    def __str__(self):
        return f"[{self.x}, {self.y}, {self.width}, {self.height}, {self.color}\nfunction: {self.string}"
    def isClicked(self):
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT) and pr.check_collision_point_rec(pr.get_mouse_position(),self.rectangle):
            return True
        else:
            return False
    def onClick(self):
        if self.function and self.isClicked():
            return self.function()
    def draw(self):
        pr.draw_rectangle_rec(self.rectangle, self.color)
        pr.draw_text(self.name, int(self.rectangle.x), int(self.rectangle.y), 10, pr.WHITE)

