"""
# Lab: 사각형을 그리는 함수 작성하기

정사각형을 그리는 함수는 다음과 같다.
def square(x, y, length):    # length는 변의 길이
    t.up()                	# 펜을 든다.
    t.goto(x, y)        	# (x, y)으로 이동한다.
    t.down()           		 # 펜을 내린다.

    for i in range(4):
        t.forward(length)
        t.left(90)

위의 함수를 호출하여 3개의 정사각형을 그려 보자.
"""

import turtle as t


def square(x, y, length):  # length는 한변의 길이
    t.up()  # 펜을 든다.
    t.goto(x, y)  # (x, y)으로 이동한다.
    t.down()  # 펜을 내린다.

    for i in range(4):
        t.forward(length)
        t.left(90)


square(-200, 0, 100)  # square() 함수를 호출한다.
square(0, 0, 100)
square(200, 0, 100)
t.done()
