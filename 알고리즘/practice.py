# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for _ in range(T):
    t = int(input())            # 테케 번호

    score = list(map(int, input().split()))

    a = 0
    score_list = []
    for i in range(1000):
        d = score[i]
        a = score.count(d)
        score_list.append(a)

    b = max(score_list)

    c = score_list.index(b)
    ans = score[c]

    print("#{} {}" .format(t, ans))