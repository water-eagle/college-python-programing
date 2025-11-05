"""
## Lab: 팩토리얼 계산하기(P. 176)

- for문을 이용하여서 팩토리얼을 계산해보자.
- 팩토리얼 n!은 1부터 n까지의 정수를 모두 곱한 것을 의미한다. 즉, n! = 1×2×3×……×(n-1)×n이다.
"""

# 3. 정수값을 입력받아 팩토리얼값을 계산하는 함수 작성하고 호출하기를 반복
# 사용자가 0을 입력하면 프로그램 종료


def calc_fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


while True:
    n = int(input("1 이상의 정수 입력, 프로그램 종료는 0: "))
    if n == 0:
        print("프로그램을 종료합니다")
        break
    fat = calc_fact(n)  # 함수호출
    print(f"{n}! = {fat}")  # 함수결과값 출력
