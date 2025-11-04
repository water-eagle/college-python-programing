"""
[실습1]
그림판에서 사용자로부터
도형종류(0~8입력, 3~8각형,원:0, 1.2,7를 입력하면 오류메시지출력), 크기,
어떤 색깔로 그릴 지(1,red 2:yellow 3:blue, 4: green, 5: black) 물어보고
요구사항에 맞게 화면의 중앙에 그리기 (if문, for, list사용하기)

그림판을 띄우고 그림...
"""

import turtle as t

# 사용자에게 몇 각형 그릴지 물어보기
t.up()
t.goto(-100, 200)
t.down

n = int(input("몇 각형을 그릴까요? (0은 원 그리기, ): "))  # 각형 입력 받기
if n == 1 or n == 2 or n == 7:  # 1, 2, 7예외 처리
    print("잘못된 입력값입니다")
    exit()

size = int(input("크기를 얼마로 할까요? : "))  # 크기 입력 받기

color = int(
    input("어떤 색깔로 그릴까요?\n(1,red 2:yellow 3:blue, 4: green, 5: black):  ")
)

if color == 1:
    color = "red"
elif color == 2:
    color = "yellow"
elif color == 3:
    color = "blue"
elif color == 4:
    color = "green"
elif color == 5:
    color = "black"
t.color = color

# 다각형 그리기
if n == 0:
    t.circle(size)
else:
    t.reset()
    angle = 360 / n
    t.up()
    t.goto(0, -200 + size)
    t.down
    for i in range(n):
        t.fd(100 + size)
        t.right(angle)

t.write("프로그램을 종료합니다.")
t.done()
