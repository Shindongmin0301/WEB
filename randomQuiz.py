from random import *
users = range(1,21)
users = list(users)
shuffle(users)
winner = sample(users,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 1명 : {}".format(winner[0] ))
print("치킨 당첨자 1명 : {}".format(winner[1:]))
print("-- 당첨자 모두 축하드립니다!--")







