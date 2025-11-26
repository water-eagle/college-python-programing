"""
리스트를 사용하여 친구의 이름, 전화번호, 주소(00동)을 관리하는 프로그램 작성
메뉴: 신규친구입력(동명이인 가능, 이름으로 검색하기, 주소로 검색하기, 이름으로 찾아 내용 수정하기, 이름으로 찾아 삭제하기(같은 이름 여러 개인 경우 사용자가 그 중에서 골라서 삭제)
"""


# 1. 새 친구 등록
def insert_friend(friends):
    name = input("친구 이름: ")
    phone = input("폰 번호: ")
    address = input("주소(동): ")
    friends.append([name, phone, address])
    # print("친구가 등록되었습니다.")


# 2. 이름으로 검색하기
def search_by_name(friends):
    name = input("검색할 이름:")
    found = [friend for friend in friends if friend[0] == name]
    if not found:
        print("등록된 친구가 없습니다.")
        return
    for i in found:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))


# 3. 주소로 검색하기
def search_by_addr(friends):
    address = input("검색할 주소(동): ")
    found = [friend for friend in friends if friend[2] == address]
    if not found:
        print("등록된 친구가 없습니다.")
        return
    for i in found:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))


# 4. 이름으로 찾아 내용 수정하기
def change_by_name(friends):
    name = input("수정할 이름:")
    found = [friend for friend in friends if friend[0] == name]
    if not found:
        print("등록된 친구가 없습니다.")
        return
    for i in found:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))
    phone = input("새로운 폰 번호:")
    address = input("새로운 주소(동):")
    for i in found:
        friends.remove(i)
        friends.append([name, phone, address])
    print("수정이 완료되었습니다.")


# 5. 이름으로 찾아 삭제하기
def delete_by_name(friends):
    name = input("삭제할 이름:")
    found = [friend for friend in friends if friend[0] == name]
    if not found:
        print("등록된 친구가 없습니다.")
        return
    for i in found:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))
        if input("삭제하시겠습니까? (y/n): ") == "y":
            friends.remove(i)
            print("삭제가 완료되었습니다.")
        else:
            print("삭제가 취소되었습니다.")


# 6. 전체 친구 출력
def all_friend_print(friends):
    new_list = sorted(friends)
    for i in new_list:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))


# 메시지 지정
msg = "1. 새 친구 등록 2. 이름으로 검색하기 3. 주소로 검색하기 4. 이름으로 찾아 내용 수정하기 5. 이름으로 찾아 삭제하기 6. 전체 친구 출력 7. 종료: "

friends = [["홍길동", "010-1234-5678", "강남구"], ["김철수", "010-2345-6789", "서초구"]]

if __name__ == "__main__":
    while True:
        n = int(input(msg))

        if n == 1:
            insert_friend(friends)
        elif n == 2:
            search_by_name(friends)
        elif n == 3:
            search_by_addr(friends)
        elif n == 4:
            change_by_name(friends)
        elif n == 5:
            delete_by_name(friends)
        elif n == 6:
            all_friend_print(friends)
        elif n == 7:
            print("프로그램 종료\n")
            break
        else:
            print("1~7 중에서 선택하세요\n")
