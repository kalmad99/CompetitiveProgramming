def superDigit(n, k):
    total = 0        
    if len(n) == 1:
        return n
    else:
        for i in range(len(n)):
            total += int(n[i])
        total *= k
        curtext = str(total)
        return superDigit(curtext, 1)
