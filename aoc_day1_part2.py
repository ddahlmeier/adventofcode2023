# advent of code day 1

from operator import itemgetter
import sys


digit_forms = {"0": ["0", "zero"],
                   "1": ["1", "one"], 
                   "2": ["2", "two"],
                   "3": ["3", "three"],
                   "4": ["4", "four"],
                   "5": ["5", "five"],
                   "6": ["6", "six"],
                   "7": ["7", "seven"],
                   "8": ["8", "eight"],
                   "9": ["9", "nine"]        
                   }


def find_digits(line):
    for index in range(len(line)):
        digit = find_digit(line, index)
        if not digit is None:
            yield digit


def find_digit(line, index):
    for digit, forms in digit_forms.items():
        for form in forms:
            if line[index:index+len(form)] == form:
                return digit
    return None


def parse(input):
    for line in input:
        first, last = itemgetter(0,-1)(list(find_digits(line)))
        yield int(first+last) 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            input = fin.readlines()
    else:
        input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
    print(sum(parse(input)))