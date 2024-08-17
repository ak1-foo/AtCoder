t_call, t_sleep, t_wake = map(int, input().split())

ans = ''
# 起きてる時間で分岐
if (t_wake < t_sleep):
    if (t_wake < t_call < t_sleep):
        ans = 'Yes'
    else:
        ans = 'No'
else: # 日をまたいで起きている
    if (t_call > t_wake): # 起きた日に叫ぶ
        ans = 'Yes'
    elif (t_call < t_sleep): # 起きた次の日に叫ぶ
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)
