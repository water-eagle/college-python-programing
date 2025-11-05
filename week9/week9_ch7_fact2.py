"""
## Lab: 팩토리얼 계산하기(P. 176)

- for문을 이용하여서 팩토리얼을 계산해보자.
- 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다. 즉, n! = 1×2×3×……×(n-1)×n이다.
"""

# 2 정수값을 입력받아 "팩토리얼값을 계산하는 함수로 작성"하고 호출하기


def calc_fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


n = int(input("1 이상의 정수 입력: "))
print(f"{n}! = {calc_fact(n)}")
