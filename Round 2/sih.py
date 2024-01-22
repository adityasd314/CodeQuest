n, p = map(lambda x: int(x), input().split())
arr = list( map(lambda x: int(x), input().split()))
arr.sort()
kth_largest = arr[p - 1]
hours = 0

for i in range(n):
    if i >= p:
        break
    hours += (kth_largest - arr[i])
print(hours)
    
