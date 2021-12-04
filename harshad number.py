n=int(input("enter the number"))
num1=n
s=0
rem=0
while(n>0):
    rem=n%10
    s=s+rem
    n=n//10
if (num1%s==0):
    print("harshad number")
else:
    print("not harshad number")