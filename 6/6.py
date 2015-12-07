import sys, re
import array

def turnon(x):
    return 1

def turnoff(x):
    return 0

def toggle(x):
    if x == 1:
        return 0
    else:
        return 1

cmdmap = {
    'turn on':turnon,
    'turn off':turnoff,
    'toggle':toggle
}

if __name__ == '__main__':
    r = re.compile(r'((?:turn on)|(?:turn off)|(?:toggle)) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')

    a = [[0] *1000] * 1000

    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = r.search(line)
            if m:
                cmd, xstart, ystart, xend, yend = m.groups()
                xstart, ystart, xend, yend = map(int, (xstart, ystart, xend, yend))

                for x in xrange(xstart, xend + 1):
                    a[x] = a[x][:ystart] + map(cmdmap[cmd], a[x][ystart:yend+1]) + a[x][yend + 1:]

    print sum([sum(c) for c in a])
