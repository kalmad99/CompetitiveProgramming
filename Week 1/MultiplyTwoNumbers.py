import A2SV1 as A2

def multiplication(first, second):
    counter = 0
    total = []
    sum = 0
    sum2 = 0

    for i in second[::-1]:
        sum += int(i) * int(first)
        total.append(str(sum) + (counter*"0"))
        sum = 0
        counter+=1

    for k in range(len(total)):
        finall = "0"
        finall = A2.summation(str(finall), total[k])
        sum2 += int(finall)
    print(sum2)

multiplication(A2.num1, A2.num2)
