import turtle as t

t.shape("turtle")
t.speed(10)

# 큰 자동차 몸체 200*100
t.fillcolor("red")
t.begin_fill()
t.forward(200)

t.left(90)
t.forward(100)

t.left(90)
t.forward(200)

t.left(90)
t.forward(100)

t.left(90)
t.end_fill()
# 창문 그리기 이동 100*50
t.forward(200)

t.left(90)
t.forward(100)

t.left(90)
# 그리기
t.fillcolor("yellow")
t.begin_fill()
t.forward(50)
t.right(90)

t.forward(50)
t.left(90)

t.forward(100)
t.left(90)

t.forward(50)
t.right(90)
t.end_fill()
# 복귀
t.forward(50)

t.left(90)
t.forward(100)

# 바퀴 그리기
t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()

t.left(90)
t.forward(150)

t.right(90)
t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()
