def Slope():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        j=True
        for i in range(1,len(l)):
            if l[i-1]==l[i]:
                j=False
                break
        if j==False:
            print("Gentle")
        else:
            print("Steep")


Slope()