# 1~9 사이 숫자 2개를 무작위로 뽑아 2개 숫자 더하기 산수문제를 화면에 출력,
# 사용자가 입력한 더하기 값이 맞는지 화면에 출력하기
#
import random as r
a = r.randint(1,9)
b = r.randint(1,9)

msg = str(a) + "+" + str(b) + "= "
input_value = int(input(msg))

if (input_value == a+b):
    print("정답!")
    exit(0)
print("틀렸어요!")
