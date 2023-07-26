# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self, num, my_str):
        self.num = num
        self.my_str = my_str

    def set_data(self, num, my_str):
        self.num = num
        self.my_str = my_str
    
    def repeat_string(self):
        for _ in range(self.num):
            print(self.my_str)

repeater1 = StringRepeater(3, "Hello")
repeater1.repeat_string()
repeater1.set_data(10,'a')
repeater1.repeat_string()
