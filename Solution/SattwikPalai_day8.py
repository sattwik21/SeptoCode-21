L=[]
def English():
    global L
    t=int(input())
    for i in range(t):
        s=input()
        l=0
        u=0
        for i in range(len(s)):
            if(s[i].isupper()):
                u+=1
            else:
                l+=1
        if l>=u:
            s=s.lower()
        else:
            s=s.upper()
        L.append(s)

def Print_list():
    global L
    for i in L:
        print(i)

English()
Print_list()