def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# print(fib(3))
# print(fib(10))
# print(fib(30))