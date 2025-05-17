hA, mB, hC, mD = map(int, input().split())

if hA > hC:
    print("Yes")
    exit()
elif hA == hC and mB > mD:
    print("Yes")
    exit()
else:
    print("No")
    exit()
