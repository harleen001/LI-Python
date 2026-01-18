
def evenodd(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd


list1=[10,20,32,13,14,53,23,56,78]
even,odd=evenodd(list1)  # to take output from tuple into simple output
print(even)
print(odd)
