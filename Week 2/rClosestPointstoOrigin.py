def kClosest(points, K):
    coordinates = {}
    result = [[] for i in range(K)]
    for i in range(len(points)):
        # distance = sqrt((points[i][0]-0)**2 + (points[i][1]-0)**2)
        distance = (points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2
        coordinates[(points[i][0], points[i][1])] = distance

    sort_orders = sorted(coordinates.items(), key=lambda x: x[1])

    for i in range(K):
        result[i] = sort_orders[i][0]

    return result


# print(kClosest([[1,3],[-2,2]], 1))
# print(kClosest([[3,3],[5,-1],[-2,4]], 2))
