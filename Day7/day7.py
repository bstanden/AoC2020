# AoC 2020
# Day 7
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"
MY_BAG = "shiny gold"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def get_rules(_lines):
    _rules = {}

    for line in _lines:
        colour, content = get_rule(line)
        _rules[colour] = content

    return _rules


def get_rule(line):
    tokens = line.split(" ")
    colour = " ".join(tokens[:2])
    contents = {}
    get_contents(tokens[4:], contents)
    return colour, contents


def get_contents(_tokens, _contents):
    if _tokens == [] or _tokens[0] == "no":
        return
    colour, count = (_tokens[1:3], int(_tokens[0]))
    _contents[" ".join(colour)] = count
    get_contents(_tokens[4:], _contents)


def get_containers(_colour, _rules):
    _containers = []
    for _rule in _rules.keys():
        if can_contain(_colour, _rule, _rules):
            _containers.append(_rule)
    return len(_containers)


def can_contain(_colour, _rule, _rules):
    if not _rule:
        return False
    elif _colour in _rules[_rule].keys():
        return True
    return any([can_contain(_colour, c, _rules) for c in _rules[_rule].keys()])


def get_bag_contents(_colour, _rules):
    _total = 0
    for _contents in _rules[_colour].keys():
        _total = _total + _rules[_colour][_contents] * (get_bag_contents(_contents, _rules) + 1)
    return _total


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    rules = get_rules(read_file(INPUT_FILE_TEST))

    # puzzle 1 example
    num_containers = get_containers(MY_BAG, rules)
    print(f"(TEST) number of bags that could contain {MY_BAG} is {num_containers}")
    assert num_containers == 4

    # puzzle 2 examples
    num_containers = get_bag_contents(MY_BAG, rules)
    print(f"(TEST) number of bags within {MY_BAG} is {num_containers}")
    assert num_containers == 32

    # puzzle1
    rules = get_rules(read_file(INPUT_FILE))
    num_containers = get_containers(MY_BAG, rules)
    print(f"number of bags that could contain {MY_BAG} is {num_containers}")

    # puzzle2
    num_containers = get_bag_contents(MY_BAG, rules)
    print(f"number of bags within {MY_BAG} is {num_containers}")
