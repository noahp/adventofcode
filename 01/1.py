import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        data = f.read()

    # 1. net open parens
    print 'Answer to question 1: ' + str(data.count('(') - data.count(')'))

    # 2. location where net value is -1
    loc = 0
    for idx,c in enumerate(data):
        if c is '(':
            loc += 1
        elif c is ')':
            loc -= 1
        if loc == -1:
            print 'Answer to question 2: ' + str(idx + 1)
            break
