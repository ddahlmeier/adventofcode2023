# advent of code day 2

import sys


def parse(input):
    games = []
    for line in input:
        game, values = line.split(":")
        game = int(game.split()[1])
        sets = []
        for subset in values.split(";"):
            counts = {"red": 0, "green": 0, "blue": 0}
            for item in subset.split(","):
                count, color = item.split()
                counts[color] = int(count)
            sets.append(counts)
        games.append((game, sets))
    return games


def is_possible_game(game, bag):
    _, sets = game
    return all((is_possible_set(set, bag) for set in sets))

def is_possible_set(set, bag):
    return all((set[color] <= bag[color] for color in bag.keys()))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fin:
            input = fin.readlines()
    else:
        input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()
    games = parse(input)
    bag = {"red": 12, "green": 13, "blue": 14}
    possible_games = [game[0] for game in games if is_possible_game(game, bag)]
    print(sum(possible_games))