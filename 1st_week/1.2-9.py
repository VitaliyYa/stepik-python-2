"""
переменная objects только для локального запуска, в поле решения задачи на степике вставлять только решение.
"""
objects = [1, 2, 3, True, [12], 'as', 2, 3, 1]

# solve:
ans = 0

s = set()
for obj in objects:
    i = id(obj)
    if i not in s:
        ans += 1
        s.add(i)

print(ans)

# Или решения в одну строку:

print(len(set(map(id, objects))))

print(len(set(id(i) for i in objects)))