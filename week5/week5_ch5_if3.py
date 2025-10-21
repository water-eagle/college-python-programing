import turtle as t

t.shape("turtle")
 
t.penup() # 펜을 올려서 그림이 그려지지 않게 한다.
t.goto(100, 100) # (100, 100) 위치로 이동한다.
t.write("거북이 여기로 오면 양수입니다.")
t.goto(100, 0)
t.write("거북이 여기로 오면 0입니다.")
t.goto(100, -100)
t.write("거북이 여기로 오면 음수입니다.")

t.goto(0, 0) # 거북이를 (0, 0) 위치로 이동한다.
t.pendown() # 펜을 내려서 그림이 그려지게 한다.
s = t.textinput("","숫자를 입력하시오: ")
n = int(s)

if n > 0:
    t.goto(100, 100) # (100, 100) 위치로 이동한다.
elif n == 0:
    t.goto(100, 0)
else:
    t.goto(100, -100)
t.done()