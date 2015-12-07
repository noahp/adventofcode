import sys


if __name__ == '__main__':
    houses = set([(0,0)])
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
            houses.add(currpos)

    print 'Answer to question 1: ' + str(len(houses))

    houses = set([(0,0)])
    currpossanta = (0,0)
    currposrobosanta = (0,0)
    with open(sys.argv[1], 'r') as f:
        for idx, c in enumerate(f.read()):
            if c not in '^v><':
                continue

            if idx & 1:
                currpos = currposrobosanta
            else:
                currpos = currpossanta

            if c == '^':
                currpos = (currpos[0], currpos[1] + 1)
            elif c == 'v':
                currpos = (currpos[0], currpos[1] - 1)
            elif c == '>':
                currpos = (currpos[0] + 1, currpos[1])
            elif c == '<':
                currpos = (currpos[0] - 1, currpos[1])
            houses.add(currpos)

            if idx & 1:
                currposrobosanta = currpos
            else:
                currpossanta = currpos


        print 'Answer to question 2: ' + str(len(houses))
