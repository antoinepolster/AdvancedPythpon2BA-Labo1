import sys
import re 

# python labo2-q2.py monfichier.txt

def main(filename):
    with open(filename) as file:
        lines = file.readlines()
    pattern = re.compile(r'[-+]?(?:[1-9]\d+|\d)')
    for i, line in enumerate(lines):
        matches = pattern.findall(line)
        print('Line {}: {}'.format(i+1, ', '.join(matches)))


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else :
        print('Usage: python labo2-q2.py <fileToProcess>')