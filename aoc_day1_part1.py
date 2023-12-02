# advent of code day 1

from operator import itemgetter
import sys


def first_last_digit(line):
    return itemgetter(0,-1)(list(filter(lambda x:x.isdigit(), line)))


def parse(input):
    for line in input:
        first, last = first_last_digit(line)
        yield int(first+last) 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            input = fin.readlines()
    else:
        input = """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet""".splitlines()
    print(sum(parse(input)))