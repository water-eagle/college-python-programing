"""
3. 다각형을 그리는 함수를 정의하기. 한변의 길이, 중심 좌표, 색깔, 다각형 그리는 횟수를 랜덤으로 생성해서 다양한 크기, 색깔의 다각형그리기
"""

import random
import turtle


def choice_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    return random.choice(colors)


def draw_polygon(sides, length, color):
    angle = 360 / sides
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()


if __name__ == "__main__":
    repeat = random.randint(1, 10)
    for i in range(repeat):
        square_length = random.randint(1, 20)
        for j in range(4):
            square(square_length)


# elif shape == "원":

# 자동차가 창 중심에 있도록 펜촉을 이동한다.

# 자동차 몸체 색상을 body_color로 지정하고, 채우기 시작하고, 몸체를 그린다.
# t.fillcolor(body_color)
# t.begin_fill()
