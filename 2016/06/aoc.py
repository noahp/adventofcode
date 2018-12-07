#!/usr/bin/env python
"""
--- Day 6: Signals and Noise ---
Something is jamming your communications with Santa. Fortunately, your signal is only partially
jammed, and protocol in situations like this is to switch to a simple repetition code to get the
message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal
(your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example,
suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
The most common character in the first column is e; in the second, a; in the third, s, and so on.
Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being
sent?

Your puzzle answer was kjxfwkdh.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?
"""
import sys
import re
import hashlib
from tqdm import tqdm

if __name__ == "__main__":
    cols = None

    with open(sys.argv[1], "r") as input:
        for line in input.readlines():
            if cols is None:
                cols = [dict() for _ in range(len(line.strip()))]
            for i, c in enumerate(line.strip()):
                if c in cols[i]:
                    cols[i][c] += 1
                else:
                    cols[i][c] = 1
    for i in range(len(cols)):
        if len(sys.argv) > 1:
            # part 2
            sys.stdout.write(sorted(cols[i], key=lambda k: cols[i][k], reverse=True)[-1])
        else:
            # part 1
            sys.stdout.write(sorted(cols[i], key=lambda k: cols[i][k], reverse=True)[0])
    sys.stdout.write("\n")
