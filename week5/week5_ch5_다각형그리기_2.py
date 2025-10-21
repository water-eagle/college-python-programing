import turtle as t

# 사용자에게 몇 각형 그릴지 물어보기
t.up()
t.goto(-100, 200)
t.down
n = int(t.textinput("", "몇 각형을 그릴까요?: "))

if n==3 or n==4 or n==5 or n==6:

    angle = 360/n

    t.up()
    t.goto(0, 200)
    t.down()

    # 해당 다각형 그리기
    for i in range(n): 
        t.forward(n)
        t.left(angle)
else:
    t.write("잘못된 입력값입니다.")


# elif shape == "원":

t.done()