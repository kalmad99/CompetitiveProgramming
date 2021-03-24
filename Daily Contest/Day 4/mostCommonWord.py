class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        res = {}
        for i in paragraph:
            if i.isalpha() or i==" ":
                continue
            else:
                paragraph = paragraph.replace(i, " ")
        print(paragraph)
        sentence = paragraph.lower().split(" ")
        for i in sentence:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)
        for i in sorted_res:
            if i[0] not in banned and i[0]!= "":
                return i[0]