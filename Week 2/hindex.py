def hIndex(self, citations: List[int]) -> int:
        # cita = sorted(citations)
        # hidx = 0
        # for i in range(len(cita)-1, -1, -1):
        #     counter = len(cita) - i
        #     if cita[i] >= counter:
        #         hidx = counter
        #     else:
        #         break
        # return hidx

        cita = sorted(citations, reverse=True)
        hidx = 0
        for i in range(len(cita)):
            counter = i+1
            if cita[i] >= counter:
                hidx = counter
            else:
                break

        return hidx

print(hIndex([3, 0, 6, 1, 5]))
