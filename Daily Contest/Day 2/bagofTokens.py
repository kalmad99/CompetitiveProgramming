from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        score = 0
        res = 0
        sortedTokens = deque(sorted(tokens))
        while len(sortedTokens) > 0:
            if sortedTokens[0] <= P:
                score += 1
                res = score
                P -= sortedTokens.popleft()
            else:
                if score > 0:
                    P += sortedTokens.pop()
                    score -= 1
                else:
                    return res
        return res