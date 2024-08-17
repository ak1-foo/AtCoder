# WA

from itertools import accumulate

rest_num, step_rule = map(int, input().split())
steps = list(map(int, input().split()))

step_sum = list(accumulate(steps))
step_sum_mod = [s % step_rule for s in step_sum]
print(f'{step_sum_mod=}')

ans_steps = [(x+y) % step_rule for i, x in enumerate(step_sum_mod) for j, y in enumerate(step_sum_mod) if i != j]

result = []
for i, x in enumerate(step_sum_mod):
    for j, y in enumerate(step_sum_mod):
        if i != j and abs(i - j) > 1:
            result.append((x + y) % step_rule)
        elif i == j:
            result.append(((x + y) // 2) % step_rule)

print(f'{result=}')

ans = ans_steps.count(0)
print(ans)