# 간단한 396 게임
num = int(input())
ans = []

point = 0
for i in range(1, num+1):               # num 까지 리스트 작성
    test = (list(map(int, str(i))))     # 각 숫자를 분리해서 list로 받음

    count_sum = test.count(3) + test.count(6) + test.count(9)   # 각 자리별로 369 포함되는지 카운트

    if count_sum > 0:                   # 만약 카운트가 1이라도 있다면 카운트 수만큼 - 추가
        ans.append("-" * count_sum)     
    else:                               # 카운트가 0이라면 i만 축
        ans.append(i)

print(*ans)                             # 리스트 언팩킹하여 정답 반환
