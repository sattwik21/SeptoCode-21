def pyramid():
      t=int(input())
      for i in range(t):
            n=int(input())
            arr=list(map(int,input().split()))
            m=max(arr)
            print(arr.index(m)+1)

    
pyramid()