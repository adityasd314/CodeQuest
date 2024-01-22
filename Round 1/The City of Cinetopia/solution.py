def max_ent(n, m, d, a, idx, cnt, selected_movies):
    if idx == n or m == 0:
        return 0
    
    current = a[idx] - d * (cnt+1) + max_ent(n, m - 1, d, a, idx + 1, 0, selected_movies + [idx + 1])
    
    rem = max_ent(n, m, d, a, idx + 1, cnt + 1, selected_movies)
    
    return max(current, rem)
t = int(input())
results = []
for i in range(t):
    n, m, d = map(lambda x: int(x), input().split())
    a = list(map(lambda x: int(x), input().split()))

    result = max_ent(n, m, d, a, 0 ,0, [])
    results.append(result)
[print(result) for result in results]
