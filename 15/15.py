import re, sys, itertools

def score(amount, props):
    ''' Score of a particular amount of an ingredient '''
    return max(0, sum([amount * c for c in props]))

if __name__ == '__main__':
    a = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'(\w+): capacity (-*[0-9]+), durability (-*[0-9]+), flavor (-*[0-9]+), texture (-*[0-9]+), calories (-*[0-9]+)', line)
            if m:
                x = [m.group(1),] + [int(c) for c in m.groups()[1:]]
                a.append(x)

    # execute the race
    m = []
    for i in itertools.permutations([range(1,5)]*len(m)):
        print i

    #print 'Answer to part 1: ' + str(max(m))
