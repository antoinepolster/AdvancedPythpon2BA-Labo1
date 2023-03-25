def call(f, *args, **kwargs):
    return f(*args, **kwargs)


def add(a,b):
    return a+b

def compute(a, b, op=add):
    return op(a,b)

def sub(a, b):
    return a-b

print(call(compute, 2, 9))
print(call(compute, 2, 9, op=sub))
