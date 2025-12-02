"""
친구관리 프로그램을 객체지향 코딩으로 바꾸기, 소스에 주석달기
"""


class Friend:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def __str__(self):
        return f"{self.name}\t{self.phone}\t{self.addr}"


class FriendManager:
    def __init__(self):
        self.friends = []

    # 1. 새친구 등록
    def insert_friend(self):
        name = input("친구이름: ")
        phone = input("폰번호: ")
        addr = input("주소(동) : ")
        friend = Friend(name, phone, addr)
        self.friends.append(friend)

    # 2. 이름으로 검색하기
    def search_by_name(self):
        # """이름으로 친구 목록 반환 (동명이인 가능)"""
        # results = [f for f in self.friends if f.name == name]
        # return results
        input_name = input("친구이름: ")
        cnt = 0  # 이름이 있는 지 확인
        for name, phone, addr in self.friends:
            if name == input_name:
                print(f"폰번호: {phone}, 주소: {addr}")
                cnt += 1
        if cnt == 0:
            print("등록되지 않은 이름입니다")

    # 3. 주소로 검색하기
    def search_by_addr(self):
        addr = input("주소(동): ")
        cnt = 0  # 해당 주소에 사는 친구 여부 확인용

        for i in range(len(self.friends)):
            if self.friends[i][2] == addr:
                print(f"이름:{self.friends[i][0]}, 폰번호: {self.friends[i][1]}")
                cnt += 1
        if cnt == 0:
            print(f"{addr}에는 사는 친구가 없습니다")

    # 4. 이름으로 찾아 내용수정하기
    def change_by_name(self):
        change_index = []  # 동명이인들의 인덱스값 저장
        name = input("친구이름: ")
        cnt = 0

        for i in range(len(self.friends)):
            if self.friends[i][0] == name:
                print(
                    f"{cnt+1}번 친구 폰번호: {self.friends[i][1]}, 주소: {self.friends[i][2]}"
                )
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

        self.friends[index][1] = input("수정할 폰번호:")
        self.friends[index][2] = input("수정할 주소: ")
        print("수정완료")

    # 5. 이름으로 삭제하기
    def delete_friend(self):
        name = input("친구이름: ")

        def delete_by_name():
            delete_index = []  # 동명이인들의 인덱스값 저장
            name = input("친구이름: ")
            cnt = 0

            for i in range(len(self.friends)):
                if self.friends[i][0] == name:
                    print(
                        f"{cnt+1}번 친구 폰번호: {self.friends[i][1]}, 주소: {self.friends[i][2]}"
                    )
                    delete_index.append(i)
                    cnt += 1

            if cnt == 0:
                print("등록되지 않은 이름입니다")
                return
            elif cnt == 1:
                index = delete_index[0]
            else:  # 동명이인이 있는 경우
                cnt = int(input("몇번 친구를 삭제할까요? "))
                index = delete_index[cnt - 1]

            del self.friends[index]

            print("삭제완료")

    # 6. 전체 친구 출력
    def get_all_friends(self):
        return self.friends

    def run(self):
        """인터랙티브 메뉴 루프. self 인스턴스에서 직접 동작합니다."""
        menu = (
            "1.새친구등록(동명이인 가능), 2. 이름으로 검색하기, 3. 주소로 검색하기,"
            " 4. 이름으로 찾아 내용수정하기, 5. 이름으로 삭제하기, 6.전체 출력, 7.종료 : "
        )

        while True:
            try:
                n = int(input(menu))
            except Exception:
                print("숫자를 입력하세요 (1~7)")
                continue

            if n == 1:  # 새친구 등록
                self.insert_friend()

            elif n == 2:  # 이름으로 검색하기
                self.search_by_name()

            elif n == 3:  # 주소로 검색하기
                self.search_by_addr()

            elif n == 4:  # 이름으로 찾아 내용수정하기
                self.change_by_name()

            elif n == 5:  # 이름으로 삭제하기
                self.delete_friend()

            elif n == 6:
                for f in sorted(self.get_all_friends(), key=lambda x: x.name):
                    print(f)

            elif n == 7:
                print("프로그램 종료\n")
                break

            else:
                print("1~7중에서 선택하세요\n")


if __name__ == "__main__":
    fmgr = FriendManager()
    fmgr.run()
