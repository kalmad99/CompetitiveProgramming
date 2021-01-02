# import AddTwoNumbers as A2
num1 = input("First number :")
num2 = input("Second number:")

def multiplication(first, second):
    counter = 0
    total = []
    sum = 0
    sum2 = 0
    numl2 = str(abs(int(second)))

    for i in numl2[::-1]:
        sum += int(i) * int(first)
        total.append(str(sum) + (counter*"0"))
        sum = 0
        counter+=1

    # print(total)
    # for k in range(len(total)):
    #     finall = "0"
    #     finall = A2.summation(finall, total[k])
    #     print(finall)
    #     sum2 += int(finall)
    for k in total:
        sum2 += int(k)

    if int(second) >= 0:
        return sum2
    else:
        return sum2*-1


print(multiplication(num1, num2))
