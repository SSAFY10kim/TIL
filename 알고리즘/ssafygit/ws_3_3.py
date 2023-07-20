from book import decrease_book

name_age = {}
user_list = []

def create_user(name, age):
    global name_age
    for i in range(len(name)):
        name_age = {"name": name[i], "age": age[i]}
        user_list.append(name_age)
        print(f"{name[i]}님 환영합니다!")  # 이름 출력

def rental_book(info):
    create_user(info["name"], info["age"])
    for user in user_list:
        num_books = user['age'] // 10
        decrease_book(num_books)
        print(f"{user['name']} 님이 {num_books}권의 책을 대여하였습니다.")
        

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

many_user = {"name": name, "age": age}
user_info = dict(map(lambda i: (i[0], i[1]), many_user.items()))

rental_book(user_info)
