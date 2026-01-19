#def is_even(n):
#    return n%2==0

def update(n):
    return n+2

list1=[10,32,4223,324,323,23,2,123,4,34332,324]

evenlist=list(filter(lambda x:x%2==0,list1))    #keeps only the elements that satisfy a condition.
print(evenlist)

doubles=list(map(update,evenlist)) #applies a function to every element in a sequence.
print(doubles)
