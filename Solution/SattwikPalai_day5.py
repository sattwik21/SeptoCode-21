def occurredOnce():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))[:n]
        L=[]
        for i in l:
            if l.count(i)==1:
                L.append(i)
        if len(L)==0:
            print(0)
        else:
            for i in L:
                print(i,end=' ')
        print()
            

occurredOnce()