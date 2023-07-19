from book import decrease_book

name_age = {}
user_list = []

def create_user(name, age):
    global name_age
    for i in range(len(name)):
        name_age = {"name" : name[i], "age" : age[i]}
        user_list.append(name_age)
        print(f"{name[i]}님 환영합니다!")                                 # 이름 출력
    rental_book()

def rental_book(info):
    create_user(name, age)
    decrease_book(info["age"])

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

rental_book(name_age)



