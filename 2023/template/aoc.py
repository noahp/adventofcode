#!/usr/bin/env python3
import re
import sys


def first_part(lines):
    pass


def second_part(lines):
    pass


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = filter(lambda line: len(line) > 0, lines)
    lines = list(lines)

    # # example input
    # lines = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
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
