n=int(input())
for i in range(n):
    if i==0 or i==(n-1):
        print()
        print("*"*(n+3),end='')
    else:
        print()
        for j in range(1):
            print("*"," "*(n+1),"*",sep='',end='')
    
