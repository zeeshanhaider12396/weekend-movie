for i in range(int(input())):
    ls = []
    n = int(input())
    ls_l = list(map(int, input().split()))
    ls_r = list(map(int, input().split()))
    maxlr = 0
    maxr = 0
    ans = 0
    for i in range(n):
        if ls_l[i]*ls_r[i] > maxlr:
            maxlr = ls_l[i]*ls_r[i]
            maxr = ls_r[i]
            ans = i
        if ls_l[i]*ls_r[i] == maxlr:
            if ls_r[i] > maxr:
                maxr = ls_r[i]
                ans = i
    print(ans+1)