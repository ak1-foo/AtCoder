S = input()

cursor = 0
while True:
    # 1: dream, 2: dreamer, 3: erase, 4: eraser, 5: null
    # 見るべきは、*d* ream, *e* r *a* se
    # 4*5=20通り

    # 11, 12
    if (S[cursor : cursor+len('dreamd')] == 'dreamd'):
        cursor += len('dream')
        continue
    # 13, 14
    if (S[cursor : cursor+len('dreamera')] == 'dreamera'):
        cursor += len('dream')
        continue

    # 21, 22
    if (S[cursor : cursor+len('dreamerd')] == 'dreamerd'):
        cursor += len('dreamer')
        continue
    # 23, 24
    if (S[cursor : cursor+len('dreamere')] == 'dreamere'):
        cursor += len('dreamer')
        continue

    # 31, 32
    if (S[cursor : cursor+len('erased')] == 'erased'):
        cursor += len('erase')
        continue
    # 33, 34
    if (S[cursor : cursor+len('erasee')] == 'erasee'):
        cursor += len('erase')
        continue

    # 41, 42
    if (S[cursor : cursor+len('eraserd')] == 'eraserd'):
        cursor += len('eraser')
        continue
    # 43, 44
    if (S[cursor : cursor+len('erasere')] == 'erasere'):
        cursor += len('eraser')
        continue

    # 最後に関して、末尾erを優先して検査
    # 25
    if (S[cursor : cursor+len('dreamer')] == 'dreamer' and cursor+len('dreamer') == len(S)):
        break
    # 15
    if (S[cursor : cursor+len('dream')] == 'dream' and cursor+len('dream') == len(S)):
        break
    # 45
    if (S[cursor : cursor+len('eraser')] == 'eraser' and cursor+len('eraser') == len(S)):
        break
    # 35
    if (S[cursor : cursor+len('erase')] == 'erase' and cursor+len('erase') == len(S)):
        break


    # 見つからなかった
    print('NO')
    exit()

# 見つかった
print('YES')
