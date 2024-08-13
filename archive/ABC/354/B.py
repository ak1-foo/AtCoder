num_user = int(input())

users = []
for _ in range(num_user):
    S, C = input().split()
    users.append({"name": S, "rate": int(C)})

users.sort(key=lambda user: user["name"])

sum_rate = 0
for user in users:
    sum_rate += user["rate"]


ans = users[sum_rate % len(users)]["name"]

print(ans)
