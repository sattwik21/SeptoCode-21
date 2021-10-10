def prime():
    t=int(input())
    for i in range(t):
        p=int(input())
        if ( p % 2 == 1): 
            print("3 ",end="")
            p -= 3
        
        while ( p>0): 
            print("2 ",end="")
            p -= 2
        
        print()

prime()