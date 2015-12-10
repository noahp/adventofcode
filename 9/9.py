import sys, re, pprint

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


    # TODO brute force,search the graph for viable routes and find the shortest
    pprint.pprint(c)
    alist = []
    for k in g.keys():
        l = [k] + g[k]
        a = 0
        for i in xrange(len(l)-1):
            a += c[''.join(sorted([l[i-1],l[i]]))]
        alist.append(a)

    print 'Answer to part 1: ' + str(min(alist))

    # # # 2. part two
    # c = 0
    # n = 0
    # with open(sys.argv[1], 'r') as f:
    #     for line in f.readlines():
    #         c += len(line.strip())
    #         n += len('"'+re.escape(line.strip())+'"')
    # print 'Answer to part 2: ' + str(n-c)
