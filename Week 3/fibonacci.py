def fib(n: int) -> int:
    #recursive
    """
    much slower but concise
    """
    # if n <= 1:
    #     return n
    # else:
    #     return fib(n - 1) + fib(n - 2)

    #iterative
    """
    much faster but longer
    """
    if n <= 1:
        return n
    else:
        first = 0
        second = 1
        for i in range(1, n):
            result = first + second
            first = second
            second = result
        return result


print(fib(3))
print(fib(10))
# print(fib(57))