a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

# 16点において、+0.1 内側に寄せたものが両方に当たるか
# if (a < x < c) and (b < y < d) and (e < z < f): で判定
if    (((a < g+0.1 < d) and (b < h+0.1 < e) and (c < i+0.1 < f))
    or ((a < g+0.1 < d) and (b < h+0.1 < e) and (c < l-0.1 < f))
    or ((a < g+0.1 < d) and (b < k-0.1 < e) and (c < i+0.1 < f))
    or ((a < g+0.1 < d) and (b < k-0.1 < e) and (c < l-0.1 < f))
    or ((a < j-0.1 < d) and (b < h+0.1 < e) and (c < i+0.1 < f))
    or ((a < j-0.1 < d) and (b < h+0.1 < e) and (c < l-0.1 < f))
    or ((a < j-0.1 < d) and (b < k-0.1 < e) and (c < i+0.1 < f))
    or ((a < j-0.1 < d) and (b < k-0.1 < e) and (c < l-0.1 < f))

# C(a, b, c, d, e, f)がC(g, h, i, j, k, l)の中にあるかどうかを判定する
# if (g < x < j) and (h < y < k) and (i < z < l): で判定
   or ((g < a+0.1 < j) and (h < b+0.1 < k) and (i < c+0.1 < l))
   or ((g < a+0.1 < j) and (h < b+0.1 < k) and (i < f-0.1 < l))
   or ((g < a+0.1 < j) and (h < e-0.1 < k) and (i < c+0.1 < l))
   or ((g < a+0.1 < j) and (h < e-0.1 < k) and (i < f-0.1 < l))
   or ((g < d-0.1 < j) and (h < b+0.1 < k) and (i < c+0.1 < l))
   or ((g < d-0.1 < j) and (h < b+0.1 < k) and (i < f-0.1 < l))
   or ((g < d-0.1 < j) and (h < e-0.1 < k) and (i < c+0.1 < l))
   or ((g < d-0.1 < j) and (h < e-0.1 < k) and (i < f-0.1 < l))):
    print('Yes')

else:
    print('No')
