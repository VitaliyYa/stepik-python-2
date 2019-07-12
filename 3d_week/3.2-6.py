def replace_counter(s, a, b):
    if (a in s) and (a in b):
        return 'Impossible'

    i = 0
    while a in s:
        s = s.replace(a, b)
        i += 1

    return i


s = input()
a = input()
b = input()

print(replace_counter(s, a, b))
