y = [7,4]
x = [8,9]
def add(a,b):
    return (a+b)
def s(a,b):
    return (a * a , b * b)
product = map(add,x,y)
result = map(s,x,y)
print("Addition of lists = ", list(product))
print(list(result))
