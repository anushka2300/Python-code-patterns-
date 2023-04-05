# @@@@@
# @@@@
# @@@
# @@
# @



n=int(input("enter number of rows:"))

for i in range(n):
    for j in range(n,0,-1):
        print("@",end='')
    n=n-1
    print()
        
