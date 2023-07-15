# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')
T = int(input())

for t in range(T):
    n = int(input()) # n개의 가격

    sales = (list(map(int, input().split()))) # 가격표를 리스트로 받을것

    goal = 0
    count = 0
    mid_sum = 0
    money = []
    goal = sales[n-1]

    for j in range(n-2,-1,-1):  # 뒤에서부터
        if sales[j] > goal:     # 더 큰 값이 있으면 변경해주기
            goal = sales[j]
   
        else:                   # 중간값에 더해주기(goal값 변경 X)
            mid_sum += goal - sales[j]

    print('#{} {}' .format(t+1, mid_sum))

# 뒤에서부터 순회하면 쉽게 해결가능
# 런타임 에러 조심(input 100만개)
# 반복문 최소화 할것!
