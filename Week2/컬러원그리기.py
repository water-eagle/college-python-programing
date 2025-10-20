import turtle as t

t.shape("turtle") # 펜촉 모양을 거북이 모양으로 설정
t.fillcolor("blue") # 채우는 색상 지정
t.begin_fill() # 채우기 시작
t.circle(100) # 반지름이 100인 원이 그려진다.
t.end_fill() # 채우기 종료
t.forward(100) # 100 픽셀크기로 직선을 그린다.
t.fillcolor("orange")
t.begin_fill()
t.circle(120) 		# 반지름이 120인 원이 그려진다.
t.end_fill()

t.done()
