N = int(input())


is_first_lefthand = False
is_first_righthand = False

cost = 0
for _ in range(N):
    A, S = input().split()
    A = int(A)
    if S == "L":
        if not is_first_lefthand:
            is_first_lefthand = True
        else:
            cost += abs(A - left_hand)
        left_hand = A
    elif S == "R":
        if not is_first_righthand:
            is_first_righthand = True
        else:
            cost += abs(A - right_hand)
        right_hand = A

print(cost)
