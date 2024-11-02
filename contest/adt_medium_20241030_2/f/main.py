import math

N = int(input())

# O(sqrt(N))
def prime_factor(n):
    primes = {}
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            primes[i] = primes.get(i, 0) + 1

    if n != 1:
        primes[n] = primes.get(n, 0) + 1
    return primes

# O(sqrt(N))
def count_factor(n):
    factors = prime_factor(n)
    count = 1
    for v in factors.values():
        count *= v + 1
    return count

def is_n_power(n):
    return math.sqrt(n).is_integer()

ans = 0
for i in range(1, N):
    ab = i
    cd = N - i

    num_ab_patterns = count_factor(ab)
    num_cd_patterns = count_factor(cd)


    ans += num_ab_patterns * num_cd_patterns

print(ans)
