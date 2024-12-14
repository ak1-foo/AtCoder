a, b, c, d, e = map(int, input().split())
scores = [a, b, c, d, e]

participants = []
for i in range(0b00001, 0b11111 + 1):
    name = []
    score = 0
    for j in range(5):
        if i >> j & 1:
            name += chr(ord("A") + j)
            score += scores[j]

    name = "".join(name)
    participants.append({"name": name, "score": score})

participants.sort(key=lambda x: x["name"])
participants.sort(key=lambda x: x["score"], reverse=True)

for participant in participants:
    print(participant["name"])
