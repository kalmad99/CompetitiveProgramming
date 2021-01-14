def twoStacks(x, a, b):
    for a_index, value in enumerate(a):
        if value > x:
            a_index -= 1
            break
        x -= value
    max_picks = a_index + 1
    # try filling b removing from a when necessary
    for b_index, value in enumerate(b):
        while value > x and a_index >= 0:
            x += a[a_index]
            a_index -= 1
        if value > x:
            return max_picks
        max_picks = max(max_picks, b_index + a_index + 2)
        x -= value
    return max_picks

# print(twoStacks(10, [4, 2, 4, 6, 1], [2, 1, 8, 5]))









# def GOTS(tot, a, b):
#     stacka = []
#     stackb = []
#     finalstack = []
#     totala = 0
#     totalb = 0
#     indexa = 0
#     indexb = 0
#     counter = 0
#     result = 0
#     fora = 0
#     forb = 0
#     for i in a:
#         totala += int(i)
#         stacka.append(totala)
#     for j in b:
#         totalb += int(j)
#         stackb.append(totalb)
#
#     for i in range(len(stacka)):
#         if stacka[i]<=10:
#             indexa += 1
#             continue
#         else:
#             break
#
#     for j in range(len(stackb)):
#         if stackb[j]<=10:
#             indexb += 1
#             continue
#         else:
#             break
#
#     fora = (int(stacka[indexa-1]))/(indexa)
#     forb = (int(stackb[indexb-1]))/(indexb)
#
#     if fora < forb:
#         counter = fora
#         for k in range(len(stackb)):
#             result += b[k] + stacka[int(fora)]
#             if result <= 10:
#                 counter+=1
#     elif fora > forb:
#         counter = forb
#         for k in range(len(stacka)):
#             result += a[k] + stackb[int(forb)]
#             if result <= 10:
#                 counter+=1
#
#     return counter+1

