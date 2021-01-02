num1 = input("First number :")
num2 = input("Second number:")

def summation(first, second):
    counter = 1
    carry = 0
    total = ""

    if len(first) < len(second):
        maxnum = len(second)
        first = first[::-1] + (len(second)-len(first))*"0"
        first = first[::-1]
    else:
        maxnum = len(first)
        second = second[::-1] + (len(first) - len(second)) * "0"
        second = second[::-1]

    while counter <= maxnum:
        summ = int(first[(counter * -1)]) + int(second[(counter * -1)])
        if summ > 9 and counter != maxnum:
            total += str(((int(first[(counter*-1)]) + int(second[(counter*-1)]) + carry)%10))
            carry = 1
            summ //= 10
        elif summ<=9 and counter!= maxnum:
            total += str((int(first[(counter*-1)]) + int(second[(counter*-1)]) + carry))
            carry = 0
            summ //= 10
        else:
            total += str(summ+carry)[::-1]
        counter+=1

    return total[::-1]

print(summation(num1, num2))