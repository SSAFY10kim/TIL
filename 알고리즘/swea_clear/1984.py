# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    total_lst = list(map(int, input().split()))

    total_lst = sorted(total_lst)
    avg_lst = total_lst[1:9]

    ans = (sum(avg_lst) / len(avg_lst))

    print(f'#{t+1} {ans:.0f}')