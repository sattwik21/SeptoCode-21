def lowercase_alphabets():
    t=int(input())
    for i in range(t):
        s=input()
        S=set()
        for i in s:
            S.add(i)
        if len(S)==26:
            print("Pass")
        else:
            print("Fail")


lowercase_alphabets()