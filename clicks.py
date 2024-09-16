from general_datas import General_Data

class Click:
    level = 1
    value = None
    cost  = None

    @classmethod
    def update(cls):
        cls.value = cls.level
        cls.cost = 10 * (2 ** cls.level)

    def click():
        General_Data.money += Click.value
        
    def upgrade():
        if General_Data.money >= Click.cost:
            General_Data.money -= Click.cost
            Click.level += 1
            Click.update()
        #    List[1].name = str(Click.cost) + ": click damage +1"
        #   used to change button name; will figure this out later


