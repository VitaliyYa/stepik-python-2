"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
"""


import sys
import re


for line in sys.stdin:
    line = line.strip()
    if re.search(r'z...z', line):
        print(line)
