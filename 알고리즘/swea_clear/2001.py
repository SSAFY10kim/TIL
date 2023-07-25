# import sys

# sys.stdin = open(r'C:\Users\HOME\Desktop\practice\input.txt','r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]            # 2중 리스트 입력받는법 항상 기억해둘것
    
    kill_number = []
    for i in range(n):
        for j in range(n):
            kill = []
            # print(point)

            for row in range(0,m):                                          # row +
                for col in range(0,m):                                      # col +
                    if (i + row) > (n - 1) or  (j + col) > (n - 1):         # 초과 범위 제한
                        continue
                    # print(matrix[i+row][j+col])
                    kill.append(matrix[i+row][j+col])
            # print(kill)
            kill_number.append(sum(kill))
    
    print("#{} {}" .format(t+1, max(kill_number)))
