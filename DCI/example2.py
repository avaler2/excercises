def add(arg1, arg2):
    return arg1 + arg2

def process(n):
    x = 100
    print(n)
    print(x)
    value = add(n, x)
    return value

print(process(12))