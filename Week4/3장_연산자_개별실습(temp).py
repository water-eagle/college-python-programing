# 3장 개별실습: 초값(time_value) 입력받아 시간(hour), 분(min), 초(sec)로 변환한 값 출력하기

# 시간 모듈을 불러온다
import time as time

# 1970년 이후 흘러온 초가 실수로 반환됨
fseconds = time.time()
total_sec = int(fseconds)

# 사용자에게 초값을 입력 받아 변수로 저장하기
time_sec = int(input("변환할 초값을 정수로 입력하세요"))

# 시간, 분, 초로 변환하기
# 흘러온 초를 분으로 바꾸고, 현재 몇분인지 계산
total_min = total_sec // 60
minute = total_min % 60

# 흘러온 분을 시간으로 바꾸고, 현재 몇시인지 계산
total_hour = total_min // 60
hour = total_hour % 24

print("현재 시간(영국 그리니치 시각): " + str(hour) + "시 " + str(minute) + "분")
