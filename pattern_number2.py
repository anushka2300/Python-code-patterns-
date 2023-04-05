#1
#2 3
#4 5 6
#7 8 9 1
#2 3 4 5 6

n=int(input())
x=1
for i in range(n):
    
    for j in range(i+1):
        print(x,end=' ')
        x+=1
    print()
    