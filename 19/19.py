import regex as re, sys, pprint, copy

def executeReplacement(op, molecule):
    a = []
    for i in xrange(len(molecule)):
        r = molecule[:i] + re.sub(op[0], op[1], molecule[i:], count=1)
        if r != molecule:
            a.append(r)
    return a

def searchall(ops, in_molecule, target_molecule, currentstep):
    a = set()
    for op in ops:
        for i in xrange(len(in_molecule)):
            r = in_molecule[:i] + re.sub(op[0], op[1], in_molecule[i:], count=1)
            if r != in_molecule:
                if len(r) > len(target_molecule):
                    break
                elif r == target_molecule:
                    a.add(currentstep)
                else:
                    a.update(searchall(ops, r, target_molecule, currentstep + 1))

    return a

if __name__ == '__main__':
    ops = []
    molecule = ''
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.search(r'([A-Za-z]+) => ([A-Za-z]+)', line)
            if m:
                ops.append(m.groups())
            else:
                m = re.match(r'([A-Za-z]+)', line)
                if m:
                    molecule = m.groups()[0]

    ## test input
    # molecule = 'HOH'
    # ops = [
    # ('H', 'HO'),
    # ('H', 'HO'),
    # ('H', 'OH'),
    # ('O', 'HH')]
    a = set()
    for op in ops:
        a.update(executeReplacement(op, molecule))

    print 'Answer to part 1: ' + str(len(a))


    # molecule = 'HOH'
    # ops = [
    #     ('e','H'),
    #     ('e','O'),
    #     ('H','HO'),
    #     ('H','OH'),
    #     ('O','HH'),
    # ]
    # too brute force, doesn't work
    #print min(searchall(ops, 'e', molecule, 1))
