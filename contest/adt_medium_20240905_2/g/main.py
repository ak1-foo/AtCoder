S = input()

box = []
depth = 0
for s in S:
    if s == '(':
        depth += 1
    elif s == ')':
        box = [item for item in box if item['depth'] != depth]
        depth -= 1
    else:
        if any(item['char'] == s for item in box):
            print('No')
            exit()
        box.append({'depth': depth, 'char': s})

print('Yes')
