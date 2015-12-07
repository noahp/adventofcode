import sys, re
import array

def toint(a):
    try:
        return int(a)
    except ValueError:
        return a

def and_test(inargs, defined):
    # try to reconcile operation with existing data
    a,b = inargs[:2]
    a = toint(a)
    b = toint(b)
    if type(a) is str:
        if a in defined:
            a = defined[a]
        else:
            return None

    if type(b) is str:
        if b in defined:
            b = defined[b]
        else:
            return None
    return a & b

def or_test(inargs, defined):
    # try to reconcile operation with existing data
    a,b = inargs[:2]
    a = toint(a)
    b = toint(b)
    if type(a) is str:
        if a in defined:
            a = defined[a]
        else:
            return None

    if type(b) is str:
        if b in defined:
            b = defined[b]
        else:
            return None
    return a | b

def set_test(inargs, defined):
    a = inargs[0]
    a = toint(a)
    if isinstance(a, str):
        if a in defined:
            a = defined[a]
        else:
            return None
    return a

def not_test(inargs, defined):
    a = inargs[0]
    a = toint(a)
    if type(a) is str:
        if a in defined:
            a = defined[a]
        else:
            return None
    return (~a) & 0xFFFF

def ls_test(inargs, defined):
    a,b = inargs[:2]
    a = toint(a)
    b = toint(b)
    if type(a) is str:
        if a in defined:
            a = defined[a]
        else:
            return None
    return a << b

def rs_test(inargs, defined):
    a,b = inargs[:2]
    a = toint(a)
    b = toint(b)
    if type(a) is str:
        if a in defined:
            a = defined[a]
        else:
            return None
    return a >> b

re_and = re.compile(r'^(?:([a-z0-9]+) AND ([a-z0-9]+) -> ([a-z]+))')
re_or = re.compile(r'^(?:([a-z0-9]+) OR ([a-z0-9]+) -> ([a-z]+))')
re_set = re.compile(r'^(?:([a-z0-9]+) -> ([a-z]+))')   # signal copied
re_not = re.compile(r'^(?:NOT ([a-z0-9]+) -> ([a-z]+))')
re_ls = re.compile(r'(?:([a-z0-9]+) LSHIFT ([0-9]+) -> ([a-z]+))')
re_rs = re.compile(r'(?:([a-z0-9]+) RSHIFT ([0-9]+) -> ([a-z]+))')

op_list = [
    (re_and, and_test),
    (re_or, or_test),
    (re_set, set_test),
    (re_not, not_test),
    (re_ls, ls_test),
    (re_rs, rs_test),
]

def partone(f):
    r = re.compile(r'((?:turn on)|(?:turn off)|(?:toggle)) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')
    a = {}
    # gather input
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # incrementally work through the rest, setting values derived from
    # existing literally set values, until we've exhausted all progress (stuck)
    # or found the answer
    lastLen = 0
    rem = lines[:]  # copy
    while len(rem) != lastLen:
        print '>> ' + str(len(rem))
        lastLen = len(rem)  # track progress
        for r in rem:
            for rgx, op in op_list:
                m = rgx.search(r)
                if m:
                    test = op(m.groups(), a)
                    if test is not None:
                        a[m.groups()[-1]] = test
                        # print m.groups()[-1], '%X'%test
                        rem.remove(r)
                        if m.groups()[-1] is 'a':
                            break

    return a['a']

def parttwo(f):
    return ''

if __name__ == '__main__':
    # 1. part one
    answer = partone(sys.argv[1])
    print 'Answer to part 1: ' + str(answer)

    # 2. part two
    answer = parttwo(sys.argv[1])
    print 'Answer to part 2: ' + str(answer)
