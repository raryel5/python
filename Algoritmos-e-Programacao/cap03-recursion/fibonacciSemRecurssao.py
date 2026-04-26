 # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fib(n):
    a = 0
    b = 1

    for i in range(n):
        tmp = a
        a = b

        b = tmp + b
    
    return a

n = 7
result = fib(n)

print(f'Fib({n}): {result}')
