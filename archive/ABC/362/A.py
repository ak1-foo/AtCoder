R_price, G_price, B_price = map(int, input().split())
dislike_color = input()

if (dislike_color == 'Red'):
    if (G_price < B_price):
        min_price = G_price
    else:
        min_price = B_price

elif (dislike_color == 'Green'):
    if (R_price < B_price):
        min_price = R_price
    else:
        min_price = B_price

elif (dislike_color == 'Blue'):
    if (R_price < G_price):
        min_price = R_price
    else:
        min_price = G_price

print(min_price)
