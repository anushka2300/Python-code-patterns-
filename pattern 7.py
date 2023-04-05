a=int(input())
for i in range(a,-1,-1):
    print("*"*(i),"*"*(i),sep=" "*(2*(a-i)))
    