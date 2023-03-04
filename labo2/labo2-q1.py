import re 

def startexo(S):
    print('\n' + "#"*10 + S + "#"*10)
    return
#1.a
startexo('1.a')
pattern = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}$'
p = re.compile(pattern)
print(p.match('+32 485 33 32 46'))

#1.b
startexo('1.b')
pattern2 = r'[-+]?[1-9]\d*'
p2 = re.compile(pattern2)
print(p2.match('345654') is not None)
print(p2.match('345 654') is not None)
print(p2.match('+345654') is not None)
print(p2.match('-235 54') is not None)
print(p2.match('0') is not None)

#1.c
startexo('1.c')
pattern3 = r'[1-9]?([A-Z]{3}\d{3}|\d{3}[A-Z]{3})'
p3 = re.compile(pattern3)
print(p3.match('345AZE') is not None)
print(p3.match('AZE123') is not None)
print(p3.match('3AZE345') is not None)
print(p3.match('AAZE345') is not None)

#1.d
startexo('1.d')
pattern4 = r'[A-Z]:\\'
p4 = re.compile(pattern4)
print(p4.match('C:/') is not None)


