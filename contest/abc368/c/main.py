N = int(input())
enemy_health = list(map(int, input().split()))

turn = 0
next_enemy = 0

for h in enemy_health:
    # 3ターン以内に倒せるように相手の体力を調整
    if h > 1+1+3:
        turn += (h // (1+1+3)) * 3
        h = h % (1+1+3)
    
    # 倒れるまで攻撃
    while h > 0:
        turn += 1
        if turn % 3 == 0:
            h -= 3
        else:
            h -= 1

print(turn)
