S = input()

current_idx = S.find('A')

sum_distance = 0
for i in range(1, 25+1):
    idx = S.find(chr(ord('A')+i))
    sum_distance += abs(idx - current_idx)
    current_idx = idx

print(sum_distance)
