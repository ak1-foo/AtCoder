import math

x = float(input())

i, f = math.modf(x)
if i == 0:
    ans = int(x)
else:
    ans = x
    
print(ans)
