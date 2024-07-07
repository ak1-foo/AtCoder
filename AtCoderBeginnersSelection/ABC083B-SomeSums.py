n, a, b = map(int, input().split())

sum_ans = 0
for num in range(1, n+1):
    num_decimal_list = list(map(lambda x: int(x) ,list(str(num))))
    sum_tmp = 0
    for d in num_decimal_list:
        sum_tmp += d
    if (a <= sum_tmp and sum_tmp <= b):
        sum_ans += num

print(sum_ans)
