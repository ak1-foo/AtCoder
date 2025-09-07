# 7-min delay

S = input()
world, stage = map(int, (S[0], S[2]))

if stage == 8:
    world += 1
    stage = 1
else:
    stage += 1

print(f"{world}-{stage}")
