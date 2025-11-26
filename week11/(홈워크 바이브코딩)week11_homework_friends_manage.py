"""
리스트를 사용하여 친구의 이름, 전화번호, 주소(00동)을 관리하는 프로그램 작성
메뉴: 신규친구입력(동명이인 가능, 이름으로 검색하기, 주소로 검색하기, 이름으로 찾아 내용 수정하기, 이름으로 찾아 삭제하기(같은 이름 여러 개인 경우 사용자가 그 중에서 골라서 삭제)
"""


# 새 친구 등록
def insert_friend(friends):
    name = input("친구 이름: ")
    phone = input("폰 번호: ")
    address = input("주소(동): ")
    friends.append({"name": name, "phone": phone, "address": address})
    print("친구가 등록되었습니다.")


# 이름으로 검색
def search_by_name(friends):
    name = input("검색할 이름: ")
    found = [f for f in friends if f["name"] == name]
    if not found:
        print("찾는 친구가 없습니다.")
    else:
        for f in found:
            print("%-7s\t%-10s\t%-10s" % (f["name"], f["phone"], f["address"]))


# 주소로 검색
def search_by_addr(friends):
    address = input("검색할 주소(동): ")
    found = [f for f in friends if f["address"] == address]
    if not found:
        print("찾는 친구가 없습니다.")
    else:
        for f in found:
            print("%-7s\t%-10s\t%-10s" % (f["name"], f["phone"], f["address"]))


# 이름으로 찾아 내용 수정
def change_by_name(friends):
    name = input("수정할 친구 이름: ")
    found = [f for f in friends if f["name"] == name]
    if not found:
        print("찾는 친구가 없습니다.")
    elif len(found) == 1:
        idx = friends.index(found[0])
        new_name = input("새 이름 (현재: %s): " % found[0]["name"]) or found[0]["name"]
        new_phone = (
            input("새 전화번호 (현재: %s): " % found[0]["phone"]) or found[0]["phone"]
        )
        new_address = (
            input("새 주소 (현재: %s): " % found[0]["address"]) or found[0]["address"]
        )
        friends[idx] = {"name": new_name, "phone": new_phone, "address": new_address}
        print("수정되었습니다.")
    else:
        print("여러 명의 친구가 있습니다. 선택하세요:")
        for i, f in enumerate(found):
            print(
                "%d. %-7s\t%-10s\t%-10s" % (i + 1, f["name"], f["phone"], f["address"])
            )
        choice = int(input("선택 (1-%d): " % len(found))) - 1
        idx = friends.index(found[choice])
        new_name = (
            input("새 이름 (현재: %s): " % found[choice]["name"])
            or found[choice]["name"]
        )
        new_phone = (
            input("새 전화번호 (현재: %s): " % found[choice]["phone"])
            or found[choice]["phone"]
        )
        new_address = (
            input("새 주소 (현재: %s): " % found[choice]["address"])
            or found[choice]["address"]
        )
        friends[idx] = {"name": new_name, "phone": new_phone, "address": new_address}
        print("수정되었습니다.")


# 이름으로 찾아 삭제
def delete_by_name(friends):
    name = input("삭제할 친구 이름: ")
    found = [f for f in friends if f["name"] == name]
    if not found:
        print("찾는 친구가 없습니다.")
    elif len(found) == 1:
        idx = friends.index(found[0])
        del friends[idx]
        print("삭제되었습니다.")
    else:
        print("여러 명의 친구가 있습니다. 선택하세요:")
        for i, f in enumerate(found):
            print(
                "%d. %-7s\t%-10s\t%-10s" % (i + 1, f["name"], f["phone"], f["address"])
            )
        choice = int(input("선택 (1-%d): " % len(found))) - 1
        idx = friends.index(found[choice])
        del friends[idx]
        print("삭제되었습니다.")


# 전체 친구 출력
def all_friend_print(friends):
    if not friends:
        print("등록된 친구가 없습니다.")
        return
    new_list = sorted(friends, key=lambda x: x["name"])
    for i in new_list:
        print("%-7s\t%-10s\t%-10s" % (i["name"], i["phone"], i["address"]))


# 메시지 지정
msg = "1. 새 친구 등록(동명이인 가능), 2. 이름으로 검색하기, 3. 주소로 검색하기 4. 이름으로 찾아 내용수정하기, 5. 이름으로 삭제하기 6. 전체 출력, 7. 종료 : "

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
            print("프로그램 종료")
            break
        else:
            print("1~7 중에서 선택하세요")
