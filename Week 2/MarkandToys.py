def maximumToys(prices, k):
    fits = []
    counter = 0
    total = 0
    for i in prices:
        if i <= k:
            fits.append(i)

    fits = sorted(fits)

    while counter < len(fits):
        total += fits[counter]
        if total <= k:
            counter += 1
        else:
            break

        # print(total)
    # return len(fits)
    return counter

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))

