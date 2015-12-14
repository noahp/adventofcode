import sys, re

VOWELS = 'aeiou'
BADSTRINGS = ['ab', 'cd', 'pq', 'xy']

def isnice1(astring):
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

def isnice2(astring):
    m = re.search(r'([a-z]{2}).*(\1)', astring)
    if not m:
        return False

    m = re.search(r'([a-z]{1})[\s\S](\1)', astring)
    if not m:
        return False

    return True

if __name__ == '__main__':
    nice1 = 0
    nice2 = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            if isnice1(line):
                nice1 += 1
            if isnice2(line):
                nice2 += 1
    print 'Answer to question 1: ' + str(nice1)
    print 'Answer to question 2: ' + str(nice2)
