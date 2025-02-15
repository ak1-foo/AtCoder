S = list(input().split())

ans = -1
if S[0] == "sick" and S[1] == "sick":
    ans = 1
elif S[0] == "sick" and S[1] == "fine":
    ans = 2
elif S[0] == "fine" and S[1] == "sick":
    ans = 3
else:
    ans = 4

print(ans)
