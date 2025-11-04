import turtle as t

t.shape("turtle")
t.speed(10)  # 속도
t.pendown()

# 자동차 크기 입력 받기
Dx = int(input("자동차 몸체 x축 길이: "))
Dy = int(input("자동차 몸체 y축 길이: "))
dx = int(input("자동차 창문 x축 길이: "))
dy = int(input("자동차 창문 y축 길이: "))
rad = int(input("자동차 바퀴 반지름: "))

print("-----")
# 자동차 색깔 받기 = int(input("자동차 몸채 색깔:"))
col1 = input("자동차 몸체 색깔: ")
col2 = input("자동차 창문 색깔: ")
col3 = input("자동차 바퀴 색깔: ")

# 자동차가 창 중심에 있도록 펜촉을 이동한다.
t.up()
t.goto(-Dx / 2, -Dy / 2)  # 펜촉을 왼쪽 아래 꼭지점으로 이동
t.down()  # 펜을 내린다.

# 자동차 몸체 색상을 col1로 지정하고, 채우기 시작하고, 몸체를 그린다.
t.fillcolor(col1)
t.begin_fill()

t.forward(Dx)
t.left(90)
t.forward(Dy)
t.left(90)

t.forward(Dx)
t.left(90)
t.forward(Dy)
t.left(90)

# 자동차 상체그리기 위해 좌표이동
t.up()
t.goto(-dx / 2, Dy / 2)  # 펜촉 왼쪽 아래 꼭지점으로 이동
t.down()  # 펜을 내린다.

# 자동차 상체 색상을 col2로 지정하고, 채우기 시작하고, 몸체를 그린다.
t.fillcolor(col1)
t.begin_fill()

t.right(180)
t.forward(dy)
t.right(90)
t.forward(dx)
t.right(90)
t.forward(dy)
t.right(90)
t.forward(dx)

t.end_fill()

# 타이어색상을 col3로 지정하고, 채우기 시작하고, 타이어를 그린다.
t.up()
t.goto(-(Dx / 4 / rad), -Dy / 2)  # 펜촉을 왼쪽 타이어 시작점으로 이동
t.left(90)
t.down()

t.fillcolor(col3)
t.begin_fill()
t.circle(rad)  # 원을 그린다.and

t.up()
t.goto(Dx / 4 - rad, -Dy / 2)  # 펜 촉을 오른쪽 타이어 시작점으로 이동
t.down()

t.circle(rad)
t.end_fill()
t.done
