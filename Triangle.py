n=int(input())
x=1
for i in range(n):
    for j in range(n-1-i):
        print("  ",end='')
    for j in range(1):
        print("* "*(2*x-1),end='')
    print()
    x+=1
print("##########################################################")
x=1
for i in range(n):
    print("  "*(n-i),"* "*(2*x-1))
    x=x+1