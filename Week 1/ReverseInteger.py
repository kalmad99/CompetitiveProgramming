import math


class Solution:
    def reverse(self, x: int) -> int:
        # case 1
        num = x
        num = abs(num)
        num = int(str(num)[::-1])
        if num>=(-2**31) and num<(2**31):
            if x>=0:
                return num
            else:
                return num * -1
        else:
            return 0

        return int(num)

        # case 2
#         num = x
#         num = abs(num)
#         counter = len(str(num))-1
#         total = 0
#         while num!=0:
#             total += (num%10) * (10**counter)
#             num//=10
#             counter-=1

#         if total>=(-2**31) and total<(2**31):
#             if x>=0:
#                 return total
#             else:
#                 return total * -1
#         else:
#             return 0

        # case 3
#         if x>0 and x<2**31:
#             num = x
#         elif x<0 and x>=(-2**31):
#             num = x*-1
#         else:
#             return 0
#         final = ""
#         while num!=0:
#             final += str(num%10)
#             num//=10

#         if int(final)>=(-2**31) and int(final)<(2**31):
#             if x>=0:
#                 return int(final)
#             else:
#                 return ((int(final)) * -1)
#         else:
#             return 0
