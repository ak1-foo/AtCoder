x, y = map(int, input().split())


def rev(x):
    return int("".join(reversed(list(str(x)))))


rev_fib_ans = [x, y]
for i in range(2, 10):
    rev_fib_ans.append(rev(rev_fib_ans[i - 2] + rev_fib_ans[i - 1]))

print(rev_fib_ans[-1])
