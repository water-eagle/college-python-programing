"""
<편의점 물품 재고 관리>
- 메뉴 1. 신규물품 재고 등록, 2. 특정물품 재고향 증가, 3. 특정물품 재고향 감소, 4. 특정 물품 삭제, 5. 전체 물품 출력, 6. 종료
- 딕셔너리 자료형 사용: item_dict = {물품명1:재고량1, 물품명2:재고량2, ...}
"""


# 신규물품 등록
def insert_item():
    item_key = input("물품병")
    item_dict[item_key] = int(input("재고: "))
    print("등록완료")


# 특정물품 재고량 증가
def inc_cnt():
    item_key = input("물품명: ")
    item_dict[item_key] += int(input("재고 증가량: "))
    print("재고량 증가 완료")


# 특정물품 재고량 감소
def dec_cnt():
    item_key = input("물품명: ")
    item_dict[item_key] -= int(input("재고 감소량: "))
    print("재고량이 음수가 됩니다.")


# 특정물품 삭제
def delete_item():
    item_key = input("물품명: ")
    del item_dict[item_key]
    print("삭제완료")


# 전체 물품 출력
def all_item_print():
    for item_key in sorted(item_dict.keys()):
        print("%7s\t5d" % (item_key, item_dict[item_key]))


# 전역변수 생성
msg = "1.물품등록 2.재고량증가 3.재고량 감소 4.물품삭제 5. 전체물품 출력 6.종료"
item_dict = {}

if __name__ == "__main__":
    while True:
        n = int(input(msg))

        if n == 1:
            insert_item()
        elif n == 2:
            inc_cnt()
        elif n == 3:
            delete_item()
        elif n == 4:
            dec_cnt()
        elif n == 5:
            all_item_print()
        elif n == 6:
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력")
