#!/usr/bin/env python3
import re
import sys


def first_part(lines):
    # first add up all the numbers in the lines
    sum_result = 0
    for line in lines:
        nums = re.findall(r"\d+", line)
        for num in nums:
            sum_result += int(num)

    # now search for any numbers that aren't adjacent to a symbol (a character
    # that's not a .), either horizontally or vertically or diagonally
    ignore_nums = []
    for i in range(len(lines)):
        prev_line = lines[i - 1] if i > 0 else None
        curr_line = lines[i].strip()
        next_line = lines[i + 1] if i < len(lines) - 1 else None

        number_chars = []  # accumulate digit chars while scanning
        found_adjacent_symbol_for_current_digit_group = False
        for j in range(len(curr_line)):
            if curr_line[j].isdigit():
                number_chars.append(curr_line[j])
                # check the surrounding up to 8 chars for symbols. symbols are
                # anything that's not a digit or a .
                # ...
                # .1.
                # ...
                surrounding_chars = []
                # left chars
                if j > 0:
                    surrounding_chars.append(curr_line[j - 1])
                    if prev_line:
                        surrounding_chars.append(prev_line[j - 1])
                    if next_line:
                        surrounding_chars.append(next_line[j - 1])
                # above and below chars
                if prev_line:
                    surrounding_chars.append(prev_line[j])
                if next_line:
                    surrounding_chars.append(next_line[j])
                # right chars
                if j < len(curr_line) - 1:
                    surrounding_chars.append(curr_line[j + 1])
                    if prev_line:
                        surrounding_chars.append(prev_line[j + 1])
                    if next_line:
                        surrounding_chars.append(next_line[j + 1])
                # now check for symbols
                for char in surrounding_chars:
                    if not char.isdigit() and char != ".":
                        found_adjacent_symbol_for_current_digit_group = True
                        break
                # debug
                # print(
                #     curr_line[j],
                #     surrounding_chars,
                #     found_adjacent_symbol_for_current_digit_group,
                # )
            else:
                # end of digit group?
                if len(number_chars) > 0:
                    if not found_adjacent_symbol_for_current_digit_group:
                        ignore_nums.append(int("".join(number_chars)))
                    number_chars = []
                    found_adjacent_symbol_for_current_digit_group = False
        # end of line, check if there's a digit group
        if len(number_chars) > 0:
            if not found_adjacent_symbol_for_current_digit_group:
                ignore_nums.append(int("".join(number_chars)))
            number_chars = []
            found_adjacent_symbol_for_current_digit_group = False

    return sum_result - sum(ignore_nums)


def line_parse_digit_groups(line):
    # for each line, create a list that's indexed by offset into the line, and
    # if there's a digit group containing that offset, the number in the group
    # is stored in the list at that offset.
    # example:
    # line = "1..23"
    # result = [1, None, None, 23, 23]
    offset_to_number = []
    current_digit_group = []
    for i in range(len(line)):
        if line[i].isdigit():
            current_digit_group.append(line[i])
        else:
            if len(current_digit_group) > 0:
                for j in range(len(current_digit_group)):
                    offset_to_number.append(int("".join(current_digit_group)))
                current_digit_group = []
            offset_to_number.append(None)
    # end of line, check if there's a digit group
    if len(current_digit_group) > 0:
        for j in range(len(current_digit_group)):
            offset_to_number.append(int("".join(current_digit_group)))

    return offset_to_number


def second_part(lines):
    # for each line, create a list of numbers in the string and the starting and
    # ending index for each, and a list of '*' in the string with their index.
    ratios = []
    for i in range(len(lines)):
        prev_line_groups = line_parse_digit_groups(lines[i - 1]) if i > 0 else None
        curr_line_groups = line_parse_digit_groups(lines[i].strip())
        next_line_groups = (
            line_parse_digit_groups(lines[i + 1]) if i < len(lines) - 1 else None
        )

        # scan for * in the line, and check the surrounding 8 positions for
        # numbers
        ratio_pairs = []
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                print(prev_line_groups, curr_line_groups, next_line_groups)
                # check the surrounding up to 8 chars for numbers
                # ...
                # .1.
                # ...
                surrounding_numbers = []
                # left and right chars same line
                if j > 0:
                    surrounding_numbers.append(curr_line_groups[j - 1])
                if j < len(curr_line_groups) - 1:
                    surrounding_numbers.append(curr_line_groups[j + 1])
                # the previous and next line chars can be inside the same digit
                # group, and we don't want to double count. to do that, we only
                # count once unless the same column character is not a digit
                # group. this only applies when the column is not the first or
                # last
                if j > 0 and j < len(curr_line_groups) - 1:
                    if not prev_line_groups[j]:
                        surrounding_numbers.append(prev_line_groups[j - 1])
                        surrounding_numbers.append(prev_line_groups[j + 1])
                    if not next_line_groups[j]:
                        surrounding_numbers.append(next_line_groups[j - 1])
                        surrounding_numbers.append(next_line_groups[j + 1])
                # first or last column, only count 1 number from the previous
                # and next lines
                elif j == 0:
                    if prev_line_groups:
                        surrounding_numbers.append(next(prev_line_groups[j : j + 1]))

                    if next_line_groups:
                        surrounding_numbers.append(next(next_line_groups[j : j + 1]))

                elif j == len(curr_line_groups) - 1:
                    if prev_line_groups:
                        surrounding_numbers.append(next(prev_line_groups[j - 1 : j]))

                    if next_line_groups:
                        surrounding_numbers.append(next(next_line_groups[j - 1 : j]))

                print("surrounding: ", surrounding_numbers)

    # look for 2 numbers touching the *.
    # there are 4 cases:
    # 1. 2 numbers on the same line:
    #    1*1
    # 2. 2 numbers on different lines:
    #   111
    #    *
    #   111
    #   this case, the numbers can have start-end indices that contain
    #   the * column indices or one position higher or lower:
    #   1
    #    *
    #     1
    # 3. 1 number on the same line as the star, 1 number not:
    #   1*
    #   1
    # 4. numbers on the same line, not touching the star:
    #   1 1
    #    *

    return ratios


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = filter(lambda line: len(line) > 0, lines)
    lines = list(lines)

    # example input
    lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
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
