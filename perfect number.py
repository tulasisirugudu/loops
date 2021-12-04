# n=int(input("enter the number"))
# i=1 
# sum=0
# while(i<=n):
#     if (n%i==0):
#         sum=sum+i
#     i=i+1
#     if(sum==n):
#         print("it is perfect number")
#     else:
#         print("not a perfect number")

n = int(input("Enter a number: "))
i=2
sum=1
while(i<= n//2 ) :
    if (n % i == 0) :
        sum +=i
        i += 1
if sum == n :
    print(n,"is a perfect number")
else :
    print(n,"is not a perfect number")