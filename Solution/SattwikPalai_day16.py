def Mirsha():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        even=[]
        odd=[]
        for i in l:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        if len(even)==1:
            print(l.index(even[0])+1)
        else:
            print(l.index(odd[0])+1)
        



    
Mirsha()