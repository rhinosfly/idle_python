import pyray as pr
from general_datas import General_Data
from buttons import Button
from clicks import Click

class Clicker:
    color = pr.WHITE
    clicks_per_minute = 60
    frames_per_click = None
    dimentions = pr.Vector2(14,21)
    padding = 5
    cost = 100
    listLength = 0
    List = []

    def init():
        Clicker.updateClass()
        Button.Dict["BuyClicker"] = Button(20,140,50,20,pr.BLUE, "100: clickers +1", Clicker.buy)

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
        width = Clicker.dimentions.x + Clicker.padding 
        height = Clicker.dimentions.y + Clicker.padding 
        rect = Button.Dict["clickMe"].rectangle
        bottomLeft = pr.Vector2(rect.x, rect.y + rect.height)
        rowLength = int((rect.width + Clicker.padding) / width)
        position = pr.Vector2((bottomLeft.x + Clicker.dimentions.x/2) + (width * (Clicker.listLength % rowLength)), 
                              (bottomLeft.y + Clicker.padding) + (height * int(Clicker.listLength / rowLength)))
        return position
    
    def __init__(self, x, y):
        self.position = pr.Vector2(x,y)
        self.triangle = Clicker.setTriangle(self.position)
        self.frame_count = 0 

    def setTriangle(position):
        triangle = [pr.Vector2(position.x, position.y), 
                    pr.Vector2(position.x-Clicker.dimentions.x/2, position.y+Clicker.dimentions.y), 
                    pr.Vector2(position.x+Clicker.dimentions.x/2, position.y+Clicker.dimentions.y)]
        return triangle

    def updateSelf(self):
        self.frame_count += 1
        if self.frame_count >= Clicker.frames_per_click:
            Click.click()
            self.frame_count = 0

    def draw(self):
        pr.draw_triangle(self.triangle[0], self.triangle[1], self.triangle[2], Clicker.color)

