"""
친구관리 프로그램을 객체지향 코딩으로 바꾸기, 소스에 주석달기
"""


class Friend:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def update_phone(self, new_phone):
        self.phone = new_phone

    def update_addr(self, new_addr):
        self.addr = new_addr

    def __str__(self):
        return f"{self.name}\t{self.phone}\t{self.addr}"


class FriendManager:
    def __init__(self):
        self.friends = []

    # 새친구 등록
    def insert_friend(self, name, phone, addr):
        friend = Friend(name, phone, addr)
        self.friends.append(friend)

    # 이름으로 검색하기
    def search_by_name(self, name):
        for friend in self.friends:
            if friend.name == name:
                return friend
        return None

    # 주소로 검색하기
    def search_by_addr(self, addr):
        results = []
        for friend in self.friends:
            if friend.addr == addr:
                results.append(friend)
        return results

    # 이름으로 찾아 내용수정하기
    def change_by_name(self, name, new_phone=None, new_addr=None):
        friend = self.search_by_name(name)
        if friend:
            friend.update_phone(new_phone) if new_phone else None
            friend.update_addr(new_addr) if new_addr else None
        else:
            print("등록되지 않은 이름입니다")

    # 이름으로 삭제하기
    def delete_friend(self, name):
        friend = self.search_by_name(name)
        if friend:
            self.friends.remove(friend)
        else:
            print("등록되지 않은 이름입니다")

    # 전체 친구 출력
    def get_all_friends(self):
        return self.friends


"""
# 새친구 등록
def insert_friend():
    name = input("친구이름: ")
    phone = input("폰번호: ")
    addr = input("주소(동) : ")
    friend.append([name, phone, addr])


# 이름으로 검색하기
def search_by_name():
    input_name = input("친구이름: ")
    cnt = 0  # 이름이 있는 지 확인

    for name, phone, addr in friend:
        if name == input_name:
            print(f"폰번호: {phone}, 주소: {addr}")
            cnt += 1
    if cnt == 0:
        print("등록되지 않은 이름입니다")


# 주소로 검색하기
def search_by_addr():
    addr = input("주소(동): ")
    cnt = 0  # 해당 주소에 사는 친구 여부 확인용

    for i in range(len(friend)):
        if friend[i][2] == addr:
            print(f"이름:{friend[i][0]}, 폰번호: {friend[i][1]}")
            cnt += 1
    if cnt == 0:
        print(f"{addr}에는 사는 친구가 없습니다")


# 이름으로 찾아 내용수정하기
def change_by_name():
    change_index = []  # 동명이인들의 인덱스값 저장
    name = input("친구이름: ")
    cnt = 0

    for i in range(len(friend)):
        if friend[i][0] == name:
            print(f"{cnt + 1}번 친구 폰번호: {friend[i][1]}, 주소: {friend[i][2]}")
            change_index.append(i)
            cnt += 1

    if cnt == 0:
        print("등록되지 않은 이름입니다")
        return
    elif cnt == 1:
        index = change_index[0]
    else:  # 동명이인이 있는 경우
        cnt = int(input("몇번 친구를 수정할까요? "))
        index = change_index[cnt - 1]

    friend[index][1] = input("수정할 폰번호:")
    friend[index][2] = input("수정할 주소: ")
    print("수정완료")


# 이름으로 삭제하기
def delete_by_name():
    delete_index = []  # 동명이인들의 인덱스값 저장
    name = input("친구이름: ")
    cnt = 0

    for i in range(len(friend)):
        if friend[i][0] == name:
            print(f"{cnt + 1}번 친구 폰번호: {friend[i][1]}, 주소: {friend[i][2]}")
            delete_index.append(i)
            cnt += 1

    if cnt == 0:
        print("등록되지 않은 이름입니다")
        return

    elif cnt == 1:
        index = delete_index[0]
    else:
        cnt = int(input("몇번 친구를 삭제할까요? "))
        index = delete_index[cnt - 1]

    del friend[index]

    print("삭제완료")


# 전체 친구 출력
def all_friend_print():
    new_list = sorted(friend)
    for i in new_list:
        print("%-7s\t%-10s\t%-10s\n" % (i[0], i[1], i[2]))
"""

# 메시지 지정
msg = "1.새친구등록(동명이인 가능), 2. 이름으로 검색하기, 3. 주소로 검색하기 4. 이름으로 찾아 내용수정하기, 5. 이름으로 삭제하기  6.전체 출력, 7.종료 : "

"""
friend = []

if __name__ == "__main__":
    while True:
        n = int(input(msg))

        if n == 1:
            insert_friend()
        elif n == 2:
            search_by_name()
        elif n == 3:
            search_by_addr()
        elif n == 4:
            change_by_name()
        elif n == 5:
            delete_by_name()
        elif n == 6:
            all_friend_print()
        elif n == 7:
            print("프로그램 종료\n")
            break
        else:
            print("1~7중에서 선택하세요\n")
"""
if __name__ == "__main__":
    fmgr = FriendManager()
    while True:
        n = int(input(msg))
        if n == 1:  # 새친구 등록
            name = input("친구이름: ")
            phone = input("폰번호: ")
            addr = input("주소(동) : ")
            fmgr.insert_friend(name, phone, addr)

        elif n == 2:  # 이름으로 검색하기
            name = input("친구이름: ")
            friend = fmgr.search_by_name(name)
            if friend:
                print(f"폰번호: {friend.phone}, 주소: {friend.addr}")
            else:
                print("등록되지 않은 이름입니다")
        elif n == 3:  # 주소로 검색하기
            addr = input("주소(동): ")
            results = fmgr.search_by_addr(addr)
            if results:
                for friend in results:
                    print(f"이름:{friend.name}, 폰번호: {friend.phone}")
            else:
                print(f"{addr}에는 사는 친구가 없습니다")

        elif n == 4:  # 이름으로 찾아 내용수정하기
            name = input("친구이름: ")

            new_phone = input("수정할 폰번호 (수정 안할거면 엔터): ")
            new_addr = input("수정할 주소 (수정 안할거면 엔터): ")
            fmgr.change_by_name(
                name, new_phone if new_phone else None, new_addr if new_addr else None
            )

        elif n == 5:  # 이름으로 삭제하기
            name = input("친구이름: ")
            fmgr.delete_friend(name)
        elif n == 6:
            friends = fmgr.get_all_friends()
            for friend in sorted(friends, key=lambda x: x.name):
                print(friend)
        elif n == 7:
            print("프로그램 종료\n")
            break
        else:
            print("1~7중에서 선택하세요\n")
