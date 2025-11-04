"""
# 3장 - 계산

## 3장 개별실습

1. 사용자에게 **초값**을 입력받음 (예: 3700)
2. 입력받은 초값을 시간, 분
3. 결과값 출력 (예: 3700초는 1시간 1분 40초)
"""

sec = int(input("변환할 초값 입력: "))

#
hour = sec // (60 * 60)  # 나눠서 시간 구하기, 1시간은 360초
remain_time = sec % (60 * 60)  #
min = remain_time // 60
out_sec = remain_time % 60

print("입력한", sec, "초는 ", hour, "시간 ", min, "분 ", out_sec, "초입니다.")
