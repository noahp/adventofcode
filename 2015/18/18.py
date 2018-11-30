import re, sys, pprint, copy

def animate(lights):
    ''' One increment of animation on the supplied configuration. '''
    result = copy.deepcopy(lights)
    for row in range(len(lights)):
        for col in range(len(lights[0])):
            neighborsOn = 0
            # bunch of tries to handle running off the edge of the array.
            # neighbors are numbered as:
            # 123
            # 4X5
            # 678
            # 1
            if row - 1 >= 0 and col - 1 >= 0 and lights[row-1][col-1] == '#':
                neighborsOn += 1
            # 2
            if row - 1 >= 0 and lights[row-1][col] == '#':
                neighborsOn += 1
            # 3
            if row - 1 >= 0 and col + 1 < len(lights) and lights[row-1][col+1] == '#':
                neighborsOn += 1
            # 4
            if col - 1 >= 0 and lights[row][col-1] == '#':
                neighborsOn += 1
            # 5
            if col + 1 < len(lights) and lights[row][col+1] == '#':
                neighborsOn += 1
            # 6
            if row + 1 < len(lights) and col - 1 >= 0 and lights[row+1][col-1] == '#':
                neighborsOn += 1
            # 7
            if row + 1 < len(lights) and lights[row+1][col] == '#':
                neighborsOn += 1
            # 8
            if row + 1 < len(lights) and col + 1 < len(lights) and lights[row+1][col+1] == '#':
                neighborsOn += 1

            if lights[row][col] == '#' and (neighborsOn == 2 or neighborsOn == 3):
                result[row][col] = '#'
            elif lights[row][col] == '.' and neighborsOn == 3:
                result[row][col] = '#'
            else:
                result[row][col] = '.'

    return result

def animate2(lights):
    ''' One increment of animation on the supplied configuration. '''
    result = copy.deepcopy(lights)
    for row in range(len(lights)):
        for col in range(len(lights[0])):
            neighborsOn = 0
            # bunch of tries to handle running off the edge of the array.
            # neighbors are numbered as:
            # 123
            # 4X5
            # 678
            # 1
            if row - 1 >= 0 and col - 1 >= 0 and lights[row-1][col-1] == '#':
                neighborsOn += 1
            # 2
            if row - 1 >= 0 and lights[row-1][col] == '#':
                neighborsOn += 1
            # 3
            if row - 1 >= 0 and col + 1 < len(lights) and lights[row-1][col+1] == '#':
                neighborsOn += 1
            # 4
            if col - 1 >= 0 and lights[row][col-1] == '#':
                neighborsOn += 1
            # 5
            if col + 1 < len(lights) and lights[row][col+1] == '#':
                neighborsOn += 1
            # 6
            if row + 1 < len(lights) and col - 1 >= 0 and lights[row+1][col-1] == '#':
                neighborsOn += 1
            # 7
            if row + 1 < len(lights) and lights[row+1][col] == '#':
                neighborsOn += 1
            # 8
            if row + 1 < len(lights) and col + 1 < len(lights) and lights[row+1][col+1] == '#':
                neighborsOn += 1

            # don't touch corners..
            if (((row == 0) and (col == 0 or col == len(lights[0]) - 1)) or
                ((row == len(lights) - 1) and (col == 0 or col == len(lights[0]) - 1))):
                result[row][col] = '#'
            elif lights[row][col] == '#' and (neighborsOn == 2 or neighborsOn == 3):
                result[row][col] = '#'
            elif lights[row][col] == '.' and neighborsOn == 3:
                result[row][col] = '#'
            else:
                result[row][col] = '.'

    return result

if __name__ == '__main__':
    lights = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            lights.append([c for c in line.strip()])

    lights2 = copy.deepcopy(lights)
    # print '\n'.join([''.join(c) for c in lights])
    # print '*'*25

    # part 1
    for i in xrange(100):
        lights = animate(lights)
    a = sum([c.count('#') for c in lights])

    print 'Answer to part 1: ' + str(a)

    # part 2
    for i in xrange(100):
        lights2 = animate2(lights2)
    a = sum([c.count('#') for c in lights2])

    print 'Answer to part 2: ' + str(a)
