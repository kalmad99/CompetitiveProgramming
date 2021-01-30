class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #case 1
        # left = 0
        # right = len(nums)-1
        # return self.binaryrec(nums, left, right, target)
        
        #case 2
        return self.binaryite(nums, target)
       
        #case 3
        # mid = (len(nums)) // 2
        # if len(nums) == 0:
        #     return -1
        # if len(nums) == 1:
        #     if nums[mid] == target:
        #         return mid
        #     return -1
        # elif nums[mid] == target:
        #     return mid
        # elif nums[mid] < target:
        #     res = self.search(nums[mid:], target)
        #     if res != -1:
        #         return mid + res
        #     else:
        #         return -1
        # else:
        #     return self.search(nums[:mid], target)
        
        
    def binaryrec(self, nums, left, right, target):
        mid = (left + right)//2
        if left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binaryrec(nums, mid+1, right, target)
            else:
                return self.binaryrec(nums, left, mid-1, target)
        return -1
    
    def binaryite(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
