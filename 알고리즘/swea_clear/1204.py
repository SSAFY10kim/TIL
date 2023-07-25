# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for _ in range(T):
    t = int(input())            # 테케 번호

    score = list(map(int, input().split()))

    a = 0
    score_list = []
    for i in range(1000):
        d = score[i]            # 숫자별로
        a = score.count(d)      # 갯수 count
        score_list.append(a)    # 모든 경우 list 등록

    b = max(score_list)         # 가장 높은 갯수 찾기

    c = score_list.index(b)     # 가장 높은 count의 위치를 찾아서
    ans = score[c]              # 원래의 리스트에서 해당 위치의 숫자를 찾아 낸다.

    print("#{} {}" .format(t, ans))