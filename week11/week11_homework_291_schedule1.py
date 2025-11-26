"""일정관리 프로그램. 하나의 일자에 여러 개 일정을 넣을 수 있게함
딕셔너리[일자] = [일정1, 일정2, 일정3 ...]
"""

mydict = {}

while True:
    print("\n메뉴:")
    print("1. 일정 추가")
    print("2. 일정 조회")
    print("3. 일정 삭제")
    print("4. 종료")
    choice = input("선택하세요: ")

    if choice == "1":
        date = input("날짜를 입력하시오: ")
        job = input("일정을 입력하시오: ")
        if date not in mydict:
            mydict[date] = [job]
        else:
            mydict[date].append(job)
        print("일정이 추가되었습니다.")

    elif choice == "2":
        date = input("조회할 날짜를 입력하시오: ")
        if date in mydict:
            print(f"{date}의 일정: {mydict[date]}")
        else:
            print("해당 날짜에 일정이 없습니다.")

    elif choice == "3":
        date = input("삭제할 날짜를 입력하시오: ")
        if date in mydict:
            print(f"{date}의 일정: {mydict[date]}")
            job_to_delete = input("삭제할 일정을 입력하시오: ")
            if job_to_delete in mydict[date]:
                mydict[date].remove(job_to_delete)
                print("일정이 삭제되었습니다.")
                if not mydict[date]:
                    del mydict[date]
            else:
                print("해당 일정이 없습니다.")
        else:
            print("해당 날짜에 일정이 없습니다.")

    elif choice == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다.")

print(mydict)
# 프로그램 소스 더블클릭하면 콘솔창이 프로그램 실행 후 자동으로 닫히는 것을 방지
input()
