# <3장 팀 실습과제>
# 초를 입력받아 시간,분,초로 변환하여 출력하기( //, %)
# 시간 모듈을 불러온다.

# 2024136021 장을수
import time

#1970년이후 불러온 초가 실수로 반횐됨
fesconds = time.time()
total_sec = int(fesconds)

#흘러온 초를 분으로 바꾸고, 현재 몇분인지 계산
total_min = total_sec // 60
minute = total_min % 60

#흘러온 분을 시간으로 바꾸고, 현재 몇시인지계산
total_hour = total_min // 60
hour = total_hour % 24

print("현재 시간(영국 그리니치 시간): " + str(hour) + "시" + str(minute) + "분")
