import re, sys, itertools, copy
'''
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
'''

def operation(op, a, b, pc):
    ''' Execute operation and return a,b,pc'''
    if op.find('hlf') != -1:
        if op[4] == 'a':
            a = a/2
        elif op[4] == 'b':
            b = b/2
        pc = pc + 1

    elif op.find('tpl') != -1:
        if op[4] == 'a':
            a = a*3
        elif op[4] == 'b':
            b = b*3
        pc = pc + 1

    elif op.find('inc') != -1:
        if op[4] == 'a':
            a = a+1
        elif op[4] == 'b':
            b = b+1
        pc = pc + 1

    elif op.find('jmp') != -1:
        m = re.search(r'jmp \+{0,1}(-{0,1}[0-9]+)', op)
        if not m:
            raise UserWarning('Whoops! ' + op)
        pc += int(m.group(1))

    elif op.find('jie') != -1:
        m = re.search(r'jie ([ab]), \+{0,1}(-{0,1}[0-9]+)', op)
        if not m:
            raise UserWarning('Whoops! ' + op)
        if m.group(1) == 'a':
            if a & 1 == 0:
                pc += int(m.group(2))
            else:
                pc += 1
        elif m.group(1) == 'b':
            if a & 1 == 0:
                pc += int(m.group(2))
            else:
                pc += 1

    elif op.find('jio') != -1:
        m = re.search(r'jio ([ab]), \+{0,1}(-{0,1}[0-9]+)', op)
        if not m:
            raise UserWarning('Whoops! ' + op)
        if m.group(1) == 'a':
            if a == 1:
                pc += int(m.group(2))
            else:
                pc += 1
        elif m.group(1) == 'b':
            if b == 1:
                pc += int(m.group(2))
            else:
                pc += 1

    return a, b, pc

def runIt(prog, a=0, b=0):
    pc = 0

    while pc < len(prog):
        a,b,pc = operation(prog[pc],a,b,pc)

    return a,b

if __name__ == '__main__':
    # 1. get puzzle input
    prog = []
    with open(sys.argv[1], 'r') as f:
        prog = [c.strip() for c in f.readlines()]

    # run the program
#     prog = [c.strip() for c in '''inc a
# jio a, +2
# tpl a
# inc a'''.splitlines()]

    a,b = runIt(prog)
    print 'Answer to part 1: ' + str(b)

    a,b = runIt(prog, a=1)
    print 'Answer to part 2: ' + str(b)
