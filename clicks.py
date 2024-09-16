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
