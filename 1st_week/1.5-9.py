class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = list()

    def add(self, *a):
        # добавить следующую часть последовательности
        for value in a:
            self.lst.append(value)

        while len(self.lst) >= 5:
            s = 0
            for i in range(5):
                s += self.lst.pop(0)
            print(s)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.lst
