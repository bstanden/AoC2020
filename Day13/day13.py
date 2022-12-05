# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def find_bus(_lines):
    _timestamp = int(_lines[0])
    _bus_list = {}

    for _bus_id in _lines[1].split(","):
        if _bus_id != 'x':
            _id = int(_bus_id)
            _bus_list[_id] = _id - (_timestamp % _id)

    return min(_bus_list.items(), key=lambda x: x[1])


def chinese_remainder(_n, _a):  # rosetta code
    from functools import reduce
    _sum = 0
    prod = reduce(lambda a, b: a * b, _n)
    for n_i, a_i in zip(_n, _a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod


def mul_inv(a, b):  # rosetta code
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_time(_lines):
    a = []
    n = []
    for _n, _x in enumerate(_lines[1].split(',')):
        if _x != "x":
            _bus_id = int(_x)
            n.append(_bus_id)
            a.append(_bus_id - _n)

    return chinese_remainder(n, a)


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    bus_id, wait_time = find_bus(read_file(INPUT_FILE_TEST))
    print(f"(TEST) bus id: {bus_id}, wait time={wait_time}, product = {bus_id * wait_time}")
    assert bus_id * wait_time == 295
    # puzzle 2 examples
    wt = get_time(read_file(INPUT_FILE_TEST))
    print(f"(TEST) timestamp={wt}")
    assert wt == 1068781

    # puzzle1
    bus_id, wait_time = find_bus(read_file(INPUT_FILE))
    print(f"bus id: {bus_id}, wait time={wait_time}, product = {bus_id * wait_time}")

    # puzzle2
    wt = get_time(read_file(INPUT_FILE))
    print(f"timestamp={wt}")
