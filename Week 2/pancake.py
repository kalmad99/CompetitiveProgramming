def pancakeSort(self, arr: List[int]) -> List[int]:
    counter = len(arr)
    initial = arr.copy()
    finalist = []
    steps = []
    while counter >= 1:
        temp = self.flip(arr, self.findmax(arr))
        steps.append(self.findmax(arr)+1)
        arr = self.flip(temp, counter-1)
        steps.append(counter)
        finalist.append(arr[-1])
        arr = arr[:counter-1]
        counter-=1
    if finalist[::-1] == initial:
        return []
    else:
        return steps


def flip(self, arr, i):
    temp = arr[:i+1][::-1] + arr[i+1:]
    return temp


def findmax(self, arr):
    counter = 0
    maxi = 0
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
            counter = i
    return counter
