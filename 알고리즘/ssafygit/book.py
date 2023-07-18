number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    print(f"현재 가입 된 유저 수 : {number_of_people}")

def create_user(name, age, address):
    global number_of_people
    print(f"현재 가입 된 유저 수 : {number_of_people}")              # 초기 인원 print
    user_info = dict(name = name, age = age, address = address)    # 딕셔너리에 각 값 입력 
    print(f"{name}님 환영합니다!")                                  # 이름 출력
    print(user_info)                                               # 딕셔너리 출력
    increase_user()                                                # 유저 수 += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
