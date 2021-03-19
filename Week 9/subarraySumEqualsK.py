class Solution:
    def subarraySum(self, nums, k: int) -> int:
        total = {0: 1}
        result = 0
        counter = 0
        for i in nums:
            result += i
            if result - k in total:
                counter += total[result - k]

            if result in total:
                total[result] += 1
            else:
                total[result] = 1
        return counter