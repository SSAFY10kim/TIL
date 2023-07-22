# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

for t in range(10):
    num = int(input())      # 덤프 횟수

    arr = list(map(int, input().split()))
    arr_set = list(set(arr))    # 크기순 정렬, 오름차순, 중복제거

    for _ in range(num):
        a = arr.count(min(arr))
        if a != 0: 
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
            
    ans = max(arr)- min(arr)

    print(f"#{t+1} {ans}")
