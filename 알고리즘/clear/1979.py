# import sys

# sys.stdin = open(r'C:\Users\PC1\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    # print(matrix)           # 입력값 검증

    ans = 0
    result = []
    for i in range(n):                      # 오른쪽 순회
        count = 0
        for j in range(n):
            pointer = matrix[i][j]          # 포인터 이동
            if pointer == 1:                # 포인터가 1이면
                count += 1                  # count += 1
            else:                       
                result.append(count)        # 0을 만나면 1만 있던 길이 반환
                count = 0                   # count 초기화
        
        result.append(count)                # 마지막칸이 1인 경우 count 반환 필수
                
    for i in range(n):                      # 아래쪽 순회
        count = 0                       
        for j in range(n):                          
            pointer = matrix[j][i]  
            if pointer == 1:                # 포인터가 1이면
                count += 1                  # count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)                # 역시 마지막칸이 1인경우 count 반환 필수
    
    for i in result:                        # 저장되어있는 길이 중 길이가 m인갯수 반환
        if i == m:
            ans += 1

    print(f'#{t+1} {ans}')    
                    