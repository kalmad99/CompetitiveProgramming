def maxDepth(s):
    counter = 0
    colist = []
    for i in s:
        if i == '(':
            counter += 1
            colist.append(counter)
        elif i == ')':
            counter -= 1
            colist.append(counter)
        else:
            counter += 0
            colist.append(counter)
    return max(colist)


# print(maxDepth("(1+(2*3)+((8)/4))+1"))
# print(maxDepth("(1)+((2))+(((3)))"))
# print(maxDepth("1+(2*3)/(2-1)"))
# print(maxDepth("1"))