import itertools

N, K = map(int, input().split())
Rn = list(map(int, input().split()))

compinations = list(itertools.product(range(1, 5+1), repeat=N))
compinations.sort()

for compination in compinations:
    if sum(compination) % K != 0:
        continue
    
    correct_flag = True
    for i, element in enumerate(compination):
        if not (1 <= element <= Rn[i]):
            correct_flag = False
            break

    if (correct_flag == True):
        print(*compination)