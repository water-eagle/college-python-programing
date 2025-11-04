import turtle as t
t.shape("turtle")
t.speed(10) # 속도
t.pendown()

# 자동차 크기 입력 받기
size = int(input("원하시는 자동차 크기를 입력하세요: "))

# 자동차 색깔 받기
# color = str(input("원하시는 자동차 색깔을 입력하세요: "))

# 큰 자동차 몸체 200*100 8*4
t.fillcolor("red")
t.begin_fill()
t.forward(size*8)

t.left(90)
t.forward(size*4)

t.left(90)
t.forward(size*8)

t.left(90)
t.forward(size*4)

t.left(90)
t.end_fill()
# 창문 그리기 이동 200*100 4*2
t.forward(size*8)

t.left(90)
t.forward(size*4)

t.left(90)
# 그리기 100*50
t.fillcolor("yellow")
t.begin_fill()
t.forward(size*2)
t.right(90)

t.forward(size*2)
t.left(90)

t.forward(size*4)
t.left(90)

t.forward(size*2)
t.right(90)
t.end_fill()

# 복귀
t.penup()
t.goto(0, 0)
t.left(90)
t.pendown()

# 바퀴 그리기 25 1
t.fillcolor("black")
t.begin_fill()
t.circle(size)
t.end_fill()

t.left(90)
t.forward(size*6)

t.right(90)
t.fillcolor("black")
t.begin_fill()
t.circle(size)
t.end_fill()
