# WA
N, M = map(int, input().split())
prohibited = []
for i in range(N):
    l, r = map(int, input().split())
    prohibited.append({'l': l, 'r': r, 'index': i})

L = []
for i in range(N):
    L.append({'l': prohibited[i]['l'], 'index': i})
L.sort(key=lambda x: x['l'])
R = []
for i in range(N):
    R.append({'r': prohibited[i]['r'], 'index': i})
R.sort(key=lambda x: x['r'], reverse=True)

count = 0
last = {'l': -1, 'r': M}
for l in L:
    print(f'last: {last}, l: {l}')
    count += (l['l'] - last['l']) * (M - R[0]['r'])
    last['l'] = l['l']
    # Rの中で、lとindexが一致するrを取り除く
    for i, r in enumerate(R):
        if r['index'] == l['index']:
            R.pop(i)
            print(f'R: {R}')
            break

print(count)
