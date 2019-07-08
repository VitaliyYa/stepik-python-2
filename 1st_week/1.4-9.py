def create(namespace, parent):
    global namespaces
    l = namespaces.get(parent, False)
    if not l:
        namespaces[parent] = list()
        l = namespaces[parent]
    l.append(namespace)


def add(namespace, var):
    global variables
    l = variables.get(namespace, False)
    if not l:
        variables[namespace] = list()
        l = variables[namespace]
    l.append(var)


def get(namespace, var):
    global variables
    global namespaces
    result = None
    l = variables.get(namespace, False)
    if not l or var not in l:
        for key, value in namespaces.items():
            if namespace in value:
                result = get(key, var)
    else:
        result = namespace
    return result


def handle(request):
    global result
    command, arg1, arg2 = map(str, request.split())
    if command == 'create':
        create(arg1, arg2)
    elif command == 'add':
        add(arg1, arg2)
    elif command == 'get':
        result.append(get(arg1, arg2))


namespaces = {}
variables = {}

result = []

n = int(input())

for i in range(n):
    handle(input())

for r in result:
    print(r)
