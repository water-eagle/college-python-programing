"""
2. Random함수를 이용하여 1~100숫자중에서 10개를 중복된 값없이 무작위로 추출하여 리스트변수에 저장한다.
이 리스트값을 인수로 넘겨 그중에서 최고값을 return하는 함수를 정의한다.
10개의 숫자와 해당함수의 호출값인 최고값을 화면에 출력한다.
"""

import random


def get_random_numbers():
    return random.sample(range(1, 101), 10)


def find_maximum(numbers):
    return max(numbers)


if __name__ == "__main__":
    random_numbers = get_random_numbers()
    max_value = find_maximum(random_numbers)

    print("생성된 숫자:", random_numbers)
    print("최고값:", max_value)
