"""
p393 - 10개 객체를 생성하려면?
리스트에 Car 객체를 10개 생성하여 저장하고, 각 자동차가 무작위로 전진하고 방향을 바꾸도록 하는 프로그램
"""

import random

# from turtle import *
from turtle import Turtle, register_shape, done

register_shape("car2.gif")


class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)

    def drive(self, distance):
        self.turtle.forward(distance)

    def turnleft(self, degree):
        self.turtle.left(degree)


car_list = []  # 빈 리스트를 생성한다.
for _ in range(10):
    car_list.append(Car(random.randint(1, 10), "red", "car2.gif"))


for _ in range(10):  # 10번 반복
    for car in car_list:
        car.drive(random.randint(50, 100))
        car.turnleft(random.choice([0, 90, 180, 270]))

done()  # 터틀 그래픽 창을 닫지 않고 유지
