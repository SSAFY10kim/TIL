class Person:
    gene = 'XYZ'
    
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):

    def swim(self):
        return '엄마가 수영'
    
class Dad(Person):

    def walk(self):
        return '아빠가 걷기'
    
class FirstChild(Dad, Mom): # 클래스 변수 X, 부모class꺼 받아옴
    def swim(self):         # 재정의, 덮어쓰기?
        return '첫째가 수영'
    
    def cry(self):          # 없던거, 본인 메서드
        return '첫째가 응애'
    
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene)   # XY    상속 순서가 Dad,Mom 이니까 첫번째 클래스의 변수 받아옴
print(FirstChild.mro())