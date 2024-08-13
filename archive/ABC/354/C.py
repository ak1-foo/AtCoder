num_card = int(input())

cards = []
for i in range(num_card):
    power, cost = map(int, input().split())
    cards.append({"index": i+1, "power": power, "cost": cost})

cards.sort(key=lambda card: card["power"], reverse=True)

discard_card_index = []

prev_card = cards[0]
for i in range(len(cards)-1):
    if prev_card["cost"] < cards[i+1]["cost"]:
        discard_card_index.append(cards[i+1]["index"])
    else:
        prev_card = cards[i+1]

ans = sorted(list(set([i for i in range(1, num_card+1)]) - set(discard_card_index)))
print(len(ans))
print(*ans)
