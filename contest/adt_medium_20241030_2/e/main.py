N = int(input())

# 0, 2, 4, 6, 8 の 5進数表記として考えられる

def base_n(x, n):
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % n))
        x //= n
    return ''.join(digits[::-1])

ans_5 = base_n(x=N-1, n=5)
ans = ''
for c in ans_5:
    if c == '0':
        ans += '0'
    elif c == '1':
        ans += '2'
    elif c == '2':
        ans += '4'
    elif c == '3':
        ans += '6'
    elif c == '4':
        ans += '8'
print(ans)
