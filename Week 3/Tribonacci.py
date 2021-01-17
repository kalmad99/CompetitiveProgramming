def tribonacci(n):
    #recursive
    # if n==0:
    #     return 0
    # elif n<=2 and n>0:
    #     return 1
    # else:
    #     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

    #iterative
    if n < 2:
        return n
    elif n == 2:
        return 1
    first = 0
    second = 1
    third = 1
    total = 0
    for i in range(2, n):
        total = first + second + third
        first = second
        second = third
        third = total
    return total

print(tribonacci(37))
