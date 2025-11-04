# 6장 반복문
# 구구단 출력

for i in range(1, 9):  # 1~9
    for dan in range(2, 10):  # 2단~9단
        if i == 0:  # 단 제목 출력
            print(f"=={dan}단==", end=" ")
        else:
            print("%d*%d=%2d" % (dan, i, dan * i), end=" ")
    print("\n")

# 구구단 출력하기(9단-->2단)
for i in range(1, 9):  # 1~9
    for dan in range(9, 1, -1):  # 9단~2단
        if i == 0:  # 단 제목 출력
            print(f"=={dan}단==", end=" ")
        else:
            print("%d*%d=%2d" % (dan, i, dan * i), end=" ")
    print("\n")
