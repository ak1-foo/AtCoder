# WA

from collections import deque

Rt, Ct, Ra, Ca = map(int, input().split())
T_loc = {"R": Rt, "C": Ct}
A_loc = {"R": Ra, "C": Ca}

N, M, L = map(int, input().split())

T_mov = deque()
for _ in range(M):
    dir, dist = input().split()
    dist = int(dist)
    T_mov.append({"dist": dist, "dir": dir})

A_mov = deque()
for _ in range(L):
    dir, dist = input().split()
    dist = int(dist)
    A_mov.append({"dist": dist, "dir": dir})

comb_mov = deque()
tm = {}
am = {}

while T_mov or A_mov:
    if not any(tm) or tm["dist"] == 0:
        tm = T_mov.popleft()
    if not any(am) or am["dist"] == 0:
        am = A_mov.popleft()

    next_dist = min(tm["dist"], am["dist"])
    comb_mov.append({"dist": next_dist, "dir": {"T": tm["dir"], "A": am["dir"]}})
    tm["dist"] = tm["dist"] - next_dist
    am["dist"] = am["dist"] - next_dist


count = 0
while comb_mov:
    T_loc_prev = T_loc
    A_loc_prev = A_loc
    ta_mov = comb_mov.popleft()
    dist = ta_mov["dist"]

    # get next location
    T_dir = ta_mov["dir"]["T"]
    if T_dir == "U":
        T_loc["R"] -= dist
    elif T_dir == "D":
        T_loc["R"] += dist
    elif T_dir == "L":
        T_loc["C"] -= dist
    elif T_dir == "R":
        T_loc["C"] += dist

    A_dir = ta_mov["dir"]["A"]
    if A_dir == "U":
        A_loc["R"] -= dist
    elif A_dir == "D":
        A_loc["R"] += dist
    elif A_dir == "L":
        A_loc["C"] -= dist
    elif A_dir == "R":
        A_loc["C"] += dist

    # count
    # go same way
    if T_dir == A_dir and T_loc_prev == A_loc_prev:
        count += dist

    # head-on
    # same row
    row_prev_dist = abs(A_loc_prev["C"] - T_loc_prev["C"])
    if A_loc_prev["C"] - T_loc_prev["C"] % 2 == 0 and row_prev_dist // 2 <= dist:
        if (T_dir == "L" and A_dir == "R") or (T_dir == "R" and A_dir == "L"):
            count += 1
    # same col
    col_prev_dist = abs(A_loc_prev["R"] - T_loc_prev["R"])
    if A_loc_prev["R"] - T_loc_prev["R"] % 2 == 0 and col_prev_dist // 2 <= dist:
        if (T_dir == "U" and A_dir == "D") or (T_dir == "D" and A_dir == "U"):
            count += 1

    # cross
    # if row_prev_dist == col_prev_dist:
    #    if T_dir == "U" and A_dir == "L":
    #        if (T_loc["R"] <= A_loc["R"] <= T_loc_prev["R"]) and (
    #            A_loc["C"] <= T_loc["C"] <= A_loc_prev["C"]
    #        ):
    #            count += 1
    #
    #    if T_dir == "U" and A_dir == "R":
    #        if (T_loc["R"] <= A_loc["R"] <= T_loc_prev["R"]) and (
    #            A_loc_prev["C"] <= T_loc["C"] <= A_loc["C"]
    #        ):
    #            count += 1
    #
    #    if T_dir == "" and A_dir == "R":
    #        if (T_loc["R"] <= A_loc["R"] <= T_loc_prev["R"]) and (
    #            A_loc_prev["C"] <= T_loc["C"] <= A_loc["C"]
    #        ):
    #            count += 1
    #

    if T_loc_prev != A_loc_prev:

        # Tが上(U)、Aが左(L)に移動した場合
        if T_dir == "U" and A_dir == "L":
            if (T_loc["R"] <= A_loc["R"] <= T_loc_prev["R"]) and (
                A_loc["C"] <= T_loc["C"] <= A_loc_prev["C"]
            ):
                count += 1

        # Tが上(U)、Aが右(R)に移動した場合
        elif T_dir == "U" and A_dir == "R":
            if (T_loc["R"] <= A_loc["R"] <= T_loc_prev["R"]) and (
                A_loc_prev["C"] <= T_loc["C"] <= A_loc["C"]
            ):
                count += 1

        # Tが下(D)、Aが左(L)に移動した場合
        elif T_dir == "D" and A_dir == "L":
            if (T_loc_prev["R"] <= A_loc["R"] <= T_loc["R"]) and (
                A_loc["C"] <= T_loc["C"] <= A_loc_prev["C"]
            ):
                count += 1

        # Tが下(D)、Aが右(R)に移動した場合
        elif T_dir == "D" and A_dir == "R":
            if (T_loc_prev["R"] <= A_loc["R"] <= T_loc["R"]) and (
                A_loc_prev["C"] <= T_loc["C"] <= A_loc["C"]
            ):
                count += 1

        # Tが左(L)、Aが上(U)に移動した場合
        elif T_dir == "L" and A_dir == "U":
            if (T_loc["C"] <= A_loc["C"] <= T_loc_prev["C"]) and (
                A_loc["R"] <= T_loc["R"] <= A_loc_prev["R"]
            ):
                count += 1

        # Tが左(L)、Aが下(D)に移動した場合
        elif T_dir == "L" and A_dir == "D":
            if (T_loc["C"] <= A_loc["C"] <= T_loc_prev["C"]) and (
                A_loc_prev["R"] <= T_loc["R"] <= A_loc["R"]
            ):
                count += 1

        # Tが右(R)、Aが上(U)に移動した場合
        elif T_dir == "R" and A_dir == "U":
            if (T_loc_prev["C"] <= A_loc["C"] <= T_loc["C"]) and (
                A_loc["R"] <= T_loc["R"] <= A_loc_prev["R"]
            ):
                count += 1

        # Tが右(R)、Aが下(D)に移動した場合
        elif T_dir == "R" and A_dir == "D":
            if (T_loc_prev["C"] <= A_loc["C"] <= T_loc["C"]) and (
                A_loc_prev["R"] <= T_loc["R"] <= A_loc["R"]
            ):
                count += 1

print(count)
