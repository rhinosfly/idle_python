import pyray as pr
from general_datas import General_Data
from buttons import Button

class Click:
    level = 1
    value = None
    cost  = None

    def init():
        Click.update()
        Button.Dict["clickMe"] = Button(550,100,150,150,pr.RED,"click me", Click.click)
        Button.Dict["upgradeClick"] = Button(20,150,50,20,pr.BLUE, "20: click damage +1", Click.upgrade)

    def update():
        Click.value = Click.level
        Click.cost = 10 * (2 ** Click.level)

    def click():
        General_Data.money += Click.value
        
    def upgrade():
        if General_Data.money >= Click.cost:
            General_Data.money -= Click.cost
            Click.level += 1
            Click.update()
            Button.Dict["upgradeClick"].name = str(Click.cost) + ": click damage +1"
