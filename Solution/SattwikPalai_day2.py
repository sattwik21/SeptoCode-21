def days_counter():
    n=int(input()) 
    l=[]
    for i in range(n):
        a,b=map(int,input().split())
        s=0
        if(a%400==0 or a%4==0):
            s+=366
        else:
             s+=365
        if(b%400==0 or b%4==0):
            s+=366
        else:
            s+=365;
        l.append(s)
    for i in l:
        print(i)

days_counter()