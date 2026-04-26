 # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
import time

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

n = 7
start_time = time.time()

result = fibonacci(n)
run_time = time.time() - start_time

print(f'Fib({n}): {result:,}')
print(f'\n--- Run time: {run_time:.3f}s ---')
