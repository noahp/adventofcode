import sys, re

def memSizeStr(s):
    pass

if __name__ == '__main__':
    # 1. part one
    c = 0
    m = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            c += len(line.strip())
            m += len(eval(line.strip()))
    print 'Answer to part 1: ' + str(c-m)

    # # 2. part two
    c = 0
    n = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            c += len(line.strip())
            n += len('"'+re.escape(line.strip())+'"')
    print 'Answer to part 2: ' + str(n-c)
