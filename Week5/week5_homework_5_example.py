# [실습5] 2개의 2자리 정수를 무작위로 생성하여 덧셈, 뺄셈, 곱셈, 나눗셈 문제를 내고 사용자의 입력값과 계산값을 비교하여 “정답“, “오답“ 출력하기 (if-else사용)
import random as r

# 2자리 정수를 무작위로 생성한다.
num1 = r.randint(10, 99)
num2 = r.randint(10, 99)

op_list = ["+", "-", "*", "/"]
op = r.choice(op_list)

print(f"{num1} {op} {num2} = ?")
user_answer = int(input("정답을 입력해주세요: "))

if op == "+":
    user_answer = num1 + num2
elif op == "-":
    user_answer = num1 - num2
elif op == "*" or "x":
    user_answer = num1 * num2
elif op == "/":
    user_answer = num1 / num2
else:
    print("오류")
