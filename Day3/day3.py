# AoC 2020
# Day 3
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE = "input.txt"
INPUT_TEST = "input_test1.txt"

PUZZLE1_H_OFFSET: int = 3
PUZZLE1_V_OFFSET: int = 1

PUZZLE2_INPUTS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def count_trees(_filename, _h, _v):
    count = pos = 0
    lines = read_file(_filename)

    for i, line in enumerate(lines):
        if (i % _v) != 0:
            continue
        elif line[pos] == '#':
            count = count + 1
        pos = (pos + _h) % len(line)

    return count


# check we're being run directly
if __name__ == '__main__':

    # assertions against known, worked examples
    assert count_trees(INPUT_TEST, PUZZLE1_H_OFFSET, PUZZLE1_V_OFFSET) == 7
    assert [count_trees(INPUT_TEST, h, v) for (h, v) in PUZZLE2_INPUTS] == [2, 7, 3, 4, 2]

    # puzzle1
    trees = count_trees(INPUT_FILE, PUZZLE1_H_OFFSET, PUZZLE1_V_OFFSET)
    print(f"Puzzle 1: Would hit {trees} trees")

    # puzzle2
    product = 1
    for (h, v) in PUZZLE2_INPUTS:
        product = product * count_trees(INPUT_FILE, h, v)
    print(f"Puzzle 2: Product is {product}")
