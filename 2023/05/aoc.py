#!/usr/bin/env python3
import multiprocessing
import re
import sys
from dataclasses import dataclass

from tqdm import tqdm


@dataclass
class RangeMap:
    # source and destination number
    src: int
    dst: int
    # range
    length: int

    def __str__(self):
        return f"{{.src = {self.src}, .dst = {self.dst}, .length = {self.length}}}"


@dataclass
class CategoryMap:
    # names of the src and dst, eg "seed-to-soil"
    srcname: str
    dstname: str
    # list of RangeMap objects
    maps: list[RangeMap]

    def map(self, number):
        for rmap in self.maps:
            # check if number is in range
            if rmap.src <= number < rmap.src + rmap.length:
                return rmap.dst + (number - rmap.src)
        # if not in map, return the same destination number
        return number

    def print_as_c_string(self):
        maps = ",\n            ".join([str(map_) for map_ in self.maps])
        return f"""const struct map {self.srcname}_{self.dstname}_map =
    {{
        .srcname = "{self.srcname}",
        .dstname = "{self.dstname}",
        .map_count = {len(self.maps)},
        .maps = {{
            {maps}
        }},
    }};
"""


def parse_maps(lines):
    # now we start mapping. first break the lines into sections
    # each section is a map
    maps = []
    thismap = None
    for line in lines:
        if line.endswith("map:"):
            # parse out src-to-dst name
            srcname, _, dstname = line.split()[0].split("-")
            thismap = CategoryMap(srcname, dstname, [])
        elif line != "":
            # parse out the map
            dst, src, length = map(int, line.split())
            thismap.maps.append(RangeMap(src, dst, length))
        else:
            # empty line, end of map
            if thismap:
                maps.append(thismap)
            thismap = None
    if thismap:
        maps.append(thismap)
    return maps


def first_part(lines):
    # parse out the seed numbers
    # convert list to iterator, so we can chomp as we go
    lines = iter(lines)
    seeds = list(map(int, next(lines).split()[1:]))
    # print("seeds:", seeds)

    maps = parse_maps(lines)

    locations = []
    for seed in seeds:
        # print("seed:", seed)
        for thismap in maps:
            seed = thismap.map(seed)
            # print(thismap.dstname, seed)
        locations.append(seed)
    return min(locations)


# import ray

# ray.init()


# @ray.remote
def process_range(start, count, maps):
    min_location = None

    for seed in range(start, start + count):
        for thismap in maps:
            seed = thismap.map(seed)
            # print(thismap.dstname, seed)
        min_location = seed if min_location is None else min(min_location, seed)
    return min_location


def maps_to_c(maps):
    with open("maps.h", "w") as f:
        # print out the maps as C code

        # print the map struct definition
        f.write(
            """
struct map_entry {
    long int src;
    long int dst;
    long int length;
};

struct map {
    const char *srcname;
    const char *dstname;
    int map_count;
    const struct map_entry maps[];
};
"""
        )

        for map_ in maps:
            f.write(map_.print_as_c_string())

        # print an array of maps in sequence
        f.write(
            """const struct map *maps[] =
        {
"""
        )
        for map_ in maps:
            f.write(f"        &{map_.srcname}_{map_.dstname}_map,\n")
        f.write("""    };\n""")


def second_part(lines):
    # in this mode, the seed line actually is pairs of [starting_number, count]
    # convert list to iterator, so we can chomp as we go
    lines = iter(lines)
    seeds = list(map(int, next(lines).split()[1:]))
    # convert to pairs
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    # print("seeds:", seeds)
    maps = parse_maps(lines)
    maps_to_c(maps)

    # now we crunch through every seed.
    min_location = None
    total_seed_count = sum([count for _, count in seeds])

    for start, count in seeds:
        print("seed:", start, count)

        # # process a single seed
        # for thismap in maps:
        #     start = thismap.map(start)
        #     # print(thismap.dstname, seed)
        # print(start)

        # # we need to parallelize the processing here based on number of cpu
        # # cores. so first, split the work into chunks
        # cpu_count = multiprocessing.cpu_count()
        # count_per_chunk = count // cpu_count
        # print("seed:", start, count, "count_per_chunk:", count_per_chunk)
        # remainder = count % cpu_count
        # # the work buckets are [(start, start + count_per_chunk), ...]
        # work_buckets = [
        #     (start + i * count_per_chunk, count_per_chunk, maps)
        #     for i in range(cpu_count)
        # ]
        # work_buckets[-1] = (work_buckets[-1][0], work_buckets[-1][1] + remainder, maps)

        # # # now we process each bucket in parallel
        # # result = ray.get([process_range.remote(*bucket) for bucket in work_buckets])
        # # print("result:", result)

        # with multiprocessing.Pool() as pool:
        #     min_locations = pool.starmap(process_range, work_buckets)
        #     min_location = (
        #         min(min_locations)
        #         if min_location is None
        #         else min(min_location, min(min_locations))
        #     )

        # break
    return min_location


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = list(lines)

    # example input
    lines = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
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
