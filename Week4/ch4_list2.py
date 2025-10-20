# 리스트에 색상을 문자열로 저장하였다가 하나씩 꺼내서 거북이의 채우기 색상으로 설정하고 원을 그려 보자.

import turtle  as t
t.shape("turtle")

# 리스트를 사용하여 색상을 문자열로 저장한다.
color_list = ["yellow", "red", "blue", "green"]

t.fillcolor(color_list[0])  # 채우기 색상을 설정한다.
t.begin_fill()  # 채우기를 시작한다.
t.circle(100)  # 속이 채워진 원이 그려진다.
t.end_fill()  # 채우기를 종료한다.
t.forward(50)

t.fillcolor(color_list[1])  # 채우기 색상을 설정한다.
t.begin_fill()  # 채우기를 시작한다.
t.circle(100)  # 속이 채워진 원이 그려진다.
t.end_fill()  # 채우기를 종료한다.
