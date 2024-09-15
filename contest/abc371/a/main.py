Sab, Sac, Sbc = input().split()

ans = ''

# a < b < c
if Sab == '<' and Sac == '<' and Sbc == '<':
    ans = 'B'
# a < c < b
elif Sab == '<' and Sac == '<' and Sbc == '>':
    ans = 'C'
# b < a < c
elif Sab == '>' and Sac == '<' and Sbc == '<':
    ans = 'A'
# b < c < a
elif Sab == '>' and Sac == '>' and Sbc == '<':
    ans = 'C'
# c < a < b
elif Sab == '>' and Sac == '>' and Sbc == '>':
    ans = 'B'
# c < b < a
else:
    ans = 'A'

print(ans)
