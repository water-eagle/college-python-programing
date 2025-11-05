import turtle as t


def draw(x, y):
    t.goto(x, y)


t.shape("turtle")
t.pensize(10)

s = t.Screen()
s.onscreenclick(draw)  # 마우스 클릭 이벤트 처리 함수를 등록한다.

s.onkey(t.penup, "Up")  # 키보드 이벤트 처리 함수를 등록한다.
s.onkey(t.pendown, "Down")  # 키보드 이벤트 처리 함수를 등록한다.
s.listen()  # 키보드 이벤트를 기다린다.
