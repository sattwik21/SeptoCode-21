def matrix():
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=[]
        row_s=0
        col_s=0
        for i in range(n):
            col=list(map(int,input().split()))
            arr.append(col)
        for i in range(n):
            for j in range(n):
                if (i==0 and j<n) or (i==n-1 and j<n) :
                    row_s+=arr[i][j]
                if (j==0 and i<n) or (j==n-1 and i<n):
                    col_s+=arr[i][j]
        print(abs(row_s-col_s))

            


matrix()