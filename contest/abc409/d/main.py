T = int(input())

for _ in range(T):
    N = int(input())
    S = list(input())
    S_encoded = [ord(c) - ord("a") for c in S]

    head_idx = -1
    for i in range(N - 1):
        if S_encoded[i] > S_encoded[i + 1]:
            head_idx = i
            break

    if head_idx == -1:
        print("".join(S))
        continue

    tail_idx = N - 1
    for i in range(head_idx + 1, N):
        if S_encoded[i] > S_encoded[head_idx]:
            tail_idx = i - 1
            break

    S = "".join(S)
    ans = (
        S[:head_idx] + S[head_idx + 1 : tail_idx + 1] + S[head_idx] + S[tail_idx + 1 :]
    )

    print("".join(ans))
