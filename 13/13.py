import itertools, re, sys

with open(sys.argv[1], 'r') as f:
    inputTxt = f.read()

datas = {}
people = []
for line in inputTxt.splitlines():
    #print line
    m = re.search(r'([A-Za-z]+) +.*?((?:gain)|(?:lose)) ([0-9]+).*?([A-Za-z]+)\.', line)
    if m:
        if m.groups()[0] not in people:
            people.append(m.groups()[0])
        z = int(m.group(3))
        if m.group(2) == 'lose':
            z = -z
        datas[m.group(1)+m.group(4)] = z
        #print z

vals = []
for g in itertools.permutations(people):
    a = 0
    a += datas[g[-1]+g[0]] + datas[g[0]+g[-1]]
    #print str(datas[g[-1]+g[0]]), str(datas[g[0]+g[-1]])
    for idx, p in enumerate(g[1:]):
        a += datas[p + g[idx]] + datas[g[idx]+p]
        #print str(datas[p + g[idx]]), str(datas[g[idx]+p])
    vals.append(a)

print 'Answer to part 1: ' + str(max(vals))

for p in people:
    datas['noahp'+p] = 0
    datas[p+'noahp'] = 0
people.append('noahp')

vals = []
for g in itertools.permutations(people):
    a = 0
    a += datas[g[-1]+g[0]] + datas[g[0]+g[-1]]
    #print str(datas[g[-1]+g[0]]), str(datas[g[0]+g[-1]])
    for idx, p in enumerate(g[1:]):
        a += datas[p + g[idx]] + datas[g[idx]+p]
        #print str(datas[p + g[idx]]), str(datas[g[idx]+p])
    vals.append(a)

print 'Answer to part 2: ' + str(max(vals))
