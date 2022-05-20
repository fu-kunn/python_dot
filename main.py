def double(n):
    return n * 2

def triple(n):
    return n * 3

def calc(n, func):
    return func(n)

print(calc(10, double))
print(calc(10, triple))