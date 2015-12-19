import re, sys, pprint, copy

if __name__ == '__main__':
    ops = []
    molecule = ''
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'([A-Za-z]+) => ([A-Za-z]+)', line)
            if m:
                ops.append(m.groups())
            else:
                m = re.match(r'([A-Za-z]+)', line)
                if m:
                    molecule = m.groups()[0]
    print ops
    print molecule

    # print 'Answer to part 1: ' + str(a)
