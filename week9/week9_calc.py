"""
1. 작성한 6장 도전문제소스를 함수 사용하는 소스로 만들기 calc.py
<문제요구사항>
    1. 1~9중 2개의 숫자를 무작위로 뽑고,사칙연산자(+,-,*,/)도 무작위로 생성하여 수학식을 만들어 화면에 출력.
    2. 사용자가 처음 정답을 맞출 때까지 계속 그 수학식을 풀게 한다.
    3. 문제풀이가 끝나면 사용자에게 계속 할지를 물어보고(y/n), 사용자가 종료를 선택하면 프로그램을 끝내고 아니면 1~2를 계속 수행한다.
"""

import random


def random_number():
    # 1~9 사이의 정수 두 개를 무작위로 뽑기
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return a, b


def random_operator(a, b):
    operator = random.choice(["+", "-", "*", "/"])  # 사칙연산자 무작위로 생성
    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    elif operator == "*":
        answer = a * b
    else:  # "/"
        # 나눗셈은 소수로 나오므로 소수 둘째자리까지 반올림해서 문제로 출제
        answer = round(a / b, 2)

    return operator, answer


def quiz(a, b, operator, answer):
    tries = 0
    print(f"문제: {a} {operator} {b} = ?")

    while True:
        user_input = input("정답을 입력하세요: ")
        try:
            guess = float(user_input)
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        tries += 1

        # 나눗셈은 반올림해서 비교 (소수 둘째자리까지)
        if operator == "/":
            if abs(guess - answer) < 1e-2:
                print(f"정답입니다! 시도 횟수: {tries}")
                break
            else:
                print("틀렸습니다. 소수 둘째자리까지 반올림해서 다시 시도하세요.")
        else:
            # 정수 연산의 경우 정확히 일치해야 정답
            if guess == answer:
                print(f"정답입니다! 시도 횟수: {tries}")
                break
            else:
                print("틀렸습니다. 다시 시도하세요.")


if __name__ == "__main__":
    # 메인 루프: 문제를 내고 사용자가 종료할 때까지 반복
    while True:
        a, b = random_number()
        operator, answer = random_operator(a, b)
        quiz(a, b, operator, answer)

        cont = input("계속 하시겠습니까? (y/n): ")
        if cont.lower() != "y":
            print("프로그램을 종료합니다.")
            break
