def evalRPN(tokens):
    stack = []
    operators = ['/', '*', '+', '-']
    for i in range(len(tokens)):
        if tokens[i] not in operators:
            stack.append(tokens[i])
        elif tokens[i] in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            res = perform(int(op1), int(op2), tokens[i])
            stack.append(res)
        else:
            continue
    return stack[0]

def perform(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return int(op1 / op2)

# print(evalRPN(["2", "1", "+", "3", "*"]))
# print(evalRPN(["4", "13", "5", "/", "+"]))
# print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
