def line():
    t = int(input())
    while t>0:
        s = input()
        fla = 0
        x = s[0]

        for i in s:
            if i==x:
                fla = fla + 1
            else:
                x = i

        print(fla-1)

        t -= 1

line()
