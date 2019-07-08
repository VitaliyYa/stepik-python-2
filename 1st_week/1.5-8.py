class MoneyBox:
    def __init__(self, capacity):
        """
        конструктор с аргументом – вместимость копилки
        """
        self.capacity = capacity
        self.value = 0

    def can_add(self, v):
        return self.value + v <= self.capacity

    def add(self, v):
        self.value += v
