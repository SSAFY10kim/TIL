def calScore(l):
    s = 0
    if len(l) == 1:
       return l[0]
    if len(l) == 2:
        return 2 * max(l[0], l[1])
    if len(l) == 3:
        a = l[1] * 3
        b = l[0] * l[2] + l[0] * 2
        c = l[0] * l[2] + l[2] * 2
        return max(a,b,c)
    s = l[1]
    l1 = l.copy()
    l1.pop(0)
    s1 = calScore(l1) + s

    s = l[len(l) -2]
    l1 = l.copy()
    l1.pop(len(l) - 1)
    s2 = calScore(l1) + s

    max1 = 0
    for i in range(1, len(l)-1):
        s = l[i-1] * l[i+1]
        l1 = l.copy()
        l1.pop(i)
        s3 = calScore(l1) + s
        if s3 > max1:
            max1 = s3

    return max(max1, s1, s2)

t = int(input())
for i in range(t):
    print("#", end = "")
    print(i + 1, end = " ")
    n = int(input())
    l = list(map(int, input().split()))
    print(calScore(l))