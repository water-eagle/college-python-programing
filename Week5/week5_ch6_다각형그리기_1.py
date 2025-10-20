import turtle as t

# shape = t.textinput("", "도형을 입력하시오.")
n = int(t.textinput("", "가로: "))
angle = 360/n

for i in range(n):
    t.forward(n)
    t.left(angle)
t.end_fill()
t.done()

# elif shape == "원":

# 자동차가 창 중심에 있도록 펜촉을 이동한다.

# 자동차 몸체 색상을 body_color로 지정하고, 채우기 시작하고, 몸체를 그린다.
#t.fillcolor(body_color)
#t.begin_fill()
