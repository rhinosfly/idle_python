import pyray as pr
from general_datas import General_Data
from buttons import Button
from clicks import Click

class Clicker:
    color = pr.WHITE
    clicks_per_minute = 60
    frames_per_click = None
    cost = 100
    listLength = 0
    List = []

    def init():
        Clicker.updateClass()
        Button.Dict["BuyClicker"] = Button(20,140,50,20,pr.BLUE, "100: clickers +1", Clicker.buy)
    def __init__(self, x, y):
       self.position = pr.Vector2(x,y)
       self.frame_count = 0
    def updateClass():
        Clicker.frames_per_click = Clicker.clicks_per_minute / 60.0 * General_Data.FRAMES_PER_SECOND
        Clicker.listLength = len(Clicker.List)
    def buy():
        if General_Data.money >= Clicker.cost:
            Clicker.add()
            Clicker.cost *= 2
            Button.Dict["BuyClicker"].name = f"{Clicker.cost}: clickers +1"
    def add():
        position = Clicker.getNextPosition()
        Clicker.List.append(Clicker(position.x, position.y))
        Clicker.updateClass()
    def getNextPosition():
        width = 30
        height = 30
        rect = Button.Dict["clickMe"].rectangle
        bottomLeft = pr.Vector2(rect.x, rect.y + rect.height)
        rowLength = int(rect.width / width)
        position = pr.Vector2((bottomLeft.x + 15) + (width * (Clicker.listLength % rowLength)), 
                              (bottomLeft.y + 15) + (height * int(Clicker.listLength / rowLength)))
        return position
    def updateSelf(self):
        self.frame_count += 1
        if self.frame_count >= Clicker.frames_per_click:
            Click.click()
            self.frame_count = 0
    def draw(self):
        pr.draw_circle(int(self.position.x), int(self.position.y), 10, Clicker.color)

