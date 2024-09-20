import pyray as pr
from general_datas import General_Data
from buttons import Button

class Clicker:

    def init():
        Clicker.Clickers.init()
        Clicker.Damage.init()
        Clicker.Speed.init()
        Clicker.Visuals.init()
        Clicker.updateClass()
        
    def updateClass():
        Clicker.Clickers.updateClass()
        Clicker.Damage.updateClass()
        Clicker.Speed.updateClass()
        Clicker.Visuals.updateClass()
        
    def __init__(self, x, y):
        self.position = pr.Vector2(x,y)
        self.homePosition = pr.Vector2(x,y)
        self.triangle = Clicker.Visuals.setTriangle(self.position)
        self.frame_count = 0 
    
    def updateSelf(self):
        self.position.y -= Clicker.Visuals.padding/Clicker.Speed.frames_per_click
        self.frame_count += 1
        if self.frame_count >= Clicker.Speed.frames_per_click:
            Clicker.click()
            self.frame_count = 0
            self.position.y = self.homePosition.y
        self.triangle = Clicker.Visuals.setTriangle(self.position)

    def click():
        General_Data.money += Clicker.Damage.value

    def draw(self):
        pr.draw_triangle(self.triangle[0], self.triangle[1], self.triangle[2], Clicker.Visuals.color)

            
            
    class Clickers:
        List = []
        cost = 100
        listLength = 0

        def init():
            Button.Dict["Clicker.Clickers.buy"] = Button(20,190,50,20,pr.BLUE, "", Clicker.Clickers.buy)
            
        def updateClass():
            Clicker.Clickers.listLength = len(Clicker.Clickers.List)
            Button.Dict["Clicker.Clickers.buy"].name = f"{Clicker.Clickers.cost}: clickers +1"


        def buy():
            if General_Data.money >= Clicker.Clickers.cost:
                General_Data.money -= Clicker.Clickers.cost
                Clicker.Clickers.cost *= 2
                Clicker.Clickers.add()


        def add():
            position = Clicker.Clickers.getNextPosition()
            Clicker.Clickers.List.append(Clicker(position.x, position.y))
            Clicker.Clickers.updateClass()

        def getNextPosition():
            width = Clicker.Visuals.dimentions.x + Clicker.Visuals.padding 
            height = Clicker.Visuals.dimentions.y + Clicker.Visuals.padding 
            rect = Button.Dict["Clicker.click"].rectangle
            bottomLeft = pr.Vector2(rect.x, rect.y + rect.height)
            rowLength = int((rect.width + Clicker.Visuals.padding) / width)
            position = pr.Vector2((bottomLeft.x + Clicker.Visuals.dimentions.x/2) + (width * (Clicker.Clickers.listLength % rowLength)), 
                                (bottomLeft.y + Clicker.Visuals.padding) + (height * int(Clicker.Clickers.listLength / rowLength)))
            return position

        
    class Damage:
        level = 1
        value = None
        cost  = None

        def init():
            Button.Dict["Clicker.click"] = Button(550,100,150,150,pr.RED,"click me", Clicker.click)
            Button.Dict["Clicker.Damage.buy"] = Button(20,150,50,20,pr.BLUE, "", Clicker.Damage.buy)

        def updateClass():
            Clicker.Damage.value = Clicker.Damage.level
            Clicker.Damage.cost = 10 * (2 ** Clicker.Damage.level)
            Button.Dict["Clicker.Damage.buy"].name = str(Clicker.Damage.cost) + ": click damage +1"

        def buy():
            if General_Data.money >= Clicker.Damage.cost:
                General_Data.money -= Clicker.Damage.cost
                Clicker.Damage.upgrade()
                
            
        def upgrade():
                Clicker.Damage.level += 1
                Clicker.Damage.updateClass()

                
    class Speed:
        level = 0
        cost = 1000
        clicks_per_second = 1
        frames_per_click = None

        def init():
            Button.Dict["Clicker.Speed.buy"] = Button(20,230,50,20,pr.BLUE, "", Clicker.Speed.buy)

        def updateClass():
            Clicker.Speed.clicks_per_second = (Clicker.Speed.level + 1)
            Clicker.Speed.frames_per_click = General_Data.FRAMES_PER_SECOND / Clicker.Speed.clicks_per_second
            Button.Dict["Clicker.Speed.buy"].name = f"{Clicker.Speed.cost}: cps +1" 

        def buy():
            if General_Data.money >= Clicker.Speed.cost:
                General_Data.money -= Clicker.Speed.cost
                Clicker.Speed.cost *= 2
                Clicker.Speed.upgrade()

        def upgrade():
            Clicker.Speed.level += 1
            Clicker.Speed.updateClass()

            
    class Visuals:
        color = pr.WHITE
        dimentions = pr.Vector2(14,21)
        padding = 5

        def init():
            pass
        def updateClass():
            pass

        def setTriangle(position):
            triangle = [pr.Vector2(position.x, position.y), 
                        pr.Vector2(position.x-Clicker.Visuals.dimentions.x/2, position.y+Clicker.Visuals.dimentions.y), 
                        pr.Vector2(position.x+Clicker.Visuals.dimentions.x/2, position.y+Clicker.Visuals.dimentions.y)]
            return triangle



