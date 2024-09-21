import re

N, Q = map(int, input().split())
S = input()
num_ABC = len(re.findall('ABC', S))

S = list(S)
S = ['-', '-'] + S + ['-', '-']
for _ in range(Q):
    idx, c = input().split()
    idx = int(idx) - 1
    idx += 2

#   if S[idx] == 'A':
#       if c == 'A':
#           continue
#       else:
#           S[idx] = 'A'
#           if idx < N-2:
#               if S[idx+1] == 'B' and S[idx+2] == 'C':
#                   num_ABC += 1
#
#   elif S[idx] == 'B':
#       if c == 'B':
#           continue
#       else:
#           S[idx] = 'B'
#           if 1 < idx < N-1:
#               if S[idx-1] == 'A' and S[idx+1] == 'C':
#                   num_ABC += 1
#
#   elif S[idx] == 'C':
#       if c == 'C':
#           continue
#       else:
#           S[idx] = 'C'
#           if idx > 1:
#               if S[idx-2] == 'A' and S[idx-1] == 'B':
#                   num_ABC += 1

    # idxから前後2文字を取得、前後2文字が存在しない場合は-で埋める
    change = S[idx-2:idx+3]

    change_pre = ''.join(change)
    change_post = change_pre[:2] + c + change_pre[3:]
    pre_num = len(re.findall('ABC', change_pre))
    post_num = len(re.findall('ABC', change_post))

    diff = post_num - pre_num
    num_ABC += diff

    S[idx] = c

    print(num_ABC)
