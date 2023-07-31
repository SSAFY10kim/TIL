# 원재의 메모리 복구하기
import sys

sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    memory = list(map(str, input()))

    count = 0
    for i in range(1, len(memory)):
        if memory[i-1] != memory[i]:
            count += 1
        
    if memory[0] == '1':
        count += 1
    
    print(f"#{t+1} {count}")
