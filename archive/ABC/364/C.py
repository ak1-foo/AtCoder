num_dishes, max_sweet, max_salt = map(int, input().split())

dises_sweet = list(map(int, input().split()))
dises_salt = list(map(int, input().split()))

dises_sweet.sort(reverse=True)
dises_salt.sort(reverse=True)


num_eatable_sweet_dishes = 0
eated_sweet = 0
for dish in dises_sweet:
    if eated_sweet > max_sweet:
        break
    else:
        eated_sweet += dish
        num_eatable_sweet_dishes += 1

num_eatable_salt_dishes = 0
eated_salt = 0
for dish in dises_salt:
    if eated_salt > max_salt:
        break
    else:
        eated_salt += dish
        num_eatable_salt_dishes += 1

num_eatable_dishes = min(num_eatable_sweet_dishes, num_eatable_salt_dishes)
print(num_eatable_dishes)
