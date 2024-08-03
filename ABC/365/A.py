from calendar import isleap

year = int(input())

if isleap(year):
    ans = 366
else:
    ans = 365

print(ans)
