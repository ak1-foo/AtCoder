N = int(input())
P = list(map(int, input().split()))
P = [p - 1 for p in P]

Q = list(map(int, input().split()))
Q = [q - 1 for q in Q]

id_to_gaze_target_id = [-1] * N
id_to_bib = [-1] * N
bib_to_id = [-1] * N
for i in range(N):
    id_to_gaze_target_id[i] = P[i]
    id_to_bib[i] = Q[i]
    bib_to_id[Q[i]] = i


ans = []
for i in range(N):
    ans.append(id_to_bib[id_to_gaze_target_id[bib_to_id[i]]] + 1)

print(*ans)
