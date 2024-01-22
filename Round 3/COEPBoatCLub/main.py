import math
x = int(input())
s = list(map(int, input()))
p = 0
n = math.ceil(x/2)
for i in range(n):
  m = sum(s[i:i+n])
  p = max(m, p)
for i in range(n, x):
    m = sum(s[i:i+n]) - s[i-n]
    p = max(p, m)
print(p)