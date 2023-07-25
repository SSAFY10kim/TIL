# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

for _ in range(10):
    t = int(input())
    arr = [(list(map(int, input().split()))) for _ in range(100)]

    max_sum = 0

    for i in range(100):
        if sum(arr[i]) >= max_sum:
            max_sum = sum(arr[i])
        
        arr_lst = []
        for j in range(100):
            arr_lst.append(arr[j][i])
            if sum(arr_lst) >= max_sum:
                max_sum = sum(arr_lst)

    arr_lst_cross = []
    arr_lst_cross2 = []
    for i in range(100):    
        arr_lst_cross.append(arr[i][i])
        if sum(arr_lst_cross) >= max_sum:
            max_sum = sum(arr_lst_cross)
        arr_lst = []
        arr_lst_cross2.append(arr[i][99-i])
        if sum(arr_lst_cross2) >= max_sum:
            max_sum = sum(arr_lst_cross2)
    
    print(f'#{t} {max_sum}')
