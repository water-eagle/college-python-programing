"""
## Lab: 팩토리얼 계산하기(P. 176)

- for문을 이용하여서 팩토리얼을 계산해보자.
- 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다. 즉, n! = 1×2×3×……×(n-1)×n이다.
"""

# 4. 팩토리얼 함수를 재귀함수로 정의하기


def calc_fact(n):
    if n == 1:
        return 1
    return calc_fact(n - 1) * n


"""
while True:
    n = int(input("1 이상의 정수 입력, 프로그램 종료는 0: "))
    if n == 0:
        print("프로그램을 종료합니다")
        break
    fat = calc_fact(n)  # 함수호출
    print(f"{n}! = {fat}")  # 함수결과값 출력
"""
