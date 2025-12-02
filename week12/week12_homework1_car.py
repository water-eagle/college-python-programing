"""
자동차 5대 경주 애니메이션 코딩하기(turtle module이용), 코드 줄단위 주석달기
"""

import random
from turtle import *

register_shape("car2.gif")  # 자동차 이미지 등록


class Car:
    def __init__(
        self, speed, fname, start_x, start_y
    ):  # 속도, 이미지 파일 이름(fname), x,y 좌표를 매개변수로 받음
        self.speed = speed
        self.turtle = Turtle()
        self.turtle.hideturtle()  # 초기에는 거북이(자동차) 숨김
        self.turtle.shape(fname)  # 자동차 이미지로 모양 설정
        self.turtle.speed(self.speed)  # 거북이(자동차) 속도 설정
        self.turtle.penup()  # 펜을 들고 이동 준비
        self.turtle.goto(start_x, start_y)  # 시작 위치로 이동
        self.turtle.pendown()  # 펜을 내리고 그리기 준비
        self.turtle.showturtle()  # 거북이(자동차) 보이기

    def drive(self, distance):  # distance만큼 전진하는 메서드
        self.turtle.forward(distance)

    """
    def turnleft(self, degree):  # degree만큼 왼쪽으로 회전하는 메서드
        self.turtle.left(degree)
    """


car_list = []  # 빈 리스트를 생성한다.

# 자동차 시작 위치 설정
start_x = -200
start_y = 100
gap = -50

# 도착 지점(임시로 미리 정의) — 자동차 생성 전에 점선을 그리기 위해 미리 선언
finish_x = 200
finish_y = 100


# 수직 점선 그리기: x 위치에서 top -> bottom 방향으로 점선을 그림
def draw_vertical_dashed(x, top, bottom, dash=10, space=10):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.pensize(3)
    t.color("black")
    t.goto(x, top)
    t.setheading(270)  # 아래 방향
    dist = top - bottom
    drawn = 0
    # 점선 그리기
    while drawn < dist:
        t.pendown()
        step = min(dash, dist - drawn)
        t.forward(step)
        drawn += step
        t.penup()
        step = min(space, dist - drawn)
        t.forward(step)
        drawn += step


# 출발/도착 점선을 자동차 생성 전에 그림
# 점선 길이는 차선 전체를 덮도록 start/finish 주변을 충분히 잡음
top_y = max(start_y, finish_y) + 20  # 위쪽 여유 공간
bottom_y = min(start_y + gap * 5, finish_y + gap * 4) - 20  # 아래쪽 여유 공간
draw_vertical_dashed(start_x, top_y, bottom_y)  # 출발선
draw_vertical_dashed(finish_x, top_y, bottom_y)  # 도착선

# 자동차 5대 생성
for _ in range(1, 6):
    car_list.append(
        Car(random.randint(1, 10), "car2.gif", start_x, start_y + gap * _)
    )  # 속도, 이미지 파일 이름, 시작지점 x, y 좌표를 지정하여 Car 객체를 생성하고 리스트에 추가


# 각 자동차가 출발할 때 한 번에 랜덤 거리만큼 전진하도록 변경
winner = None
# 각 자동차가 도착선(finish_x)을 넘을 때까지 랜덤한 작은 거리(1~10)만큼 이동
while not winner:
    for car in car_list:
        car.drive(random.randint(1, 10))
        if car.turtle.xcor() >= finish_x:
            winner = car
            break

# 승자 표시 (콘솔과 화면에 텍스트)
winner_index = car_list.index(winner) + 1
print(f"자동차 {winner_index}번이 이겼습니다!")
pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, top_y + 30)
pen.write(
    f"자동차 {winner_index}번이 이겼습니다!", align="center", font=("Arial", 16, "bold")
)

done()  # 창 그대로 유지
