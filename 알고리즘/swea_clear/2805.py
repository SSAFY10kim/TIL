# # 농작물 수확하기
# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    matrix = []
    num = int(input())

    for _ in range(num):
        row = list(input())
        matrix.append(list(map(int, row)))
    
    # print(matrix)
    my_lst = []
    cen = num // 2
    for i in range(cen+1):    # 위에서 아래로
        left = cen - i
        right = cen + i
        
        if left == right:
            my_lst.append(matrix[i][cen])
        else:
            my_lst.extend(matrix[i][left:right+1])
    
    for i in range(cen+1, num):
        left = i - cen
        right = num - 1 - (i-cen)

        if left == right:
            my_lst.append(matrix[i][cen])
        else:
            my_lst.extend(matrix[i][left:right+1])

    ans = sum(my_lst)

    print(f'#{t+1} {ans}')