# 두근두근 파이썬 4장 연습문제 7번
# 사용자가 입력하는 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그 색상으로 채워진 원을 그리는 프로그램을 작성해보자. 신호등처럼 보이게 출력한다. 반복문은 사용하지 않는다.

# 리스트에 색상을 문자열로 저장하였다가 하나씩 꺼내서 거북이의 채우기 색상으로 설정하고 원을 그려 보자.

import turtle as t

t.shape("turtle")
t.speed(10)

# input으로 입력 받은 색상을 리스트에 저장한다.
color_list = []
color_list.append(input("색상 #1을 입력하시오: "))
color_list.append(input("색상 #2을 입력하시오: "))
color_list.append(input("색상 #3을 입력하시오: "))

t.pendown()
t.fillcolor(color_list[0])  # 채우기 색상을 설정한다.
t.begin_fill()  # 채우기를 시작한다.
t.circle(100)  # 속이 채워진 원이 그려진다.
t.end_fill()  # 채우기를 종료한다.
t.penup()
t.forward(200)

t.pendown()
t.fillcolor(color_list[1])  # 채우기 색상을 설정한다.
t.begin_fill()  # 채우기를 시작한다.
t.circle(100)  # 속이 채워진 원이 그려진다.
t.end_fill()  # 채우기를 종료한다.
t.penup()
t.forward(200)

t.pendown()
t.fillcolor(color_list[2])  # 채우기 색상을 설정한다.
t.begin_fill()  # 채우기를 시작한다.
t.circle(100)  # 속이 채워진 원이 그려진다.
t.forward(200)
t.end_fill()  # 채우기를 종료한다.
