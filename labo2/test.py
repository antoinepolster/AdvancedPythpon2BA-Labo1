import re
import sys

# python labo2-q3.py http://www.this.is/big/shit/this/is/iepk
# python labo2-q3.py https://www.perdu.com/

pattern = r'(?P<protocol>[a-z]+)\:\//(?P<domain>[w]{3}\.[a-z]+\.[a-z]+)\/(?P<path>[a-z]+\/[a-z]+)*'
p = re.compile(pattern)
a = []
a = p.split

print(a)