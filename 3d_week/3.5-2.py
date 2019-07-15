"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными: Crimes.csv
"""

from collections import Counter as Count
import csv

# var 1:
with open('Crimes.csv') as f:
    data = csv.reader(f)
    print(Count(row[5] for row in data if '2015' in row[2]))


crimes = [row[5] for row in csv.reader(open('Crimes.csv'))]
print(max(set(crimes), key=lambda x: crimes.count(x)))


# var 2:
with open('Crimes.csv') as fi:
    reader = csv.reader(fi)
    next(reader)
    crime_cnt = dict()
    for row in reader:
        year = row[2][6:10]
        if year == '2015':
            crime_type = row[5]
            if crime_type not in crime_cnt:
                crime_cnt[crime_type] = 0
            crime_cnt[crime_type] += 1

a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
a.sort(key=lambda x: -x[0])

print(a[0][1])
