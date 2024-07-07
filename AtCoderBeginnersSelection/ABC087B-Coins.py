c500_num = int(input())
c100_num = int(input())
c50_num = int(input())
sum_pay = int(input())

pattern = 0


sum_tmp = 0
for c500 in range(c500_num+1):
    for c100 in range(c100_num+1):
        for c50 in range(c50_num+1):
            sum_tmp = 500 * c500 + 100 * c100 + 50 * c50
            if (sum_tmp == sum_pay):
                pattern += 1

print(pattern)
