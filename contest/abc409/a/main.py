N = int(input())
T = list(input())
A = list(input())

for i in range(N):
    if T[i] == "o" and A[i] == "o":
        print("Yes")
        exit()

print("No")
