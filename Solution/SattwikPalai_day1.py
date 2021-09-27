def score_generator():
    n=int(input()) 
    l=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        l.append(int(a+b*c/a-b))
    for i in l:
        print(i)

score_generator()