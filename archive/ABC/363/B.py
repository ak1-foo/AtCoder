num_person, goal_hair_len, goal_num_person = map(int, input().split())
hair_len = list(map(int, input().split()))

hair_len.sort()

goal_days = 0
if (hair_len[-goal_num_person] < goal_hair_len):
    goal_days = goal_hair_len - hair_len[-goal_num_person]

print(goal_days)
