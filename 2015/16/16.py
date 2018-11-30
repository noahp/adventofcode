import re, sys, itertools, pprint
from operator import mul

# traits
traits = ['children', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes',]
target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def score1(sue, trait):
    if sue[trait] == target[trait]:
        return 1

    return 0

def score2(sue, trait):
    if trait in ['cats', 'trees']:
        if sue[trait] > target[trait]:
            return 1
    elif trait in ['pomeranians', 'goldfish']:
        if sue[trait] < target[trait]:
            return 1
    elif sue[trait] == target[trait]:
        return 1

    return 0


if __name__ == '__main__':
    aunts = []
    scores1 = []
    scores2 = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            # aunt entry is like name, {traits}. may not actually need it
            s1 = 0
            s2 = 0
            sue = {}
            for trait in traits:
                m = re.search(trait + r': ([0-9]+)', line)
                if m:
                    sue[trait] = int(m.groups()[0])
                    s1 += score1(sue, trait)
                    s2 += score2(sue, trait)
                else:
                    sue[trait] = None
            scores1.append(s1)
            scores2.append(s2)
            aunts.append(sue)

    print 'Answer to part 1: ' + str(scores1.index(max(scores1)) + 1)
    print 'Answer to part 2: ' + str(scores2.index(max(scores2)) + 1)
