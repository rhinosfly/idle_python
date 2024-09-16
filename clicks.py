class Click:
    level = 1
    value = None
    cost  = None

    @classmethod
    def update(cls):
        cls.value = cls.level
        cls.cost = 10 * (2 ** cls.level)
