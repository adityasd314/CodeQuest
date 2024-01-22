def count(sub, a, b):
    a -= 1
    b -= 1
    blueInSub = 0
    a,b = (a,b) if a < b else( b,a)
    diff = b - a
    length = len(sub)
    
    a = a % length
    b = a + diff
    blue = 0
    
    for i in range(0, length):
        if(sub[i] == 'B'):
            blueInSub+=1
            if(i >= a):
                blue+=1
    
    blue += blueInSub*((b - length + 1) // length)
    for i in range(0,((b-length + 1)%length)):
        if(sub[i] == 'B'):
            blue+=1
    return blue

pattern = input().strip()
i, j = map(lambda x: int(x),input().split())

result = count(pattern, i, j)
print(result)
