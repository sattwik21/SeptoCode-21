def sports():
    n=int(input())
    l=[]
    for i in range(n):
        a=int(input())
        if 5-(a%5)<3 and a>33:
            a+=(5-(a%5))
        l.append(a)
    for i in l:
        print(i)


sports()