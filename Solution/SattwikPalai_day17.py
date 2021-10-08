def square_digits(n):
    return sum( int(c)**2 for c in str(n) )

def lucky_draw():
    t=int(input())
    for i in range(t):
        n=int(input())
        attractors = [1, 4, 16, 37, 58, 89, 145, 42, 20]
        m = n
        while m not in attractors:
            m = square_digits(m)
        if m==1:
            print("lucky")
        else:
            print("unlucky")

        



    
lucky_draw()