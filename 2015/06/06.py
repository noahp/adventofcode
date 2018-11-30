import sys, re
import array

def turnon_1(x):
    return 1

def turnoff_1(x):
    return 0

def toggle_1(x):
    if x == 1:
        return 0
    else:
        return 1

def turnon_2(x):
    return x + 1

def turnoff_2(x):
    if x > 1:
        return x - 1
    else:
        return 0

def toggle_2(x):
    return x + 2

cmdmap_1 = {
    'turn on':turnon_1,
    'turn off':turnoff_1,
    'toggle':toggle_1
}

cmdmap_2 = {
    'turn on':turnon_2,
    'turn off':turnoff_2,
    'toggle':toggle_2
}

def partone(f):
    r = re.compile(r'((?:turn on)|(?:turn off)|(?:toggle)) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')
    a = [[0] *1000] * 1000
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = r.search(line)
            if m:
                cmd, xstart, ystart, xend, yend = m.groups()
                xstart, ystart, xend, yend = map(int, (xstart, ystart, xend, yend))

                for x in xrange(xstart, xend + 1):
                    a[x] = a[x][:ystart] + map(cmdmap_1[cmd], a[x][ystart:yend+1]) + a[x][yend + 1:]
    return sum([sum(c) for c in a])

def parttwo(f):
    r = re.compile(r'((?:turn on)|(?:turn off)|(?:toggle)) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')
    a = [[0] *1000] * 1000
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = r.search(line)
            if m:
                cmd, xstart, ystart, xend, yend = m.groups()
                xstart, ystart, xend, yend = map(int, (xstart, ystart, xend, yend))

                for x in xrange(xstart, xend + 1):
                    a[x] = a[x][:ystart] + map(cmdmap_2[cmd], a[x][ystart:yend+1]) + a[x][yend + 1:]
    return sum([sum(c) for c in a])

if __name__ == '__main__':
    # 1. part one
    answer = partone(sys.argv[1])
    print 'Answer to part 1: ' + str(answer)

    # 2. part two
    answer = parttwo(sys.argv[1])
    print 'Answer to part 2: ' + str(answer)
