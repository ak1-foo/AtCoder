N, K = map(int, input().split())
S = list(input())

X = S[:]

# "o"のとなりは必ず"."
for i in range(N - 1):
    if S[i] == "?" and S[i + 1] == "o":
        X[i] = "."
    elif S[i] == "o" and S[i + 1] == "?":
        X[i + 1] = "."

# 連続する"?"がいくつずつあるか
count = []
questions = []
for i in range(N):
    if X[i] == "?":
        count.append(i)
    elif len(count) > 0:
        questions.append(count)
        count = []
if len(count) > 0:
    questions.append(count)


# 最大でいくつ"o"が入るか
max_o_capacity = 0
for question in questions:
    max_o_capacity += (len(question) + 1) // 2

# すでに入っている"o"の数
num_o = 0
for i in range(N):
    if X[i] == "o":
        num_o += 1


# 埋める
if K - num_o == max_o_capacity:
    for question in questions:
        if len(question) % 2 == 1:
            for i in range(len(question)):
                if i % 2 == 0:
                    X[question[i]] = "o"
                else:
                    X[question[i]] = "."

elif K == num_o:
    for i in range(N):
        if X[i] == "?":
            X[i] = "."

print("".join(X))
