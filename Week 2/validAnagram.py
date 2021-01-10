def counting(t):
    counter = []
    output = [0 for i in range(len(t))]
    ans = ["" for i in range(len(t))]

    for i in range(256):
        counter.append(0)

    for i in t:
        counter[ord(i)] += 1

    for i in range(1, 256):
        counter[i] += counter[i - 1]

    for i in range(len(t)):
        output[counter[ord(t[i])] - 1] = t[i]
        counter[ord(t[i])] -= 1
    for i in range(len(t)):
        ans[i] = output[i]

    return ans


def isAnagram(s, t):
    first = counting(t)
    second = counting(s)

    if first == second:
        return True
    else:
        return False


# print(isAnagram("anagram", "nagaram"))
# print(isAnagram("rat","car"))