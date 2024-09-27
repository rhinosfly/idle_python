import pyray as pr
from general_datas import General_Data
from buttons import Button

class Clicker:

    def init():
        Clicker.Clickers.init()
        Clicker.Damage.init()
        Clicker.Speed.init()
        #update
        Clicker.updateClass()
        #phase2
        Clicker.Clickers.init_phase2()

        
    def updateClass():
        Clicker.Clickers.updateClass()
        Clicker.Damage.updateClass()
        Clicker.Speed.updateClass()
        
    def __init__(self, x, y):
        self.Visuals = Clicker.Visuals(x,y)
        self.frame_count = 0 
    
    def updateSelf(self):
        self.Visuals.position.y -= Clicker.Visuals.padding / Clicker.Speed.frames_per_click #increment position by distance/timeperframe
        self.frame_count += 1
        if self.frame_count >= Clicker.Speed.frames_per_click:
            Clicker.click()
            self.frame_count = 0
            self.Visuals.position.y = self.Visuals.homePosition.y
        self.Visuals.triangle = Clicker.Visuals.setTriangle(self.Visuals.position)

    def click():
        General_Data.money += Clicker.Damage.value

    def draw(self):
        pr.draw_triangle(self.Visuals.triangle[0], self.Visuals.triangle[1], self.Visuals.triangle[2], Clicker.Visuals.color)

    def read(Dict):
        if "Clicker" in Dict:
            Dict = Dict["Clicker"]
        else:
            return
        if "Clickers" in Dict:
            Clicker.Clickers.targetLength = Dict["Clickers"]
        if "Damage" in Dict:
            Clicker.Damage.level = Dict["Damage"]
        if "Speed" in Dict:
            Clicker.Speed.level = Dict["Speed"]

    def write(file):
        #opener
        file.write("\"Clicker\" : \n\t{\n")
        #body
        file.write(f"\t\"Clickers\":{Clicker.Clickers.listLength},\n")
        file.write(f"\t\"Damage\":{Clicker.Damage.level},\n")
        file.write(f"\t\"Speed\":{Clicker.Speed.level}\n")
        #closer
        file.write("\t}\n")
           

    class Clickers:
        List = []
        cost = None
        listLength = 0
        targetLength = 0 #read from save file; does nothing afterward

        def init():
            Button.Dict["Clicker.Clickers.buy"] = Button(20,190,50,20,pr.BLUE, "", Clicker.Clickers.buy)
        
        def init_phase2():
            Clicker.Clickers.correctLength()

        def updateClass():
            Clicker.Clickers.listLength = len(Clicker.Clickers.List)
            Clicker.Clickers.cost = 100 * 2**Clicker.Clickers.listLength
            Button.Dict["Clicker.Clickers.buy"].name = f"{Clicker.Clickers.cost:,}: clickers +1"
            
        def correctLength():
            diff = Clicker.Clickers.targetLength - Clicker.Clickers.listLength
            for i in range(diff):
                Clicker.Clickers.add()

        def buy():
            if General_Data.money >= Clicker.Clickers.cost:
                General_Data.money -= Clicker.Clickers.cost
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
        level = 0
        value = None
        cost  = None

        def init():
            Button.Dict["Clicker.click"] = Button(550,100,150,150,pr.RED,"click me", Clicker.click)
            Button.Dict["Clicker.Damage.buy"] = Button(20,150,50,20,pr.BLUE, "", Clicker.Damage.buy)

        def updateClass():
            Clicker.Damage.value = Clicker.Damage.level + 1
            Clicker.Damage.cost = 10 * (2 ** Clicker.Damage.level)
            Button.Dict["Clicker.Damage.buy"].name = f"{Clicker.Damage.cost:,}" + ": click damage +1"

        def buy():
            if General_Data.money >= Clicker.Damage.cost:
                General_Data.money -= Clicker.Damage.cost
                Clicker.Damage.upgrade()
                
            
        def upgrade():
                Clicker.Damage.level += 1
                Clicker.Damage.updateClass()

                
    class Speed:
        level = 0
        cost = None
        clicks_per_second = None
        frames_per_click = None

        def init():
            Button.Dict["Clicker.Speed.buy"] = Button(20,230,50,20,pr.BLUE, "", Clicker.Speed.buy)

        def updateClass():
            Clicker.Speed.clicks_per_second = (Clicker.Speed.level + 1)
            Clicker.Speed.cost = 1000 * 2**Clicker.Speed.level
            Clicker.Speed.frames_per_click = General_Data.FRAMES_PER_SECOND / Clicker.Speed.clicks_per_second
            Button.Dict["Clicker.Speed.buy"].name = f"{Clicker.Speed.cost:,}: cps +1" 

        def buy():
            if General_Data.money >= Clicker.Speed.cost:
                General_Data.money -= Clicker.Speed.cost
                Clicker.Speed.upgrade()

        def upgrade():
            Clicker.Speed.level += 1
            Clicker.Speed.updateClass()

            
    class Visuals:
        color = pr.WHITE
        dimentions = pr.Vector2(14,21)
        padding = 5

        def __init__(self, x, y):
            self.position = pr.Vector2(x,y)
            self.homePosition = pr.Vector2(x,y)
            self.triangle = Clicker.Visuals.setTriangle(self.position)
 
        def setTriangle(position):
            triangle = [pr.Vector2(position.x, position.y), 
                        pr.Vector2(position.x-Clicker.Visuals.dimentions.x/2, position.y+Clicker.Visuals.dimentions.y), 
                        pr.Vector2(position.x+Clicker.Visuals.dimentions.x/2, position.y+Clicker.Visuals.dimentions.y)]
            return triangle
