
def climbingLeaderboard(ranked, player):
    result = []
    ranked = sorted(list(set(ranked)))
    # player = sorted(player, reverse=True)
    print(ranked)
    print(player)
    n = len(ranked)
    counter = 0
    for i in range(len(player)):
        while counter < n and ranked[counter] <= player[i]:
            counter += 1
        result.append(n-counter+1)
    return result

# print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))

# def climbingLeaderboard(ranked, player):
#     finallist = []
#     ranked = sorted(list(set(ranked)), reverse=True)
#     player = sorted(player, reverse=Tr)
#     print(ranked)
#     rankptr = len(ranked)-1
#     for i in range(len(player)):
#         for j in range(rankptr, -1, -1):
#             if player[i] < ranked[j]:
#                 finallist.append(j+1)
#                 break
#             else:
#                 rankptr-=1
#                 # counter += 1
#                 continue
#     if len(finallist) != len(player):
#         diff = len(player) - len(finallist)
#         for i in range(diff):
#             finallist.append(1)
#         return finallist
#     else:
#         return finallist
# # #
# # print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))
# # print(checker([100,100,50,40,40,20,10], 120))
# # print(checker([100,100,50,40,40,20,10], 50))
#
# import score as sc
# score = sc.scores.replace(' ', ',')
# player = sc.players.replace(' ', ',')
# # def climbingLeaderboard(ranked, player):
# #     finallist = []
# #     counter = 0
# #     ranked = sorted(list(set(ranked)), reverse=True)
# #     player = sorted(player, reverse=True)
# #
# #     print(player)
# #     print(ranked)
# #     for i in range(len(player)):
# #         while counter < len(ranked) and player[i]<ranked[counter]:
# #             counter += 1
# #         finallist.append(counter + 1)
# #     return finallist[::-1]
#
#     # if len(finallist) != len(player):
#     #     diff = len(player) - len(finallist)
#     #     for i in range(diff):
#     #         finallist.append(1)
#     #     return finallist
#     # else:
#     # return finallist
#
#
# # def rank(ranked, j):
# #     counter = 0
# #     ranked.append(j)
# #     ranked = sorted(ranked)
# #     maxi = 0
# #     for i in ranked[::-1]:
# #         if i != maxi:
# #             maxi = i
# #             counter += 1
# #         if i == j:
# #             return counter
#
# # def climbingLeaderboard(ranked, player):
# #     player = player[::-1]
# #     finallist = []
# #     cur = [[] for i in range(len(player))]
# #     for i in range(len(player)):
# #         cur[i] = checker(ranked.copy(), player[i])
# #         val = rank(cur[i], player[i])
# #         finallist.append(val)
# #     return finallist[::-1]
# #
# # def checker(ranked, singleScore):
# #     counter=0
# #     for i in range(len(ranked)):
# #         if singleScore >= ranked[i]:
# #             break
# #         else:
# #             counter += 1
# #             continue
# #     ranked.insert(counter, singleScore)
# #     return ranked
# #
# # def rank(ranked, j):
# #     counter = 0
# #     # counterlist = []
# #     maxi = 0
# #     for i in ranked:
# #         if i != maxi:
# #             maxi = i
# #             counter += 1
# #         if i == j:
# #             return counter
# print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))
#
# # print(climbingLeaderboard(list(score), list(player)))
# # print(rank([100,100,50,40,40,20,10], 120))
# # print(checker([100,100,50,40,40,20,10], 120))
# # print(checker([100,100,50,40,40,20,10], 50))
