# WA
N = int(input())
P = list(map(int, input().split()))


embed = [("start", 0)]

for i in range(1, N - 1):
    if P[i - 1] < P[i] and P[i] > P[i + 1]:
        embed.append(("mount", i))
    elif P[i - 1] > P[i] and P[i] < P[i + 1]:
        embed.append(("valley", i))

embed.append(("end", N - 1))


ans_area = []
for i in range(1, len(embed) - 2):
    if (
        embed[i][0] != embed[i + 1][0]
        and embed[i][0] == "mount"
        and embed[i + 1][0] == "valley"
    ):
        ans_area.append(
            {
                "area": (embed[i - 1][1], embed[i + 2][1]),
                "mount_valley_idx": (embed[i][1], embed[i + 1][1]),
            }
        )

ans = 0
for area in ans_area:

    area_len = area["area"][1] - area["area"][0]
    if area_len < 4:
        continue

    left_margin = area["mount_valley_idx"][0] - area["area"][0]
    right_margin = area["area"][1] - area["mount_valley_idx"][1]

    # A1 < A2
    valid_left_margin = 0
    for i in range(left_margin):
        A1_idx = area["area"][0] + i
        A2_idx = A1_idx + 1
        if P[A1_idx] < P[A2_idx]:
            valid_left_margin += 1

    ans += valid_left_margin * right_margin


print(ans)
