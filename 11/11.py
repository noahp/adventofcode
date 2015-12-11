import re, string

def incrementPw(instr):
    for i,x in enumerate(instr[::-1]):
        print i,x

def validatePw(instr):
    # 1, sequence of characters
    s = []
    for c in instr:
        if len(s) == 0:
            s.append(c)
        elif len(s) < 3:
            if c == chr(ord(s[-1]) + 1):
                s.append(c)
                if len(s) == 3:
                    break
            else:
                s = [c]
    if len(s) != 3:
        print 'no seq'
        return False

    # 2, don't contain [i, o, l]
    if 'i' in instr or 'o' in instr or 'l' in instr:
        print 'iol'
        return False

    # 3, two different, non-overlapping pairs of letters
    m = re.findall(r'(([a-z])(\2))', instr)
    if not m:
        print 'no dup'
        return False
    m = set(m)
    if len(m) < 2:
        return False

    return True

if __name__ == '__main__':
    incrementPw('vzbxkghb')

    # # 1. part one
    # qinput = 'vzbxkghb'
    # a = ''
    # while True:
    #     qinput = incrementPw(qinput)
    #     if validatePw(qinput):
    #         a = qinput
    #         break
    #
    # print a
