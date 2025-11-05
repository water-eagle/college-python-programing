"""
문자열을 받아서 모음의 개수를 카운팅하여 반환하는 함수 countVowel()를 작성하고 호출해보자.
"""


def countVowel(string):
    count = 0
    for ch in string:
        if ch in ["a", "e", "i", "o", "u"]:
            count += 1
    return count


s = input("문자열을 입력하시오: ")
n = countVowel(s)
print(f"모음의 개수는 {n}개입니다.")
