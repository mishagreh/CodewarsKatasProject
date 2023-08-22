from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/57f6051c3ff02f3b7300008b

def meeting(rooms, need):

    if not need:
        return 'Game On'

    x = []
    for i in rooms:
        if sum(x) < need:
            if i[1]-len(i[0]) < 0:
                x.append(0)
            else:
                x.append(i[1]-len(i[0]))

    if sum(x) >= need:
        return x[:-1] + [x[-1] - sum(x) + need]
    return "Not enough!"

# match/case statement solution
#
# def meeting(rooms, need):
#     match not need:
#         case True: return 'Game On'
#         case False:
#
#             x = []
#             for i in rooms:
#                 if sum(x) < need:
#                     match i[1] - len(i[0]) < 0:
#                         case True: x.append(0)
#                         case False: x.append(i[1] - len(i[0]))
#
#             match sum(x) >= need:
#                 case True: return x[:-1] + [x[-1] - sum(x) + need]
#                 case False: return "Not enough!"


rooms, need = [['XXX', 5], ['', 1], ['XXXXX', 3], ['XX', 1], ['', 9], ['XXXXXXX', 10], ['X', 9], ['XXXXXXXXXX', 5],
               ['XXXXX', 7], ['XXXXXXXXXX', 10], ['XXXXXXX', 0], ['XXXX', 8]] , 2
print(meeting(rooms, need))

end = timer()
print(end - start)
