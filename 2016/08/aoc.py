#!/usr/bin/env python
"""
--- Day 8: Two-Factor Authentication ---
You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
"""
import sys
import re

if __name__ == "__main__":

    count = 0
    total = 0

    rect = re.compile(r"rect (\d+)x(\d+)")
    rotate_col = re.compile(r"rotate column x=(\d+) by (\d+)")
    rotate_row = re.compile(r"rotate row y=(\d+) by (\d+)")

    pixels = list([[0] * 50 for x in range(6)])
    # pixels = list([[0] * 7 for x in range(4)])

    with open(sys.argv[1], "r") as input:
        for line in input.readlines():
        # for line in "rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1\n".splitlines():
            r = rect.match(line.strip())
            if r:
                for y in range(int(r.group(2))):
                    for x in range(int(r.group(1))):
                        pixels[y][x] = 1

            c = rotate_row.match(line.strip())
            if c:
                rotate = (int(c.group(2))) % len(pixels[0])
                pixels[int(c.group(1))] = pixels[int(c.group(1))][-rotate:] + pixels[int(c.group(1))][:-rotate]

            c = rotate_col.match(line.strip())
            if c:
                col = []
                for x in range(len(pixels)):
                    col += [pixels[x][int(c.group(1))]]

                rotate = (int(c.group(2))) % len(col)
                col = col[-rotate:] + col[:-rotate]
                for i,l in enumerate(col):
                    pixels[i][int(c.group(1))] = l
            # for row in pixels:
            #     print("".join([str(x) for x in row]))
            # print "\n"

    total = 0
    for row in pixels:
        print("".join(["#" if x else " " for x in row]))
        total += sum(row)

    print(total)
