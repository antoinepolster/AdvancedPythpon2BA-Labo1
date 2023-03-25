def exo(x): 
    print('\n' + '########## ' + str(x) + ' ##########')
    return 

def call(x, *args, **kwargs):
    return x(*args, **kwargs)

#1 
exo(1)
def hello():
    print('Hello') 

call(hello)

#2
exo(2)
def add(a, b):
    return (a+b)

print(call(add, 2, 9))

#3
exo(3)
def sub(a, b):
    return (a-b)

def compute(a, b, op=add):
    return op(a, b)

print(call(compute, 2, 9))
print(call(compute, 2, 9, op=sub))