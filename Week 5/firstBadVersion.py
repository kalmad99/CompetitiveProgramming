class Solution:
    def firstBadVersion(self, n):
        return self.binaryIte(n)
        # return self.binaryRec(0, n)

    def binaryIte(self, nums):
        left = 0
        right = nums-1
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid) == True:
                right = mid-1
            if isBadVersion(mid) == False:
                left = mid + 1
        return left

    # def binaryRec(self, left, right):
    #     mid = (left + right)//2
    #     if left <= right:
    #         if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
    #             return mid
    #         elif isBadVersion(mid) == False:
    #             return self.binaryRec(mid+1, right)
    #         else:
    #             return self.binaryRec(left, mid-1)