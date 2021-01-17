def minOperations(logs):
    stack = []
    count = 0
    for i in range(len(logs)):
        if logs[i] != "../" and logs[i] != './':
            stack.append(logs[i])
        elif i == './':
            continue
        else:
            if len(stack) > 0 and logs[i] != './':
                stack.pop()
            else:
                continue
    for i in stack:
        count += 1
    return count

# print(minOperations(["d1/","d2/","./","d3/","../","d31/"]))
# print(minOperations(["d1/","d2/","../","d21/","./"]))
# print(minOperations(["d1/","../","../","../"]))