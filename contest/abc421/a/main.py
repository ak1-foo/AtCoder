N = int(input())

name = [input() for _ in range(N)]

x, y = input().split()
x = int(x) - 1

if name[x] == y:
    print("Yes")
else:
    print("No")
