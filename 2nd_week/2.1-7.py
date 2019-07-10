def been_catched(error):
    if error in catched:
        return True

    if len(errors[error]):
        return any(map(lambda x: been_catched(x), errors[error]))

    return False


errors = {}

for i in range(int(input())):
    data = input().split(' : ')
    if len(data) == 1:
        data.append("")

    errors[data[0]] = data[1].split()
    for j in errors[data[0]]:
        if j not in errors:
            errors[j] = []

catched = []

for _ in range(int(input())):
    error = input()
    if been_catched(error):
        print(error)
    else:
        catched.append(error)
