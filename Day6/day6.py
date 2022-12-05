# AoC 2020
# Day 6
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def get_groups(_lines):
    from functools import reduce
    return reduce(lambda _grp, _per: (_grp.append([]) if _per == '' else _grp[-1].append(_per), _grp)[1], _lines, [[]])


def group_unique(_group):
    return set("".join(_group))


def group_common(_group):
    s = set("abcdefghijklmnopqrstuvwxyz")
    for g in _group:
        s = s.intersection(set(g))

    return s


def file_unique(_f):
    return sum([len(group_unique(g)) for g in get_groups(read_file(_f))])


def file_common(_f):
    return sum([len(group_common(g)) for g in get_groups(read_file(_f))])


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    assert file_unique(INPUT_FILE_TEST) == 11

    # puzzle 2 examples
    assert file_common(INPUT_FILE_TEST) == 6

    # puzzle1
    print(f"total of all questions answered is {file_unique(INPUT_FILE)}")

    # puzzle2
    print(f"total of questions answered by all is {file_common(INPUT_FILE)}")
