K, G, M = map(int, input().split())

glass_ml, magcup_ml = 0, 0

for _ in range(K):
    if glass_ml == G:
        glass_ml = 0
    elif magcup_ml == 0:
        magcup_ml = M
    else:
        pour = min(G - glass_ml, magcup_ml)
        glass_ml += pour
        magcup_ml -= pour

print(glass_ml, magcup_ml)
