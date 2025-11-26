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
    for friend in found:
        print("%-7s\t%-10s\t%-10s\n" % (friend[0], friend[1], friend[2]))


# 3. 주소로 검색하기
def search_by_addr(friends):
    address = input("검색할 주소(동): ")
    if not address in friends:
        print("등록된 친구가 없습니다.")
        return
    for i in friends:
        if i[2] == address:
            print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))


# 4. 이름으로 찾아 내용 수정하기
def change_by_name(friends):
    name = input("수정할 이름:")
    if not name in friends:
        print("등록된 친구가 없습니다.")
        return
    for i in range(len(friends)):
        if friends[i][0] == name:
            phone = input("새 폰 번호: ")
            address = input("새 주소(동): ")
            friends[i] = {name, phone, address}
            print("친구 정보가 수정되었습니다.")


# 5. 이름으로 찾아 삭제하기
def delete_by_name(friends):
    name = input("삭제할 이름:")
    if not name in friends:
        print("등록된 친구가 없습니다.")
        return
    for i in range(len(friends)):
        if friends[i][0] == name:
            friends.pop(i)
            print("친구 정보가 삭제되었습니다.")
            return


# 6. 전체 친구 출력
def all_friend_print(friends):
    new_list = sorted(friends)
    if not friends:
        print("등록된 친구가 없습니다.")
        return
    for i in new_list:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))


# 메시지 지정
msg = "1. 새 친구 등록 2. 이름으로 검색하기 3. 주소로 검색하기 4. 이름으로 찾아 내용 수정하기 5. 이름으로 찾아 삭제하기 6. 전체 친구 출력 7. 종료: "

friends = []

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
