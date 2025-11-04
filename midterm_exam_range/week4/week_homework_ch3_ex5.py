# 사용자에게 두 개의 정수(x, y)를 입력받고 정수를 더하고(plus) 빼고(min) 곱하고(com) 나누고
# (div), 몫과 나머지를 구한 걸 출력하기

x = int(input("첫 번째 정수 입력"))
y = int(input("두 번째 정수 입력"))
print("x:", x)
print("y:", y)
print("두수의 합: ", x + y)
print("두수의 차: ", max(x, y) - min(x, y))
print("두수의 곱: ", x * y)
print("두수의 평균: ", (x + y) / 2)
print("큰수 ", max(x, y))
print("작은수: ", min(x, y))

# 추가
print("두수의 나누기: ", x / y)
