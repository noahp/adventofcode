import sys

if __name__ == '__main__':
    # 1. wrapping paper area needed
    # 2. ribbon length needed
    a = 0
    ribbon = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            l,w,h = (int(c) for c in line.strip().split('x'))

            a += 2*l*w + 2*w*h + 2*h*l
            a += min(l*w, w*h, h*l)

            ribbon += min(2*(l+w), 2*(w+h), 2*(h+l))
            ribbon += l*w*h

    print 'Answer to question 1: ' + str(a)
    print 'Answer to question 2: ' + str(ribbon)
