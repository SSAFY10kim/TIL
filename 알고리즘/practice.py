# import sys

# sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(1, T+1):
    num = int(input())

    number = list(map(int, input()))

    num_lst = [0,1,2,3,4,5,6,7,8,9]
    num_count = [0,0,0,0,0,0,0,0,0,0]

    for n in number:
        num_count[n] += 1
    
    for c in num_count:
        max_count = num_count[0]
        if c > max_count:
            max_count = c
    
    print(f'#{t} {num_count.index(c)} {c}')