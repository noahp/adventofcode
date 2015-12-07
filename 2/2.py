import sys


if __name__ == '__main__':
    a = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            l,w,h = (int(c) for c in line.strip().split('x'))

            a += 2*l*w + 2*w*h + 2*h*l
            a += min(l*w, w*h, h*l)

print a
