from time import sleep

def exo(x): 
    print('\n' + '########## ' + str(x) + ' ##########')
    return 

#1
exo(1)

def delay(f):
    def wrapper(*args, **kwargs):
        sleep(1)
        return f(*args, **kwargs)
    return wrapper 

#@delay
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1

print('KA-BOUM')

#2
exo(2)
@delay(5)
def printnum(i):
    print(i)

cnt = 3
while cnt > 0:
    printnum(cnt)
    cnt -= 1

print('KA-BOUM')

