"""
Вам дана в архиве файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером. files/sample, files/sample_ans.txt
"""

import os.path

print(os.getcwd())

res = []
for home, dirs, files in os.walk('main'):
    for file in files:
        if file.endswith('.py'):
            r = str(home)
            if r not in res:
                res.append(r)

res.sort()

out_file = 'files/ans_2-4-6.txt'
with open(out_file, 'w') as f:
    for line in res:
        l = line + '\n'
        f.writelines(l)
