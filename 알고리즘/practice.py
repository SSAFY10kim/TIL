T = int(input())

for t in range(T):
    n = int(input())

    goal_mat = []
    for i in range(0,n*n,n):
        mat = []
        for j in range(n):
            mat.append(i + j + 1)
        goal_mat.append(mat)

    num = n

    row = 0
    col = n-1

    for count in range(n-1,-1,-2):
        if count == 0:
            break
        
        for _ in range(count):
            goal_mat[row][col] = num
            num += 1
            row += 1
        for _ in range(count):
            goal_mat[row][col] = num
            num += 1
            col -= 1
        
        if count - 1 == 0:
            goal_mat[row][col] = num
            break
        
        for _ in range(count-1):
            goal_mat[row][col] = num
            num += 1
            row -= 1
        for _ in range(count-1):
            goal_mat[row][col] = num
            num += 1
            col += 1
        
        goal_mat[row][col] = num

    print("#{}" .format(t+1))
    for i in goal_mat:
        for j in i:
            print(j, end=' ')
        print()