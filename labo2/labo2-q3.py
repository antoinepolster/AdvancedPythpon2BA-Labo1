import re
import sys

# python labo2-q3.py http://www.this.is/big/shit/this/is/iepk
# python labo2-q3.py https://www.perdu.com/

def main(url):
    pattern = r'(?P<protocol>[a-z]+)\:\//(?P<domain>[w]{3}\.[a-z]+\.[a-z]+)\/(?P<path>[a-z]+\/[a-z]+)*'
    p = re.compile(pattern)
    m = p.match(url)
    print(len(m.group('protocol')))
    print(len(m.group('domain')))
    if m.group('path') == None:
        print('there is no path')
    else : 
        print(len(m.group('path')))

def thereispath (m):
    if m is not None:
        print('Protocol : ' + m.group('protocol'))
        print('Domain : ' + m.group('domain'))
        print('Path : ' + m.group('path'))

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else :
        print('Usage : python labo2-q3.py <url>')

