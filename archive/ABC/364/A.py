N = int(input())
dishes = [input() for _ in range(N)]

for i in range(N-2):
    if dishes[i] == "sweet" and dishes[i+1] == "sweet":
        print('No')
        exit()

print('Yes')
