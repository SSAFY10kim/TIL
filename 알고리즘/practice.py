T = int(input())

for t in range(T):
    sdo = []

    for i in range(9):
        sdo.append(list(map(int, input().split())))

    for r in range(9):
        ans_r = 0
        row_set = []
        row_set = set(sdo[r])

        if len(row_set) == 9:
            ans_r = 1
        else:
            ans_r = 0
            break
    col = []
    col_set = []
    for c1 in range(9):
        ans_c = 0
        c2 = 0
        col.append(sdo[c1][c2])
        col_set = set(col)

        c2 += 1
        if len(col_set) == 9:
            ans_c = 1
        else:
            ans_c = 0
            break

    m1_list = []
    m1_set = []
    for m1 in range(3):
        num = 0
        ans_m = 0
        for m2 in range(3):
            m1_list.append(sdo[num + m1][num + m2])

        m1_set = set(m1_list)
        num += 3

        if len(m1_set) == 9:
            ans_m = 1
        else:
            ans_m = 0
            break

    if ans_r == 1 and ans_c == 1 and ans_m == 1:
        ans = 1
    else:
        ans = 0

    print('#{0} {1}'.format(t + 1, ans))