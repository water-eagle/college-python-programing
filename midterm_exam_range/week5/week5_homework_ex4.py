"""
학생의 시험 점수를 물어보고
시험 점수가 90점 이상이면 A,
80점 이상이면 B,
70점 이상이면 C,
60점 이상이면 D,
그 외의 점수면 F를 학점으로 주는 프로그램을 작성하라
[실습3] 연습문제 4번 : if – elif- else 구문 사용
"""

# 학생의 시험 점수를 입력받는다.
score = int(input("성적을 입력하시요: "))

# 조건에 따라 학점을 결정한다.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# 결과 출력
print(f"{grade}학점입니다.")
