def line():
    t = int(input())
    while t>0:
        s = input()
        flag = 0
        x = s[0]

        for i in s:
            if i==x:
                flag = flag + 1
            else:
                x = i

        print(flag-1)

        t -= 1

line()