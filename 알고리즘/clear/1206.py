# import sys
# sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

for t in range(10):

    length = int(input())
    arr = list(map(int, input().split()))

    # print(arr) 입력 배열 검증

    ans = 0
    for i in range(2, length-2):
        comp = arr[i-2:i+3]
        if arr[i] != max(comp):
            continue
        
        sort_comp = list(reversed(sorted(comp)))
        # print(sort_comp)
        ans += (sort_comp[0] - sort_comp[1])
        
    print(f'#{t+1} {ans}')