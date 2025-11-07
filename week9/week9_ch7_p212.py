import turtle as t


def square(x, y, length):  # length는 변의 길이
    t.up()  # 펜을 든다.
    t.goto(x, y)  # (x, y)으로 이동한다.
    t.down()  # 펜을 내린다.

    for i in range(4):
        t.forward(length)
        t.left(90)
