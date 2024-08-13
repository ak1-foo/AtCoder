n = int(input())
dn_list = []

for _ in range(n):
    dn_list.append(int(input()))

dn_list.sort(reverse=True)
height = 0
for i,dn in enumerate(dn_list):
    if (i == 0):
        height += 1
        most_recent_mochi = dn
        continue

    if (dn < most_recent_mochi):
        height += 1
        most_recent_mochi = dn

print(height)
