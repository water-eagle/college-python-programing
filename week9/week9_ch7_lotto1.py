"""
ch7 - p215
로또 번호를 생성하는 함수를 작성하여 사용해보자.
로또 번호는 1부터 45까지의 숫자 6개로 이루어진다.
따라서 6개의 난수를 생성하여야 한다.
번호는 중복되면 안 된다.
"""

import random


def getLotto():  # 로또 번호 생성 함수
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1, 45)
        if n not in numbers:
            numbers.append(n)
    return numbers


print(f"생성된 로또 번호: {getLotto()}")  # 함수 호출하여 로또 번호 출력
