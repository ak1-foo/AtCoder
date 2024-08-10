N, T, A = map(int, input().split())

if (T > N/2 or A > N/2):
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
