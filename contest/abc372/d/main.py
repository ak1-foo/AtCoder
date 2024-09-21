# WA
# timeover

N = int(input())
H = list(map(int, input().split()))

buildings = []
# for i, h in enumerate(H):
#     if i == N-1:
#         buildings.append({'idx': i+1, 'height': h, 'score': 0})
#     else:
#         buildings.append({'idx': i+1, 'height': h, 'score': 1})

score = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    if i == N-1:
        score[i] = 0
    else:
        if H[i] >= H[i+1]:
            score[i] = score[i+1] + 1
        else:
            score[i] = score[i+1]

print(*score)
