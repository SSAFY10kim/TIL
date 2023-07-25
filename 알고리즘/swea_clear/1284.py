# 1284. 수도 요금 경쟁

T = int(input())

for t in range(T):
    p, q, r, s, w = map(int, input().split())

    a_charge = p * w
    
    b_charge = 0
    if r >= w:
        b_charge = q
    else:
        b_charge = q + (w-r) * s
    
    if a_charge >= b_charge:
        print(f'#{t+1} {b_charge}')
    else:
        print(f'#{t+1} {a_charge}')