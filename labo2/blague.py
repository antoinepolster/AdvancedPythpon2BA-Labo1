import re

print('quel est ton nom? ')
answer = input()
pattern = r'[a-z]'
p1 = re.compile(pattern)

def cons(answer):
    print('ok')
    if answer == 'pierre' or 'Pierre':
        print('ok chacal tu es con')
    elif answer == 'elliott' or 'Elliott':
        print('ok chacal tu es con')
    else: 
        print('toi tu es intelligent')

print(p1.match(answer) is not None)

if (p1.match(answer) is not None) == True:
    cons(answer)
else: 
    print('un nom pas un chiffre tdc') 
