# 그림판을 띄우고 그림...

import turtle as t

n = 1  # 변수 n 선언 및 초기값 1

while n != 0:
    # 사용자에게 몇 각형 그릴지 물어보기
    t.up()
    t.goto(-100, 200)
    t.down
    n = int(t.textinput("", "몇 각형을 그릴까요? (종료는 0번): "))

    if n == 0:
        t.write("종료")
        break
    elif n < 3 or n > 6:
        t.write("잘못된 입력값입니다")
    else:  # 다각형 그리기
        t.reset()
        angle = 360 / n
        t.up()
        t.goto(0, -200)
        t.down
        for i in range(n):
            t.fd(100)
            t.right(angle)

t.write("프로그램을 종료합니다.")
t.done()
