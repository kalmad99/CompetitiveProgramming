from operator import itemgetter, attrgetter
def frequencySort(nums):
    dictionary = {}
    frequencies = []
    for i in nums:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    freq_tuple = sorted(nums, reverse=True)
    res = sorted(freq_tuple, key=lambda x: dictionary[x])
    print(res)

frequencySort([2,3,1,3,2])