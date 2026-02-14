num=int(input("Enter your number ="))
print("The Entered number is =",num)
rev1=num%10
num=num//10
rev2=num%10
num=num//10
rev3=num%10
num=num//10
rev4=num%10
num=num//10
print("The Reversed number is =",rev1*1000+rev2*100+rev3*10+rev4*1)