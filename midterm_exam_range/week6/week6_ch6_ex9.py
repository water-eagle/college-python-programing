"""
6장 연습문제 9번
사용자가 알파벳 소문자 3글자와 숫자 2글자로 패스워드를 만들었다고 하자.
이 패스워드를 알아 맞추는 프로그램을 작성해보자.
본문의 Lab을 참고한다.
"""

import sys

user_pass = input("패스워드를 입력하시오: ")
pwd_str = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
pwd_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for letter1 in pwd_str:
    for letter2 in pwd_str:
        for letter3 in pwd_str:
            for letter4 in pwd_num:
                for letter5 in pwd_num:
                    guess = letter1 + letter2 + letter3 + letter4 + letter5
                    # print(guess)
                    if guess == user_pass:
                        print("당신의 패스워드는 " + guess)
                        sys.exit()
