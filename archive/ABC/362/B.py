xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

# 内積が0かどうかを考える
AB_vec = [xB-xA, yB-yA]
BC_vec = [xC-xB, yC-yB]
CA_vec = [xA-xC, yA-yC]


def inner_product(vec_a, vec_b):
    ans = vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]
    return ans

if inner_product(AB_vec, BC_vec) == 0:
    print('Yes')
elif inner_product(BC_vec, CA_vec) == 0:
    print('Yes')
elif inner_product(CA_vec, AB_vec) == 0:
    print('Yes')

else:
    print('No')
