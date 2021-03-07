class Solution:
    def maxArea(self, height) -> int:
        i,j = 0, len(height)-1
        maxi, width, area = 0, 0, 0
        while i < j:
            width = j-i
            if height[i] < height[j]:
                res = width * height[i]
                i+=1
            else:
                res = width * height[j]
                j-=1
            if res > maxi:
                maxi = res
        return maxi