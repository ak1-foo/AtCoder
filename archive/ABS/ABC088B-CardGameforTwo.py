n = int(input())
an_list = list(map(int, input().split()))

alice_sum = 0
bob_sum = 0

an_list.sort(reverse=True)

for i,an in enumerate(an_list):
    if (i % 2 == 0): # アリスが取る
        alice_sum += an
    else: # ボブが取る
        bob_sum += an

print(alice_sum - bob_sum)
