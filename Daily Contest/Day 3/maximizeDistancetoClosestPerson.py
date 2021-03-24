class Solution:
    def maxDistToClosest(self, seats) -> int:
        ones = []
        maxi = 1
        for i in range(len(seats)):
            if seats[i] == 1:
                ones.append(i)
            else:
                continue

        maxi = max(maxi, ones[0])
        maxi = max(maxi, len(seats) - 1 - ones[-1])
        for i in range(len(ones) - 1):
            maxi = max((ones[i + 1] - ones[i]) // 2, maxi)
        return maxi