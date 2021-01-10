def relativeSortArray(arr1, arr2):
    conta = []
    notconta = []
    output = []
    counter = [0 for i in range(1000)]

    for i in arr1:
        if i in arr2:
            conta.append(i)
        else:
            notconta.append(i)
    for i in arr2:
        for j in conta:
            if j == i:
                output.append(j)

    output2 = [0 for i in range(len(notconta))]

    for i in range(1001):
        counter.append(0)

    for i in notconta:
        counter[i] += 1

    for i in range(1, 1001):
        counter[i] += counter[i - 1]

    for i in range(len(notconta)):
        output2[counter[notconta[i]] - 1] = notconta[i]
        counter[notconta[i]] -= 1

    for i in output2:
        output.append(i)
    return output

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))