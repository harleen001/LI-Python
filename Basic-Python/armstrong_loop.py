num=int(input("Enter the number"))
sum=0
temp=num
while(num>0):
  rem=num%10
  num=num//10
  sum+=rem**3

if(temp==sum):
  print("ArmStrong")
else:
  print("Not Armstrong")