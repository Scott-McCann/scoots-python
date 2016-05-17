# def get_factors(num):
#     Factors = []
#     Factors.append(tuple([1, num]))
#     if num%2 == 0:
#         half = num//2
#         Factors.append(tuple([2, half]))
#         if num%3 == 0:
#             third = num//3
#             Factors.append(tuple([3, third]))
#             if num%4 == 0:
#                 quarter = num//4
#                 Factors.append(tuple([4, quarter]))
#                 if num%5 == 0:
#                     fifth = num//5
#                     Factors.append(tuple([5, fifth]))
#     return Factors
#
# a = get_factors(15)
#
# print(a)


def factors(num):
    Factors = []
    for x in range(1, num):
        if num % x == 0:
            factor = num//x
            Factors.append(tuple([x, factor]))
            if tuple([factor, x]) in Factors:
                Factors.pop()

    return Factors

b = factors(1000)
print(b)
