query = input()

num = 0
for q in query:
    if q == '+':
        num += 1
    elif q == '-':
        num -= 1

print(num)