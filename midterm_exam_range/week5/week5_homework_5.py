"""
[실습5]
2개의 2자리 정수를 무작위로 생성하여 덧셈, 뺄셈, 곱셈, 나눗셈 문제를 내고
사용자의 입력값과 계산값을 비교하여 “정답“, “오답“ 출력하기 (if-else사용)
"""

import random as r

# 2자리 정수를 무작위로 생성한다.
a = r.randint(10, 99)
b = r.randint(10, 99)

answer = int(input(f"문제: {a}+{b} = "))
if answer == a + b:
    print("덧셈 정답!")
else:
    print("오답")

answer = int(input(f"문제: {a}-{b} = "))
if answer == a - b:
    print("정답!")
else:
    print("오답")

answer = int(input(f"문제: {a}*{b} = "))
if answer == a * b:
    print("정답!")
else:
    print("오답")

answer = int(input(f"문제: {a}/{b}의 몫?"))
if answer == a / b:
    print("정답!")
else:
    print("오답")
