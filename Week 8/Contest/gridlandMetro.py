def gridlandMetro(n, m, k, track):
    available = n * m
    visited = {}
    track.sort()
    for row, start, end in track:
        if row not in visited:
            visited[row] = [[start, end]]
        else:
            counter = 0
            for i in range(len(visited[row])):
                curstart, curend = visited[row][i]
                if start > curend or end < curstart:
                    continue
                else:
                    if curstart >= start:
                        curstart = start
                    if curend <= end:
                        curend = end
                    visited[row][i] = [curstart, curend]
                    counter = 1
            if counter == 0:
                visited[row].append([start, end])

    # print(visited.values())
    for columns in visited.values():
        for start, end in columns:
            available -= (end - start + 1)
    return available
