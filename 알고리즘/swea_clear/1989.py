# 초심자의 회문 검사

T = int(input())

for t in range(T):
    my_str = list(input())
    ans = 0
    print(my_str)
    print(my_str[::-1])

    if (my_str) == (my_str[::-1]):
        ans = 1

    print(f"#{t+1} {ans}")