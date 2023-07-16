import sys

sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]            # 2중 리스트 입력받는법 항상 기억해둘것

    kill_number = []
    for i in range(n):
        for j in range(n):
            kill = []
            point = matrix[i][j]

            for row in range(1,m-1):
                for col in range(1,m-1):
                    if (i + row) > (n - 1) or  (j + col) > (n - 1):
                        continue
                    kill.append(matrix[i+row][j+col])
        print(kill)
        kill_number.append(sum(kill) + point)
    
    print("#{} {}" .format(t+1, max(kill_number)))