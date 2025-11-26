"""
1. 입력한 날짜에 일정 넣기
2. 특정한 날에 여러개 일정 등록 가능
3. 기능 메뉴화
"""

mydict = {}

while True:
    date = input("날짜를 입력하시오: ")
    if date == "q":
        break
    job = input("일정을 입력하시오: ")

    if date not in mydict:
        mydict[date] = job
    else:
        print("오류입니다.")

print(mydict)
