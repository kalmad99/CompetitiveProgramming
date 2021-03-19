class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        counter, left, right, total = 0,0,0,0
        while right < len(s):
            if total + abs(ord(s[right])-ord(t[right])) <= maxCost:
                total += abs(ord(s[right])-ord(t[right]))
                counter += 1
            else:
                total -= abs(ord(s[left])-ord(t[left]))
                total += abs(ord(s[right])-ord(t[right]))
                left += 1
            right+=1
        return counter