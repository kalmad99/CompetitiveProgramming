class Solution:
    def minIncrementForUnique(self, A) -> int:
        A.sort()
        prev = 0
        result = 0

        for i in range(len(A)):
            while (prev < A[i]):
                prev += 1

            result += prev - A[i]
            prev += 1

        return result
