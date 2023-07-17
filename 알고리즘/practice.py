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

create_user("홍길동", 30, "서울")                                   # 각 인자 입력
    
    
