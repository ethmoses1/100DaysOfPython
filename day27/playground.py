def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(6, 7, 8, 10))


def calculate(**kwargs):
    for key,value in kwargs.items():
        print(key, value)
        

print(calculate(add=5, multiply=2))