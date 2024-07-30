color_num = int(input())
people_color = list(map(int, input().split()))

cnt = 0
for i in range(2*color_num - 2):
    if people_color[i] == people_color[i+2]:
        cnt += 1

print(cnt)
