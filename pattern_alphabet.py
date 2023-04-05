#A
#B C
#D E F
#G H I J
#K L M N O

n=int(input())
x=65
for i in range(n):
    
    for j in range(i+1):
        print(chr(x),end=' ')
        x+=1
    print()
    