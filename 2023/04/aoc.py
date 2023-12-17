#!/usr/bin/env python3
import re
import sys


def get_line_wincount(line):
    # parse into [Card \d+]: (?:(\d+) )+|(?:(\d+) )+
    _card, data = line.split(":")
    winners, scratches = data.split("|")
    winners = list(map(int, winners.split()))
    scratches = list(map(int, scratches.split()))
    # print(winners, scratches)
    # count the number of scratches in winners
    count = 0
    for scratch in scratches:
        if scratch in winners:
            count += 1
    return count


def get_line_index(line):
    # get the 'Card \d+' part and return the index
    card, _ = line.split(":")
    card = card.split()[1]
    return int(card)


def first_part(lines):
    winvals = []
    for line in lines:
        count = get_line_wincount(line)
        winval = (1 << (count - 1)) if count else 0
        winvals.append(winval)

    return sum(winvals)


def recurse_copies(lines, copies, count_of_all_cards):
    for copy in copies:
        count = get_line_wincount(copy)
        if count:
            copy_index = get_line_index(copy)
            new_copies = lines[copy_index : copy_index + count]
            # print(list(map(get_line_index, new_copies)))
            count_of_all_cards += recurse_copies(lines, new_copies, 0) + 1
        else:
            count_of_all_cards += 1
    return count_of_all_cards


def second_part(lines):
    # ugh this one sucks
    sys.setrecursionlimit(15000000)
    return recurse_copies(lines, lines, 0)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = filter(lambda line: len(line) > 0, lines)
    lines = list(lines)

    # # example input
    # lines = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    # ]
    print("first part:", first_part(lines))

    # second part

    # example input
    # lines = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]
    print("second part:", second_part(lines))
