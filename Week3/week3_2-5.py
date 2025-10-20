import turtle as t
t.speed(10) # 속도
t.shape("turtle")

radius = 50 # 반지름 초기값: 50

# 0, 0에
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(radius)
radius = radius + 20

# 100, 0
t.penup()
t.goto(100, 0)
t.pendown()
t.circle(radius)
radius = radius + 20

# 200, 0
t.penup()
t.goto(200, 0)
t.pendown()
t.circle(radius)
radius = radius + 20
