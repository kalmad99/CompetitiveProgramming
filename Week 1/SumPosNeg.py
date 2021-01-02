
num1 = input("First number :")
num2 = input("Second number:")

def summation(first, second):
    counter = 1
    carry = 0
    total = ""
    numl1 = first
    numl2 = second
    put1 = ""
    put2 = ""

    if len(first) < len(second):
        maxnum = len(str(abs(int(second))))
        diff = len(str(abs(int(second)))) - len(str(abs(int(first))))
        numl1 = str(abs(int(first)))[::-1] + (diff * "0")
        numl1 = numl1[::-1]
    else:
        maxnum = len(str(abs(int(first))))
        diff = len(str(abs(int(first)))) - len(str(abs(int(second))))
        numl2 = str(abs(int(second)))[::-1] + (diff * "0")
        numl2 = numl2[::-1]

    print("Num1 " + str(numl1))
    print("Num2 " + str(numl2))

    while counter <= maxnum:
        if (int(first) < 0 and int(second) < 0):
            summ = int(numl1[counter*-1]) + int(numl2[counter*-1]) + carry
        elif (int(first) >= 0 and int(second) < 0):
            res = str((10 ** len(str(abs(int(numl2)))) - int(abs(int(second)))))
            numl2 = res
            summ = int(numl1[counter * -1]) + int(numl2[counter * -1]) + carry
        elif(int(first) < 0  and int(second) >= 0):
            res = str((10 ** len(str(abs(int(numl1)))) - int(abs(int(first)))))
            numl1 = res
            summ = int(numl2[counter * -1]) + int(numl1[counter * -1]) + carry
        else:
            summ = int(numl1[counter*-1]) + int(numl2[counter*-1]) + carry


        if summ > 9 and counter != maxnum:
            total += str((summ)%10)
            carry = 1
        elif summ<=9 and counter!= maxnum:
            total += str(summ)
            carry = 0
        else:
            total += str(summ)[::-1]

        # print("Num1 last digit " + numl1[counter * -1])
        # print("Num2 last digit " + numl2[counter * -1])
        counter+=1


    if (int(first) < 0 and int(second) < 0):
        return str(-1*(int(total[::-1])))
    elif (int(first) >= 0 and int(second) >= 0):
        return total[::-1]
    elif(int(first) < 0  and int(second) > 0):
        if abs(int(first))>=abs(int(second)):
            return str(int(total[::-1]) - 10**len(total))
        else:
            return total[::-1]
    else:
        if abs(int(second))>=abs(int(first)):
            return str(int(total[::-1]) - 10**len(numl2))
        else:
            # total[-1] = 0
            return str(int(total))

print(summation(num1, num2))


# num1 = input("First number :")
# num2 = input("Second number:")
#
# def summation(first, second):
#     counter = 1
#     carry = 0
#     total = ""
#     num1 = first
#     num2 = second
#     if len(first) < len(second):
#         maxnum = len(second)
#         if (int(first) >= 0 and int(second)>=0) or (int(first) <= 0 and int(second)<=0):
#             num1 = abs(int(first))[::-1] + (len(second) - len(first)) * "0"
#             num1 = num1[::-1]
#         elif (int(first) < 0 and int(second)>0):
#             num1 = abs(int(first))[::-1] + (len(second) - len(first)) * "0"
#             num1 = num1[::-1]
#         else:
#             num2 = abs(int(second))[::-1] + (len(second) - len(first)) * "0"
#             num2 = num2[::-1]
#
#
#
#     else:
#         maxnum = len(first)
#         if (int(first) >= 0 and int(second)>=0) or (int(first) <= 0 and int(second)<=0):
#             num1 = abs(int(first))[::-1]
#             num2 = abs(int(second))[::-1] + (len(second) - len(first)) * "0"
#             num2 = num2[::-1]
#         elif (int(first) < 0 and int(second)>0):
#             num2 = second[::-1]
#             num1 = abs(int(first))[::-1] + (len(second) - len(first)) * "0"
#             num1 = num1[::-1]
#         else:
#             num2 = abs(int(second))[::-1] + (len(second) - len(first)) * "0"
#             num1 = first[::-1]
#             num2 = num2[::-1]
#
#         # second = second[::-1] + (len(first) - len(second)) * "0"
#         # second = second[::-1]
#
#     while counter <= maxnum:
#         if (int(first) < 0 and int(second) < 0) or (int(first) >= 0 and int(second) >= 0):
#             # summ = int(abs(int(first[(counter * -1)]))) + int(abs(int(second[(counter * -1)])))
#             summ = num1[counter*-1] + num2[counter*-1]
#         elif (int(first) < 0 and int(second) > 0):
#             summ = int(num1)*-1 + num2[counter*-1]
#             summ = (-1 * int(abs(int(first))[(counter * -1)])) + int(second[(counter * -1)])
#         else:
#             summ = int(abs(int(second[(counter * -1)]))) - int(first[(counter * -1)])
#
#         if summ > 9 and counter != maxnum:
#             total += str(((int(first[(counter*-1)]) + int(second[(counter*-1)]) + carry)%10))
#             carry = 1
#             summ //= 10
#         elif summ<=9 and counter!= maxnum:
#             total += str((int(first[(counter*-1)]) + int(second[(counter*-1)]) + carry))
#             carry = 0
#             summ //= 10
#         else:
#             total += str(summ+carry)[::-1]
#         counter+=1
#
#     return total[::-1]
#
# print(summation(num1, num2))
