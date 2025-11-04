"""
리스트로 입력값을 저장하고
fstring 이용해서 출력하기
"""

friend = []
friend.append(input("이름: "))
friend.append(input("성: "))
friend.append(int(input("나이: ")))

print("이름: " + friend[0] + ", 성: " + friend[1] + ", 나이: " + str(friend[2]))
