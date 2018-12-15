#!/usr/bin/env python
"""
--- Day 7: Internet Protocol Version 7 ---
While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to
figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two different
characters followed by the reverse of that pair, such as xyyx or abba. However,
the IP also must not have an ABBA within any hypernet sequences, which are
contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""
import sys
import re

if __name__ == "__main__":

    count = 0
    total = 0

    bracketed = re.compile(r"\[(.*?)\]")
    found = re.compile(r"([a-z])([a-z^\1])\2\1")
    with open(sys.argv[1], "r") as input:
        for line in input.readlines():
            total += 1
        # for line in [
        #     "abba[mnop]qrst",
        #     "abcd[bddb]xyyx",
        #     "aaaa[qwer]tyui",
        #     "ioxxoj[asdfgh]zxcvbn",
        # ]:
            f = found.search(line.strip())
            a = bracketed.search(line.strip())
            if a:
                a = found.search(a.group(1))
                if a:
                    print("-- " + a.group(0))
                    continue

            if f:
                if len(set(f.group(0))) == 2:
                    print("++ " + line.strip() + "," + f.group(0))
                    count += 1
            # else:
            #     print(">> " + line)

    print(str(count) + "/" + str(total))
