import sys, re, pprint, itertools

def traverse(allList, graph, thisList):
    for x in allList:
        if x not in thisList:
            thisList.append(x)
            traverse(graph[x], graph, thisList)
    #print thisList

if __name__ == '__main__':
    # 1. part one
    c = {}
    g = {}
    # collect the routes
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'(.*?) to (.*?) = ([0-9]+)', line)
            if m:
                if m.group(1) not in g:
                    g[m.group(1)] = []
                if m.group(2) not in g:
                    g[m.group(2)] = []
                g[m.group(1)].append(m.group(2))
                g[m.group(2)].append(m.group(1))

                k = ''.join(sorted([m.group(1), m.group(2)]))
                c[k] = int(m.group(3))


    # use permutations, because there are routes between all elements
    pprint.pprint(c)
    alist = []
    for p in itertools.permutations(g.keys()):
        a = 0
        for i in xrange(len(p)-1):
            a += c[''.join(sorted([p[i-1],p[i]]))]
        alist.append(a)

    print 'Answer to part 1: ' + str(min(alist))
    print 'Answer to part 2: ' + str(max(alist))
