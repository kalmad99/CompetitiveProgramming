def isValid(s: str):
    pair = {']': '[', '}': '{', ')': '('}
    stack = []
    for i in s:
        if i in pair:
            if stack:
                top = stack.pop()
            else:
                top = ''
            if pair[i] != top:
                return False
        else:
            stack.append(i)
    return not stack

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))