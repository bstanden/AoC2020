# AoC 2020
# Day 5
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE = "input.txt"
INPUT_TEST = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
TEST_RESULTS = [357, 567, 119, 820]


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def bpart(_s, _f):
    return int("".join(["0" if c == _f else "1" for c in _s]), 2)


def get_seat_ids(line):
    return bpart(line[:7], "F") * 8 + bpart(line[7:], "L")


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples

    # puzzle 1 example
    assert TEST_RESULTS == [get_seat_ids(line) for line in INPUT_TEST]

    # puzzle 2 examples
    pass  # no examples for puzzle2 today

    # get seat id list
    id_list = [get_seat_ids(line) for line in read_file(INPUT_FILE)]

    # puzzle1
    max_id = max(id_list)
    print(f"max seat id is {max_id}")

    # puzzle2
    my_seat = set(range(min(id_list), max(id_list) + 1)).difference(set(id_list))  # set of all empty seats
    print(f"my seat id is {my_seat}")
