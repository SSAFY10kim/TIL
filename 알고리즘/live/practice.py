# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        while True:
            try:
                user_name = input("이름을 입력하세요: ")
                user_age = int(input("나이를 입력하세요: "))
                self.user_data['이름'] = user_name
                self.user_data['나이'] = user_age
                break
                
            except:
                print("나이는 숫자로 입력해야 합니다.")
                return False

    def display_user_info(self):
        if '이름' in self.user_data and '나이' in self.user_data:
            print("사용자 정보:")
            print(f"이름: {self.user_data['이름']}")
            print(f"나이: {self.user_data['나이']}")
        else:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
