T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(input().split())
    odd = []        # 큐 = pop(0)
    even = []       # 스택 = pop()
    bonus = 0
    score_lst = [0] * 11    # 1~10번까지 인덱스 = 번호위해 사람수 + 1

    for i in range(n):
        if arr[i] == '+':   # 보너스 점수 +1
            bonus += 1

        if arr[i].isdigit():    # +가 아니라 숫자라면
            if (int(arr[i]) + bonus) % 2 == 0:  # 보너스 점수 더해서 홀수 큐, 짝수 스택에 추가
                even.append(int(int(arr[i]) + bonus))
            else:
                odd.append((int(arr[i]) + bonus))

    score_B, score_C = 0, 0
    for i in range(1, 11):
        if len(even) == 0 and len(odd) == 0:    # 스택, 큐가 모두 비었으면 더이상 점수 획득 X
            break                               # 반복문 의미 X, 반목문 탈출

        if odd:                                 # 홀수 큐에 숫자가 있을 때
            score_B = odd.pop(0)                # 가장 앞의, front의 점수 꺼낸다
        elif not odd:                           # 큐가 비어있으면
            score_B = 0                         # 점수 = 0

        if even:                                # 짝수 스택에 숫자가 있을 때
            score_C = even.pop()                # 가장 뒤에서 꺼낸 수가 점수
        elif not even:                          # 스택이 비어있으면
            score_C = 0                         # 점수 = 0

        score_lst[i] = score_B + score_C        # 최종 i번의 점수

    print(f'#{t} {score_lst[m]}')               # 그중 m번 김싸피의 점수 출력