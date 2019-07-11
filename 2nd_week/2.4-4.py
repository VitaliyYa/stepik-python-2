"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
"""

# r - read (default)
# w - write
# a - append
# b - binary
# t - text (default)
# r+ - open file for reading and writing
# w+ - open for reading and writing, the contents of the file is erased


with open('files/dataset_24465_4.txt') as source, open('files/revers.txt', 'w') as target:
    l = []
    for line in source:
        l.append(line.strip())
    l.reverse()
    text = "\n".join(l)
    target.write(text)
