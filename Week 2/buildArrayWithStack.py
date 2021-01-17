def buildArray(target, n):
    empty = []
    for i in range(1, target[-1]+1):
        if i in target:
            empty.append('Push')
        else:
            empty.append('Push')
            empty.append('Pop')
    return empty


print(buildArray([1,2,3], 3))
print(buildArray([1,2], 4))
print(buildArray([2,3,4], 4))
print(buildArray([1,3,4,6,7,8], 9))
