#!/usr/bin/env python3

import sys


def get_first_and_last_digit_in_line(line):
    """takes a string, and returns the first and last single numerical digit as
    a single number"""
    digits = list(filter(str.isdigit, line))
    first = digits[0]
    last = digits[-1]

    return int(first) * 10 + int(last)


def get_first_and_last_digit_in_line_2(line):
    """takes a string. scans from left to right looking for either the first
    spelled out digit, "one", "two", etc, or the first numerical digig, "1",
    "2", etc, whichever comes first. then scans from right to left looking for
    the same. returns the sum of the two digits found"""
    first = None
    last = None
    for i in range(len(line)):
        if line[i].isdigit():
            first = line[i]
            break
        elif line[i : i + 3] == "one":
            first = "1"
            break
        elif line[i : i + 3] == "two":
            first = "2"
            break
        elif line[i : i + 5] == "three":
            first = "3"
            break
        elif line[i : i + 4] == "four":
            first = "4"
            break
        elif line[i : i + 4] == "five":
            first = "5"
            break
        elif line[i : i + 3] == "six":
            first = "6"
            break
        elif line[i : i + 5] == "seven":
            first = "7"
            break
        elif line[i : i + 5] == "eight":
            first = "8"
            break
        elif line[i : i + 4] == "nine":
            first = "9"
            break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            last = line[i]
            break
        elif line[i : i + 3] == "one":
            last = "1"
            break
        elif line[i : i + 3] == "two":
            last = "2"
            break
        elif line[i : i + 5] == "three":
            last = "3"
            break
        elif line[i : i + 4] == "four":
            last = "4"
            break
        elif line[i : i + 4] == "five":
            last = "5"
            break
        elif line[i : i + 3] == "six":
            last = "6"
            break
        elif line[i : i + 5] == "seven":
            last = "7"
            break
        elif line[i : i + 5] == "eight":
            last = "8"
            break
        elif line[i : i + 4] == "nine":
            last = "9"
            break

    return int(first) * 10 + int(last)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # example input
    #  lines = [
    #      "1abc2",
    #      "pqr3stu8vwx",
    #      "a1b2c3d4e5f",
    #      "treb7uchet",
    # ]
    print("first part:", sum(get_first_and_last_digit_in_line(line) for line in lines))

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
    print(
        "second part:", sum(get_first_and_last_digit_in_line_2(line) for line in lines)
    )
