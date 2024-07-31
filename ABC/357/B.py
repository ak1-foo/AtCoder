S = input()

num_lower_case = 0
num_upper_case = 0
for char in S:
    if 'a' <= char <= 'z':
        num_lower_case += 1
    elif 'A' <= char <= 'Z':
        num_upper_case += 1

if num_lower_case < num_upper_case:
    print(S.upper())
else:
    print(S.lower())
