"""
p392 - 2개의 객체를 만들어보자
2개의 Car 객체를 생성하여 각각의 Car 객체가 서로 다른 경로를 주행하도록 하기
"""

from turtle import *


class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)

    def drive(self, distance):
        # move forward by the requested distance
        self.turtle.forward(distance)

    def turnleft(self, distance):
        # compatibility method for callers that expect turnleft
        self.turtle.left(distance)


register_shape("car1.gif")
register_shape("car2.gif")
myCar = Car(200, "red", "car1.gif")
yourCar = Car(0, "red", "car2.gif")

for i in range(4):
    myCar.drive(30)
    myCar.turnleft(90)
    yourCar.drive(100)
    yourCar.turnleft(60)
