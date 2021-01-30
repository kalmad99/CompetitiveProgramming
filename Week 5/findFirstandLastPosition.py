class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        cur = self.binaryite(nums, target)
    
        res = []
        
        first = nums[:cur]
        second = nums[cur+1:]
        
        end = cur
        start = cur
            
        for i in range(len(first)):
            if first[i] == target:
                start = i
                break
            else:
                continue
                
        for i in range(len(second)):
            if second[i] == target:
                end += 1
            else:
                continue
        
        res.append(start)
        res.append(end)
        return res
        
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
