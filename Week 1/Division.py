num1 = input("First Number: ")
num2 = input("Second Number:")


def division(dividend, divisor):
    first = str(abs(int(dividend)))
    second = str(abs(int(divisor)))
    ans = ""
    carry = 0
    current = 0
    for i in range(len(first)):
        current = int(first[i]) + (carry * 10)
        ans += str(current//int(second))
        carry = current % int(second)

    if carry == 0:
        ans = int(ans)
    else:
        rem = float(carry/int(second))
        ans = float(ans) + float(rem)

    if (int(divisor) >=0 and int(dividend) >= 0) or (int(dividend) < 0 and int(divisor) < 0):
        return float("{:.3f}".format(ans))
    else:
        return float("{:.3f}".format(ans))*-1


print(division(num1, num2))