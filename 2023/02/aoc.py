#!/usr/bin/env python3

"""

only 12 red cubes, 13 green cubes, and 14 blue cubes

"""

import sys

MAX_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class BadPullException(Exception):
    pass


def first_part(lines):
    id_sum = 0
    for index, line in enumerate(lines):
        try:
            pulls = line.strip().partition(": ")[2].split("; ")
            for pull in pulls:
                # parse the pull. form is like "3 blue, 4 red" etc
                colors = pull.split(", ")
                for color in colors:
                    # parse the color. form is like "3 blue"
                    amount, color = color.split(" ")
                    if int(amount) > MAX_COLORS[color]:
                        raise BadPullException
        except BadPullException:
            continue
        id_sum += index + 1

    return id_sum


def second_part(lines):
    power_sum = 0
    for index, line in enumerate(lines):
        min_cube_counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        pulls = line.strip().partition(": ")[2].split("; ")
        for pull in pulls:
            # parse the pull. form is like "3 blue, 4 red" etc
            colors = pull.split(", ")
            for color in colors:
                # parse the color. form is like "3 blue"
                amount, color = color.split(" ")
                min_cube_counts[color] = max(min_cube_counts[color], int(amount))
        # multiply together all values from min_cube_counts
        power = (
            min_cube_counts["red"] * min_cube_counts["green"] * min_cube_counts["blue"]
        )
        power_sum += power

    return power_sum


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # # example input
    # lines = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
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
