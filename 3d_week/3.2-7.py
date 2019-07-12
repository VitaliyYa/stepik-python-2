def contain_counter(s, t):
    c = 0
    if t not in s:
        return c
    i = 0
    while True:
        try:
            tar = s[i:]
            if tar.index(t) == 0:
                c += 1
        except:
            if i >= len(s):
                break
        i += 1
    return c


s = input()
t = input()

print(contain_counter(s, t))
