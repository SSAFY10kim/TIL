# 조교의 성적 매기기
import sys

sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    n, k = map(int, input().split())    # 10명 학생, k번째 학생의 학점?

    stu_score = []
    for i in range(n):
        score = list(map(int, input().split()))
        total = (score[0]*0.35)+(score[1]*0.45)+(score[2]*0.2)
        stu_score.append(total)
        sort_score = list(reversed(sorted(stu_score)))

    if stu_score[k-1] in sort_score[:n//10]:
        print(f"#{t+1} A+")
    elif stu_score[k-1] in sort_score[:(n//10)*2]:
        print(f"#{t+1} A0")
    elif stu_score[k-1] in sort_score[:(n//10)*3]:
        print(f"#{t+1} A-")
    elif stu_score[k-1] in sort_score[:(n//10)*4]:
        print(f"#{t+1} B+")
    elif stu_score[k-1] in sort_score[:(n//10)*5]:
        print(f"#{t+1} B0")
    elif stu_score[k-1] in sort_score[:(n//10)*6]:
        print(f"#{t+1} B-")
    elif stu_score[k-1] in sort_score[:(n//10)*7]:
        print(f"#{t+1} C+")
    elif stu_score[k-1] in sort_score[:(n//10)*8]:
        print(f"#{t+1} C0")
    elif stu_score[k-1] in sort_score[:(n//10)*9]:
        print(f"#{t+1} C-")
    else:
            print(f"#{t+1} D0")