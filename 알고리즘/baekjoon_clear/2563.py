# 백준. 색종이

t = int(input())

arr = []
for _ in range(t):
    arr.append(list(map(int,input().split())))

    matrix = [[False for _ in range(100)]for _ in range(100)]
    count = 0
# print(matrix)
for a in range(len(arr)):
    for i in range(arr[a][0],arr[a][0]+10):
        for j in range(arr[a][1],arr[a][1]+10):
            if matrix[i][j] == False:
                matrix[i][j] = True
                count += 1

print(count)
