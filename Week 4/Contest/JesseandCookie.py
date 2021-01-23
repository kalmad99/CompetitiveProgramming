import heapq

def cookies(k, A):
    heapq.heapify(A)
    counter = 0
    while len(A) > 1 and A[0] < k:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        heapq.heappush(A, 1*first + 2*second)
        counter+=1
    if A[0] < k:
        return -1
    return counter
