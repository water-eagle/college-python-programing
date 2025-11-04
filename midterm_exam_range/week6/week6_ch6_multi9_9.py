# 6장 반복문
# 구구단 출력

a = int(input("원하는 단은: "))
for b in range(1, 10):
    print("%d * %d = %d" % (a, b, a * b))
