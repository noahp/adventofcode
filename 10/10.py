import itertools

if __name__ == '__main__':
    # 1. part one
    qinput = '1113122113'

    for i in xrange(40):
        grouped = [list(g) for k, g in itertools.groupby(qinput)]
        qinput = ''.join(['%d'%len(x) + x[0] for x in grouped])
    print 'Answer to part 1: ' + str(len(qinput))

    for i in xrange(50-40):
        grouped = [list(g) for k, g in itertools.groupby(qinput)]
        qinput = ''.join(['%d'%len(x) + x[0] for x in grouped])
    print 'Answer to part 2: ' + str(len(qinput))
