T = int(input())

di = [-1,0,1,0]
dj = [0,1,0,-1]     # 상우하좌

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    MAX = 0             # 최대값
    MIN = 987654321     # 최소값

    for i in range(n):
        for j in range(n):
            score = arr[i][j]   # score + 해당 칸의 점수
            for k in range(4):  # 4방향
                for l in range(1, arr[i][j] + 1):   # 주위 1칸부터 점수만큼 증가
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < n and 0 <= nj < n: # 범위를 벗어나지 않는다면
                        score += arr[ni][nj]        # 점수 +
            if MAX < score:     # 최고점
                MAX = score
            if MIN > score:     # 최저점
                MIN = score

    print(f'#{t} {MAX-MIN}')