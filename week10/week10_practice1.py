"""
<실습1>
사용자에게 2이상 정수 n과 연산자를 입력받아
연산자가 곱하기이면 1~n까지의 곱을 계산
연산자가 더하기면 1~n까지의 합을 계산
함수 사용하기 전과 후 비교
"""

n = int(input("정수를 입력하시오"))

op = input("연산자를 선택하시오(+, * )")

# 함수 사용 전
"""
if op == "+":
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)
elif op == "*":
    total = 1
    for i in range(1, n + 1):
        total *= i
    print(total)
else:
    print("잘못된 연산자입니다.")
"""


# 함수 사용 후
def calc(n, op):
    if op == "+":
        total = 0
        for i in range(1, n + 1):
            total += i
    elif op == "*":
        total = 1
        for i in range(1, n + 1):
            total *= i
    else:
        print("잘못된 연산자입니다.")
    return total


print(calc(n, op))
