# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [(list(map(int, input().split()))) for _ in range(n)]

    point = 0
    ans_plus = []
    ans_cross = []

    for i in range(n):
        for j in range(n):
            point = matrix[i][j]
            plus = []
            cross = []
            sum_plus = 0
            sum_cross = 0
            
            for k in range(1, m):
                a = i - k
                b = j - k
                c = i + k
                d = j + k

                

                # 십자모양
                if a >= 0:
                    plus.append(matrix[i-k][j]) # 상
                if c < n:
                    plus.append(matrix[i+k][j]) # 하
                if b >= 0:
                    plus.append(matrix[i][j-k]) # 좌
                if d < n:
                    plus.append(matrix[i][j+k]) # 우

                # X자모양
                if a >= 0 and b >= 0:
                    cross.append(matrix[i-k][j-k]) # 11시
                if a >= 0 and d < n:
                    cross.append(matrix[i-k][j+k]) # 01시
                if c < n and d < n:
                    cross.append(matrix[i+k][j+k]) # 05시
                if c < n and b >= 0:
                    cross.append(matrix[i+k][j-k]) # 07시
                # print(cross)
                sum_plus = sum(plus) + point
                sum_cross = sum(cross) + point
            ans_plus.append(sum_plus)
            ans_cross.append(sum_cross)
    
    if max(ans_plus) > max(ans_cross):
        print('#{0} {1}' .format(t+1, max(ans_plus)))
    else:
        print('#{0} {1}' .format(t+1, max(ans_cross)))        
        
                