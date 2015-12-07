import sys, re

VOWELS = 'aeiou'
BADSTRINGS = ['ab', 'cd', 'pq', 'xy']

def isnice(astring):
    # 1. count vowels
    v = 0
    for c in VOWELS:
        v += astring.count(c)
    if v < 3:
        return False

    # 2. find doubled characters
    m = re.search(r'([\s\S])\1', astring)
    if not m:
        return False

    # 3. check presence of bad strings
    for s in BADSTRINGS:
        if s in astring:
            return False

    return True

if __name__ == '__main__':
    nice = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            if isnice(line):
                nice += 1
    print nice
