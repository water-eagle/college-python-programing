# [실습2] P.143 주사위던지기 게임 완성하기
import random as r

print("주사위 던지기 게임을 시작합니다.")
dice = r.randrange(1, 6)
if dice == 1:
    print("1")
elif dice == 2:
    print("2")
elif dice == 3:
    print("3")
elif dice == 4:
    print("4")
elif dice == 5:
    print("5")
else:
    print("6")
