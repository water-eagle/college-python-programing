"""
실습문제 #1:
1, 10~99중 2개의 숫자를 무작위로 뽑고,사칙연산자(+,-,*,/)도 무작위로 생성하여 수학식을 만들어 화면에 출력.
2, 사용자가 문제 정답을 맞출 때까지 계속 그 수학식을 풀게 한다.
3, 처음 문제풀이가 끝나면 사용자에게 계속 할지를 물어보고(y/n),
사용자가 종료를 선택하면 프로그램을 끝내고 아니면 1~2를 계속 수행한다.
"""

import random

tries = 0
guess = 0

answer = random.randrange(1, 100)
# print(answer)
print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("낮음!")
    if guess > answer:
        print("높음!")

if guess == answer:
    print("축하합니다. 시도횟수: %d" % tries)
else:
    print("오답입니다. 정답은 %d" % answer)

"""
# 응용: 시도 횟수 10번 제한
if tries < 10:
    print(f"오답, 남은 시도 횟수: {tries - 1}/10")
elif tries == 10:
    print(f"시도 횟수가 10번을 넘겼으므로 실패하셨습니다. 정답은 {guess}.")
else:
    print(f"축하합니다. 남은 시도 횟수: {tries - 1}/10")
"""
