class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        change, prev, total, i = 0, 0, 0, 0
        while i < len(s) and prev <= i:
            if total + (abs(ord(s[i]) - ord(t[i]))) <= maxCost:
                total += (abs(ord(s[i]) - ord(t[i])))
                change += 1
            else:
                total -= abs(ord(s[prev]) - ord(t[prev]))
                total += abs(ord(s[i]) - ord(t[i]))
                prev += 1
            i += 1
        return change
