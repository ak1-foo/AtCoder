# TLE
import itertools

num_shop, num_taste = map(int, input().split())
popcorn_info = [input() for _ in range(num_shop)]

popcorn_info_bit = []
for menu in popcorn_info:
    popcorn_info_bit += [menu.replace("x", "0").replace("o", "1")]


min_shop = float('inf')
num_taste_set = set(range(num_taste))

for pattern in list(itertools.permutations(popcorn_info_bit)):
    get_taste_bit = 0
    for index, shop_menu in enumerate(pattern):
        get_taste_bit = get_taste_bit | int(shop_menu, 2)
        if get_taste_bit == int("1" * num_taste, 2):
            min_shop = min(min_shop, index+1)
            continue

print(min_shop)
