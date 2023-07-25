class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second

class Morecal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            self.first / self.second

a = [1,2,3,4]
b = sum(a)
print(b)

c = Fourcal(4,2)
print(c.sum())      # 지역변수, 전역변수처럼 함수도 Scope 영향을 받는가?