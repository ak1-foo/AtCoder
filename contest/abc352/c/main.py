N = int(input())

heights = []

for _ in range(N):
    shoulder_height, all_height = map(int, input().split())
    head_height = all_height - shoulder_height
    heights.append({'shoulder': shoulder_height, 'head': head_height})

sum_shoulder = sum([h['shoulder'] for h in heights])
max_head = max([h['head'] for h in heights])

max_height = sum_shoulder + max_head
print(max_height)
