"""
연습문제 2번 TV클래스 정의하고 1개 객체 만들기, 사용자에게 메뉴를 보여주고 입력된 메뉴에 따라 TV조작하기(TV켜기, 끄기, 채널변경, 볼륨변경)
"""


class TV:
    def __init__(self):
        self.channel = 1  # TV 채널 초기값 1
        self.volume = 10  # TV 볼륨 초기값 10
        self.on = False  # TV 전원 초기값 꺼짐(False)

    def turnOn(self):
        self.on = True  # TV 켜기 메서드

    def turnOff(self):
        self.on = False  # TV 끄기 메서드

    def setChannel(self, channel):  # 채널을 변경한다.
        if self.on:  # TV가 켜져 있을 때만 채널 변경 가능
            self.channel = channel
        else:
            print("TV가 꺼져 있습니다. 먼저 TV를 켜주세요.")

    def setVolume(self, volume):  # 볼륨을 변경한다.
        if self.on:  # TV가 켜져 있을 때만 볼륨 변경 가능
            self.volume = volume
        else:
            print("TV가 꺼져 있습니다. 먼저 TV를 켜주세요.")

    def tvPowerToggle(self):
        if input("TV 전원을 토글하시겠습니까? (y/n): ").lower() != "y":
            return
        self.on = not self.on  # TV 전원 상태를 토글한다.


if __name__ == "__main__":
    tv = TV()  # TV 객체 생성
    tv.tvPowerToggle()  # TV 전원 토글(켜기)
    print(f"TV 전원 상태: {'켜짐' if tv.on else '꺼짐'}")

    tv.setChannel(int(input("변경할 채널 입력: ")))  # 사용자로부터 채널 입력 받기
    tv.setVolume(int(input("변경할 볼륨 입력: ")))  # 사용자로부터 볼륨 입력 받기
    print(f"TV의 채널: {tv.channel}")
    print(f"TV의 음량: {tv.volume}")
