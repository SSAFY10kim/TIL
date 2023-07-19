
user_list = []
def create_user(name, age, address):
    global user_list
    user_info = dict(name = name, age = age, address = address)    # 딕셔너리에 각 값 입력 
    print(f"{name}님 환영합니다!")                                  # 이름 출력
    user_list.append(user_info)

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in range(5):
    create_user(name[i],age[i],address[i])
print(user_list)
