def serial_number():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        b=True
        a=0
        for i in range(1,n+1):
            if i not in l:
                b=False
                a=i
                break
        if b:
            print(0)
        else:
            print(a)




    
serial_number()