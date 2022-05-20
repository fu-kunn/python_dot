# def double(n):
#     return n * 2

# def triple(n):
#     return n * 3

def calc(n, func):
    return func(n)

print(calc(10, lambda n: n * 2))
print(calc(10, lambda n: n * 3))