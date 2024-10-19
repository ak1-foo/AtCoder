N = int(input())
A = list(map(int, input().split()))

q = []
for a in A:
    q.append(a)
    while len(q) > 1:
        last = q.pop()
        append = q.pop()
        if last == append:
            q.append(last+1)
        else:
            q.append(append)
            q.append(last)
            break

print(len(q))
