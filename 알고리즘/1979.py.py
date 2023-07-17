import sys

sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    # print(matrix)           # 입력값 검증

    ans = 0

    for i in range(n):
        for j in range(n):
            count = 0
            pointer = matrix[i][j]        # 포인터 이동
            if pointer == 1:
                for right in range(n):
                    if (j + right) > n-1:
                        continue

                    if matrix[i][j + right] == 1:
                        count += 1
                    else:
                        break
                if count == m:
                    ans += 1
                    count = 0
                
                
                for down in range(n):
                    if (i + down) > n-1:
                        continue

                    if matrix[i+down][j] == 1:
                        count += 1
                    else:
                        break
                if count == m:
                    ans += 1
                    
                    
    print(f'#{t+1} {ans}')
                    