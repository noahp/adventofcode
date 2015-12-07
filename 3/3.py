import sys


if __name__ == '__main__':
    map = set([(0,0)])
    currpos = (0,0)
    with open(sys.argv[1], 'r') as f:
        for c in f.read():
            if c not in '^v><':
                continue

            if c == '^':
                currpos = (currpos[0], currpos[1] + 1)
            elif c == 'v':
                currpos = (currpos[0], currpos[1] - 1)
            elif c == '>':
                currpos = (currpos[0] + 1, currpos[1])
            elif c == '<':
                currpos = (currpos[0] - 1, currpos[1])
            map.add(currpos)

print len(map)
