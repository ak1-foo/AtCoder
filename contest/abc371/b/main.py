N, M = map(int, input().split())

# 太郎を生んだ家の番号を格納
set_taro = set()

for _ in range(M):
    a, b = input().split()
    a = int(a)

    if a not in set_taro and b == 'M':
        print('Yes')
        set_taro.add(a)
    else:
        print('No')
