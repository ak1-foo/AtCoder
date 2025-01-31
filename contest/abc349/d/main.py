L, R = map(int, input().split())


def devide_2(x):
    if x == 0:
        return 61, 0
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1

    return count, x


ans = []
current = L
while current < R:
    two, remain = devide_2(current)
    while two >= 0:
        next = (2**two) * (remain + 1)
        if next <= R:
            ans.append((current, next - 1))
            current = next
            break
        two -= 1
        remain *= 2

print(len(ans))
for a in ans:
    print(a[0], a[1] + 1)
