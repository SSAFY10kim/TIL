# import sys

# sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    num = int(input())

    v = 0
    l = 0

    for c in range(num):
        s_a = input().split()
        s = int(s_a[0])

        try:                        # try-except 예외처리 사용
            a = int(s_a[1])         # s = 0일때, a값 없음
        except IndexError:          # 에스테리스크로 안되느 이유?
            a = v

        if s == 1:
            v += a
            l += v
        elif s == 2:
            v -= a
            if v <= 0:
                v = 0
            l += v
        else:
            l += v

    print(f'#{t+1} {l}')
