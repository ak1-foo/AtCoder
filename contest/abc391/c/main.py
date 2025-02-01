from sortedcontainers import SortedList

N, Q = map(int, input().split())

pigeon_location = [i for i in range(N)]
nest = [SortedList([i]) for i in range(N)]
num_multi_pigeon_nest = 0

for _ in range(Q):
    input_value = list(map(int, input().split()))

    if input_value[0] == 1:
        P, H = input_value[1] - 1, input_value[2] - 1

        # count
        prev_nest, target_nest = (len(nest[pigeon_location[P]]), len(nest[H]))
        if prev_nest == 2:
            num_multi_pigeon_nest -= 1
        if target_nest == 1:
            num_multi_pigeon_nest += 1

        # pick
        nest[pigeon_location[P]].remove(P)

        # drop
        nest[H].add(P)
        pigeon_location[P] = H

    elif input_value[0] == 2:
        print(num_multi_pigeon_nest)
