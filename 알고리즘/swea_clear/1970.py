# 쉬운 거스름돈

T = int(input())

for t in range(T):
    money = int(input())
    change = [0,0,0,0,0,0,0,0]  # 50000, 10000, 5000, 1000, 500, 100, 50, 10

    now_change = 0

    while now_change <= money:
        now_change += 50000
        change[0] += 1
        if now_change > money:
            now_change -= 50000
            change[0] -= 1
            break
    
    while now_change <= money:
        now_change += 10000
        change[1] += 1
        if now_change > money:
            now_change -= 10000
            change[1] -= 1
            break
    
    while now_change <= money:
        now_change += 5000
        change[2] += 1
        if now_change > money:
            now_change -= 5000
            change[2] -= 1
            break
    
    while now_change <= money:
        now_change += 1000
        change[3] += 1
        if now_change > money:
            now_change -= 1000
            change[3] -= 1
            break
    
    while now_change <= money:
        now_change += 500
        change[4] += 1
        if now_change > money:
            now_change -= 500
            change[4] -= 1
            break

    while now_change <= money:
        now_change += 100
        change[5] += 1
        if now_change > money:
            now_change -= 100
            change[5] -= 1
            break
    
    while now_change <= money:
        now_change += 50
        change[6] += 1
        if now_change > money:
            now_change -= 50
            change[6] -= 1
            break
    
    while now_change <= money:
        now_change += 10
        change[7] += 1
        if now_change > money:
            now_change -= 10
            change[7] -= 1
            break
    
    print(f"#{t+1}")
    print(*change)
    