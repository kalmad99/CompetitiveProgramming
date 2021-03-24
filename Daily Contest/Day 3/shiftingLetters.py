class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        total = []
        counter = 0
        result = ""
        for i in range(len(S)-1, -1, -1):
            counter += shifts[i]
            total.append(counter)
        total = total[::-1]
        print(total)
        print(ord('l'))
        for i in range(len(S)):
            result += chr(((ord(S[i]) + (total[i])-123)%26) + 97)
        return result