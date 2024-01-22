def optimal(strikes, n, h):
    minK = h//n + (1 if (h%n)!=0 else 0)
    poison = 0
    p = 1
    for i in range(1, len(strikes)):
        t2 = strikes[i]
        t1 = strikes[i-1]
        if(t2 - t1 < minK):
            poison += t2 - t1
        else:
            poison += minK
            p += 1
    if(poison >= h):
        return minK
    else:
        poison -= minK* (p-1)
        h -= poison
        return h//p + h%p




t = int(input())
for i in range(t):
    n, h = map(lambda x: int(x),input().split())
    strikes = list(map(lambda x: int(x),input().split()))
    k = optimal(strikes, n, h)
    print(k)
