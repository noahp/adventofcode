import re, sys

def distTraveled(reindeer, g):
    d = 0
    # add periods of active + idle times active rate
    d += (g / (reindeer[2] + reindeer[3])) * reindeer[1] * reindeer[2]
    # now remainder
    d += min((g % (reindeer[2] + reindeer[3])), reindeer[2]) * reindeer[1]

    return d

if __name__ == '__main__':
    a = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'(\w+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds\.', line)
            if m:
                x = [m.group(1),] + [int(c) for c in m.groups()[1:]]
                a.append(x)

    # execute the race
    m = {}
    g = 2503    # race duration
    for r in a:
        m[r[0]] = distTraveled(r, g)

    print 'Answer to part 1: ' + str(max(m.values()))

    # part 2, gross iterative method
    m = dict([(r[0], 0) for r in a])
    g = 2503    # race duration
    for i in xrange(1, g):
        # compute distance traveled at each time segment by each reindeer
        distanceEach = dict([(r[0], 0) for r in a])
        for r in a:
            distanceEach[r[0]] = distTraveled(r, i)
        #print distanceEach
        # add up points
        for r in a:
            if distanceEach[r[0]] == max(distanceEach.values()):
                m[r[0]] += 1

    print 'Answer to part 1: ' + str(max(m.values()))
