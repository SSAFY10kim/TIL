T = int(input())

for t in range(T):
    time = list(map(int, input().split()))

    ans_time = []
    ans_time.append(time[0] + time[2])
    ans_time.append(time[1] + time[3])

    while ans_time[1] >= 60:
        ans_time[1] -= 60
        ans_time[0] += 1

    if ans_time[0] > 12:
        ans_time[0] -= 12

    print(f"#{t+1}" ,end=' ')
    print(*ans_time)
    