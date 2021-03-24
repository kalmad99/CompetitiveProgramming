from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, total = 0, 1, 0
        while right < len(prices) and left < len(prices):
            if prices[right] > prices[left]:
                total += prices[right] - prices[left]
            right += 1
            left += 1
        return total