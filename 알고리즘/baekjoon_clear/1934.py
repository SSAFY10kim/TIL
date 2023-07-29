def gcd(x, y):                  # 유클리드 호제법(최대공약수)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
def lcm(x, y):                  # 유클리드 호제법(최소공배수)
    result = (x*y) // gcd(x,y)  # 최소 공배수 = 두수의 곱 // 최대공약수
    return result

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if b > a:
        a, b = b, a

    print(lcm(a,b))

    
    
