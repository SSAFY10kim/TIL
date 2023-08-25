def sol(lst):
    if len(lst) == 1:
        return lst[0]  # 하나의 풍선만 있는 경우, 해당 풍선의 점수가 최대 점수가 됨
    if len(lst) == 2:
        return max(lst[0], lst[1]) * 2  # 두 풍선 중 더 큰 점수를 선택하고 2를 곱한 것이 최대 점수
    if len(lst) == 3:
        case1 = lst[1] * 3  # 가운데 풍선을 터트릴 경우의 점수
        case2 = lst[2] * lst[0] + (lst[0] * 2)  # 왼쪽 풍선을 선택하고 양 옆 풍선을 터트릴 경우의 점수
        case3 = lst[2] * lst[0] + (lst[2] * 2)  # 오른쪽 풍선을 선택하고 양 옆 풍선을 터트릴 경우의 점수
        return max(case1, case2, case3)  # 세 경우 중에서 가장 큰 점수를 선택

    # 앞쪽 풍선부터 터트리기
    score = lst[1]  # 첫 번째 풍선을 터트렸을 때의 점수
    lst_copy = lst.copy()
    lst_copy.pop(0)  # 첫 번째 풍선을 터트리고 리스트에서 제거
    score1 = sol(lst_copy) + score  # 남은 풍선들을 터트려 얻는 점수와 합쳐서 최대 점수 계산

    # 뒤쪽 풍선부터 터트리기
    score = lst[-2]  # 마지막에서 두 번째 풍선을 터트렸을 때의 점수
    lst_copy = lst.copy()
    lst_copy.pop(len(lst)-1)  # 마지막에서 두 번째 풍선을 터트리고 리스트에서 제거
    score2 = sol(lst_copy) + score  # 남은 풍선들을 터트려 얻는 점수와 합쳐서 최대 점수 계산

    max_ = 0
    # 가운데
    for i in range(1, len(lst)-1):
        score = lst[i-1] * lst[i+1]  # 가운데 풍선을 터트렸을 때의 점수
        lst_copy = lst.copy()
        lst_copy.pop(i)  # 가운데 풍선을 터트리고 리스트에서 제거
        score3 = sol(lst_copy) + score  # 남은 풍선들을 터트려 얻는 점수와 합쳐서 최대 점수 계산
        if max_ < score3:
            max_ = score3  # 가장 큰 점수를 업데이트
    return max(max_, score1, score2)  # 세 가지 방법 중 가장 큰 점수를 선택

# 테스트 케이스의 개수를 입력 받음
T = int(input())
for t in range(1, T + 1):
    n = int(input())  # 순열의 길이
    lst = list(map(int, input().split()))  # 순열의 원소들을 입력 받음
    result = sol(lst)  # 최대 점수 계산
    print(f'#{t} {result}')  # 결과 출력