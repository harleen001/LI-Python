def div(a,b):
    print(a/b)

def smart_div(fun):
    def inner_fun(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner_fun

div1=smart_div(div)
div1(2,4)