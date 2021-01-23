def matchingStrings(strings, queries):
    counter = [0 for _ in range(len(queries))]
    for i in range(len(queries)):
        for j in range(len(strings)):
            if strings[j] == queries[i]:
                counter[i] += 1
    return counter