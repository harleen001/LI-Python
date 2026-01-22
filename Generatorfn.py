def mygenerator():
    print("First Item")
    yield 10

    print("Second Item")
    yield 20

    print("Third Item")
    yield 30

gen=mygenerator()
print(next(gen))

print(next(gen))

print(next(gen))