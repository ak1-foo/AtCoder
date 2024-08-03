num_people, budget_sum = map(int, input().split())
travel_costs = list(map(int, input().split()))

travel_costs.sort()

def calc_sum_pay(travel_costs, budget_per_person):
    sum_pay = 0
    for cost in travel_costs:
        sum_pay += min(cost, budget_per_person)

    return sum_pay

if (sum(travel_costs) <= budget_sum):
    print("infinite")
    exit()

budget_per_person = 10**9

left = 0
right = 10**9
while True:
    mid = (left + right)//2
    sum_pay = calc_sum_pay(travel_costs, mid)
    if (sum_pay <= budget_sum):
        left = mid
    else:
        right = mid

    if left == right:
        print(left)
        exit()

    if left + 1 == right:
        left_sum = calc_sum_pay(travel_costs, left)
        right_sum = calc_sum_pay(travel_costs, right)
        if right_sum <= budget_sum:
            ans = right
        else:
            ans = left
        print(ans)
        exit()
