import sys, re, pprint

if __name__ == '__main__':
    # 1. part one
    c = {}
    g = {}
    # collect the routes
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'(.*?) to (.*?) = ([0-9]+)', line)
            if m:
                c[(m.groups()[:2])] = m.groups()[2]
                if m.group(1) not in g:
                    g[m.group(1)] = []
                g[m.group(1)].append(m.group(2))

    # TODO brute force,search the graph for viable routes and find the shortest

    pprint.pprint(c)
    pprint.pprint(g)

    print 'Answer to part 1: '

    # # # 2. part two
    # c = 0
    # n = 0
    # with open(sys.argv[1], 'r') as f:
    #     for line in f.readlines():
    #         c += len(line.strip())
    #         n += len('"'+re.escape(line.strip())+'"')
    # print 'Answer to part 2: ' + str(n-c)
