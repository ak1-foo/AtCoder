n = int(input())
an_list = list(map(int, input().split()))

end_flag = False
cnt = 0

while True:
    for an in an_list:
        if (an % 2 != 0):
            end_flag = True
            break
    if(end_flag == True):
        break
    cnt = cnt + 1
    an_list = list(map(lambda an: an/2, an_list))

print(cnt)
