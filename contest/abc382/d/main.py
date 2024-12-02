N, M = map(int, input().split())


def generate_sequences(A, N, M):
    def backtrack(current_sequence):
        # 最後の要素が M を超えたら終了
        if current_sequence[-1] > M:
            return

        # 長さが N に達したら結果に追加
        if len(current_sequence) == N:
            result.append(current_sequence[:])
            return

        # 次の要素を生成して探索
        start = current_sequence[-1] + 10
        # ゆとりを持たせつつ、次の要素を生成
        for next_value in range(start, M + 1 - (N - len(current_sequence) - 1) * 10):
            current_sequence.append(next_value)
            backtrack(current_sequence)
            current_sequence.pop()  # 戻る

    result = []
    backtrack([A])  # 初期値 A でスタート
    return result


ans = []
init = 1
while True:
    sequences = generate_sequences(init, N, M)
    if not sequences:
        break
    ans.extend(sequences)
    init += 1

print(len(ans))
for a in ans:
    print(*a)
