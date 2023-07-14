T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [(list(map(int, input().split()))) for _ in range(n)]

    # print(matrix)
    point = 0  # 시작점

    ans_ten = []
    ans_cross = []

    for i in range(n):
        for j in range(n):
            point = matrix[i][j]
            # sum += point

            ten = []
            cross = []
            for k in range(1, m):
                try:
                    a = i - k
                    if a < 0:
                        a = 100
                    b = j - k
                    if b < 0:
                        b = 100
                    c = i + k
                    if c > n - 1:
                        c = 100
                    d = j + k
                    if d > n - 1:
                        d = 100
                    up = matrix[a][j]
                    print(up)
                    down = matrix[c][j]
                    left = matrix[i][b]
                    right = matrix[i][d]
                    ten.append(up)
                    ten.append(down)
                    ten.append(left)
                    ten.append(right)

                    time_11 = matrix[a][b]
                    time_01 = matrix[a][d]
                    time_05 = matrix[c][d]
                    time_07 = matrix[c][b]
                    cross.append(time_11)
                    cross.append(time_01)
                    cross.append(time_05)
                    cross.append(time_07)
                except:
                    continue

            sum_ten = sum(ten, point)
            sum_cross = sum(cross, point)
            # print(sum_ten)
            # print(sum_cross)
            ans_ten.append(sum_ten)
            ans_cross.append(sum_cross)

    if max(ans_ten) >= max(ans_cross):
        print('#{0} {1}'.format(t + 1, max(ans_ten)))
    else:
        print('#{0} {1}'.format(t + 1, max(ans_cross)))