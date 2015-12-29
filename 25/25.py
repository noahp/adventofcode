import re, sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        r = f.read()
        m = re.search(r'To continue, please consult the code grid in the manual\.  Enter the code at row (2947), column (3029)\.', r)
        if m:
            row,column = map(int, m.groups())

    # print row,column

    # 1. from row,column find position in linear code
    pos = sum([c for c in xrange(row + column)]) - (row - 1)
    # pos = sum([c for c in xrange(5 + 4)]) - (5 - 1)

    init = 20151125
    mult = 252533
    divi = 33554393
    for i in xrange(pos-1):
        init = (init * mult) % divi

    print init
