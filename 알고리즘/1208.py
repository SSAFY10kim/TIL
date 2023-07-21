import sys

sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

for t in range(10):
    num = int(input())      # 덤프 횟수

    arr = list(map(int, input().split()))
    arr_set = list(set(arr))    # 크기순 정렬, 오름차순, 중복제거

    for _ in range(num):
        a = 0
        if min(arr) == arr_set[a]:
            # big_num = arr[arr.index(max(arr))]
            # sm_num = arr[arr.index(min(arr))]

            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
        else:
            a += 1
    ans = arr[arr.index(max(arr))]- arr[arr.index(min(arr))]

    print(f"#{t+1} {ans}")
