"""
ch7 - p223
## **Lab: 클릭하는 곳에 사각형 그리기**

- 사용자가 화면에서 마우스 버튼을 클릭한 경우, 클릭 된 위치에 사각형을 그리는 프로그램을 작성해 보자.
앞에서 작성한 square() 함수도 사용한다.
"""

import turtle as t
import random as r


def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


def circle(length):
    t.circle(length)


def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color(r.random(), r.random(), r.random())  # 랜덤 색상 지정
    # square(100)
    circle(100)
    t.end_fill()


s = t.Screen()  # 그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit)  # 마우스 클릭 이벤트 처리 함수를 등록한다.

t.done()
