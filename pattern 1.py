n=int(input("enter number of rows:"))

for i in range(n):
    for j in range(i):
        print("*",end='')
    print()

#  *
#  **
#  ***
#  ****