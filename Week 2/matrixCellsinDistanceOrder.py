def allCellsDistOrder(R, C, r0, c0):
    row = []
    coordinates = {}
    matrix = []
    for i in range(R):
        for j in range(C):
            row.append(i)
            row.append(j)
            matrix.append(row)
            row = []
    result = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        distance = abs(matrix[i][0] - r0) + abs(matrix[i][1] - c0)
        coordinates[(matrix[i][0], matrix[i][1])] = distance

    sort_orders = sorted(coordinates.items(), key=lambda x: x[1])

    for i in range(len(matrix)):
        result[i] = sort_orders[i][0]

    return result


# print(allCellsDistOrder(1, 2, 0, 0))
# print(allCellsDistOrder(2, 2, 0, 1))
# print(allCellsDistOrder(2, 3, 1, 2))
