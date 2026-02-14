num_1=int(input("Enter a number ="))
check=num_1
rev=0
while(num_1>0):
    num_2=num_1%10
    rev=rev*10+num_2
    num_1=num_1//10
if(check==rev):
    print("The number is palindrome")
elif(check!=rev):
    print("The number is not a palindrome")