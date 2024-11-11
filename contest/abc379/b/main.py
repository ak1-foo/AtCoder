N, K = map(int, input().split())
S = input()

def is_safe_teeth(start, end):
    for i in range(start, end):
        if S[i] == 'X':
            return False

    return True

i = 0
ans = 0
while i < N-K+1:
    if is_safe_teeth(i, i+K):
        ans += 1
        i += K
    else:
        i += 1

print(ans)
