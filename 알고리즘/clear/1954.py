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
        
        for _ in range(count):          # 아래진행
            goal_mat[row][col] = num 
            num += 1
            row += 1
        for _ in range(count):          # 좌측진행
            goal_mat[row][col] = num
            num += 1
            col -= 1
        
        if count - 1 == 0:              # 범위 0이면 탈출
            goal_mat[row][col] = num
            break
        
        for _ in range(count-1):        # 위쪽진행
            goal_mat[row][col] = num
            num += 1
            row -= 1
        for _ in range(count-1):        # 우측진행
            goal_mat[row][col] = num
            num += 1
            col += 1
        
        goal_mat[row][col] = num        # 탈출시 탈출

    print("#{}" .format(t+1))
    for i in goal_mat:                  # 리스트 풀어서 출력하기
        for j in i:
            print(j, end=' ')
        print()