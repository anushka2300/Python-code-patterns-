n=int(input("rows:"))
m=int(input("middle line"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    if(i==0):
        print("*")
    else:
        if(i==m-1):
            print("*"+"*"*(2*i-1)+"*")
        else:
            print("*"+" "*(2*i-1)+"*")
        
    