"""
<실습문제 #2>
1. 주석문달기
2. 요구사항: 3명 학생의 이름, 국,영,수 점수를 입력받아 list변수에 저장하기(중첩리스트와 반복구조 사용)
3. 화면에 아래와 같이 서식을 갖춰서 출력하기(평균값은 소수점1자리까지 표시)

성명           국어    영어    수학   총점     평균
Kim             95        90       95    총점1    평균1
Min              100     50       40    총점2    평균2
Park             75       88       63   총점3    평균3
===================================
총점/평균     O/o.o  O/o.o    O/o.o

4. 소스는 간결하게, 읽기 쉽게 작성할 것
"""

# 3명의 학생의 이름과 국어, 영어, 수학 점수를 입력받아 list 중첩리스트에 저장하기
list = [[0 for col in range(4)] for row in range(3)]
for x in range(0, 3):
    list[x][0] = input(f"{x+1}번째 학생 성명: ")
    list[x][1] = int(input(f"{list[x][0]}의 국어 점수: "))
    list[x][2] = int(input(f"{list[x][0]}의 영어 점수: "))
    list[x][3] = int(input(f"{list[x][0]}의 수학 점수: "))

# 학생별 출력 및 과목별 합계 계산
print("성명\t국어\t영어\t수학\t총점\t평균")
for x in range(0, 3):
    total = 0
    for y in range(0, 4):
        print(f"{list[x][y]}\t", end="")
        if y > 0:
            total += list[x][y]
    avg = total / 3
    print(f"{total}\t{avg:.1f}")
print("===================================")

# 과목별 총점 및 평균 계산 및 출력
print("총점/평균\t", end="")
for y in range(1, 4):
    sub_total = 0
    for x in range(0, 3):
        sub_total += list[x][y]
    sub_avg = sub_total / 3
    print(f"{sub_total}/{sub_avg:.1f}\t", end="")
