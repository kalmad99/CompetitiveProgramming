def perform(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
def prefix(expr):
    stack = []
    newexpr = expr.split(' ')
    operators = ['/', '*', '+', '-']
    for i in range(len(newexpr)-1, -1, -1):
        if newexpr[i] not in operators:
            stack.append(newexpr[i])
        elif newexpr[i] in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            res = perform(int(op1), int(op2), newexpr[i])
            stack.append(res)
        else:
            continue
    return stack[0]

print(prefix('+ 4 * 3 12'))
print(prefix('- + * 2 3 * 5 4 9'))
