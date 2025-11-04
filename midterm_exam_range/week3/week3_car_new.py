import turtle as t
t.shape("turtle")
t.speed(10) # 속도
t.pendown()

# 자동차 크기 입력 받기
body_dx = int(input("자동차 몸체 x축 길이: "))
body_dy = int(input("자동차 몸체 y축 길이: " ))
window_dx = int(input("자동차 창문 x축 길이: "))
window_dy = int(input("자동차 창문 y축 길이: "))
wheel_radius = int(input("자동차 바퀴 반지름: "))

print("-----")
# 자동차 색깔 받기 = int(input("자동차 몸채 색깔:"))
body_color = input("자동차 몸체 색깔: ")
window_color = input("자동차 창문 색깔: ")
wheel_color = input("자동차 바퀴 색깔: ")

# 자동차가 창 중심에 있도록 펜촉을 이동한다.
t.up()
t.goto(-body_dx/2, -body_dy/2) # 펜촉을 왼쪽 아래 꼭지점으로 이동
t.down() # 펜을 내린다.

# 자동차 몸체 색상을 body_color로 지정하고, 채우기 시작하고, 몸체를 그린다.
t.fillcolor(body_color)
t.begin_fill()

t.forward(body_dx)
t.left(90)
t.forward(body_dy)
t.left(90)

t.forward(body_dx)
t.left(90)
t.forward(body_dy)
t.left(90)

# 자동차 상체그리기 위해 좌표이동
t.up()
t.goto(-window_dx/2, body_dy/2) # 펜촉 왼쪽 아래 꼭지점으로 이동
t.down() # 펜을 내린다.

# 자동차 상체 색상을 window_color로 지정하고, 채우기 시작하고, 몸체를 그린다.
t.fillcolor(body_color)
t.begin_fill()

t.right(180)
t.forward(window_dy)
t.right(90)
t.forward(window_dx)
t.right(90)
t.forward(window_dy)
t.right(90)
t.forward(window_dx)

t.end_fill()

# 타이어색상을 wheel_color로 지정하고, 채우기 시작하고, 타이어를 그린다.
t.up()
t.goto(-(body_dx/4/wheel_radius), -body_dy/2) # 펜촉을 왼쪽 타이어 시작점으로 이동
t.left(90)
t.down()

t.fillcolor(wheel_color)
t.begin_fill()
t.circle(wheel_radius) # 원을 그린다.and

t.up()
t.goto(body_dx/4-wheel_radius, -body_dy/2) # 펜 촉을 오른쪽 타이어 시작점으로 이동
t.down()

t.circle(wheel_radius)
t.end_fill()
t.done
