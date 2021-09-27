def danger():
    t=int(input())
    for i in range(t):
        l=int(input())
        s=input()
        n=1
        f=0
        for i in range(1,l):
            if s[i]==s[i-1]:
                n+=1
            else:
                n=1
            if n==6:
                f+=1
                break
        if f>0:
            print("YES")
        else:
            print('NO')


        
            
danger()