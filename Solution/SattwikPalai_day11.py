import math
def marbles():
    t=int(input())
    for i in range(t):
        a=int(input())
        print(int(math.log2(a)))

marbles()