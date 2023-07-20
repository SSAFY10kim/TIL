# import sys

# sys.stdin = open(r'C:\Users\SSAFY\Desktop\TIL\알고리즘\input.txt','r')

T = int(input())

for t in range(T):
    word = input()
    ans = 0
    for i in range(1, len(word)):
        if word[:i] == word[i:i+i]:
            ans = i
            break
    
    print(f'#{t+1} {ans}')


        

        