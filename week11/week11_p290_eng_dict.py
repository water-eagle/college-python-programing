english_dict = {}

english_dict["one"] = "하나"
english_dict["two"] = "둘"
english_dict["three"] = "셋"

while True:
    word = input("단어를 입력하세요 (종료하려면 'q' 입력): ")
    if word == "q":
        break
    print(english_dict[word])
