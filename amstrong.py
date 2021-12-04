num=int(input("enter the num"))
len=len(str(num))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**len
    temp=temp//10
if num==sum:
    print("it is an amstrong number")
else:
    print("it is not a amstrong number")

