# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4 
# 5

n=int(input("enter the number"))
i=1
while(i<=n):
    j=n
    while (j>=i):
        print(i,end="")
        j=j-1
    print()
    i=i+1
