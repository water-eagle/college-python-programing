"""
p391 - 화면에 car 객체를 그려보자
Turtle 그래픽을 사용해서 화면에 자동차를 그리고 움직이기
"""

from turtle import *  # pyright: ignore[reportWildcardImportFromLibrary]


class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car1.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)


register_shape("car1.gif")
myCar = Car(200, "red", "E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
