import itertools
from operator import mul

s = '''1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113'''
s = [int(c.strip()) for c in s.splitlines()]

# gross hacky approach, not general solution probs
e = sum(s)/3

minimum = 0
for i in xrange(1,len(s)):
    if not minimum and sum(s[:-i:-1]) >= e:
        # print s[:-i:-1]
        minimum = i

print e, minimum

print min([reduce(mul,c,1) for c in itertools.combinations(s, minimum) if sum(c) == e])

e = sum(s)/4

minimum = 0
for i in xrange(1,len(s)):
    if not minimum and sum(s[:-i:-1]) >= e:
        # print s[:-i:-1]
        minimum = i

print e, minimum

print min([reduce(mul,c,1) for c in itertools.combinations(s, minimum) if sum(c) == e])
