S = input()
S = list(S)
S.sort()
S = ''.join(S)

if S == 'ABC':
    print('Yes')
else:
    print('No')
