class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        result = path.split('/')
        for i in range(len(result)):
            if result[i] == '' or result[i] == '.':
                continue
            elif result[i] == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(result[i])

        result = "/".join(stack)
        return "/" + result