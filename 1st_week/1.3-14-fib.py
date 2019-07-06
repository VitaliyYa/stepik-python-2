"""
Рекурсивная функция, на примере послдовательности Фиббоначи
"""


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


y = fib(5)
print(y) # 8
