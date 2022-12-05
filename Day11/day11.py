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


def get_stable(_lines, _method, _tol):
    _iterations = 0
    _seat_map = []
    while not _seat_map == _lines:
        if _seat_map:
            _lines = _seat_map.copy()
        _seat_map = []
        _iterations = _iterations + 1
        for y, line in enumerate(_lines):
            _seat_map.append("")
            for x, pos in enumerate(line):
                if pos == "L":
                    _seat_map[y] = _seat_map[y] + (pos if _method(x, y, _lines).count("#") else "#")
                elif pos == "#":
                    _seat_map[y] = _seat_map[y] + (pos if _method(x, y, _lines).count("#") < _tol else "L")
                else:
                    _seat_map[y] = _seat_map[y] + pos
    return _iterations, sum(occ.count("#") for occ in _seat_map)


def get_occupancy(_x, _y, _lines):
    ret_val = []
    for y in [_y - 1, _y, _y + 1]:
        for x in [_x - 1, _x, _x + 1]:
            if 0 <= y < len(_lines) and 0 <= x < len(_lines[y]):
                if not (x == _x and y == _y):
                    ret_val.append(_lines[y][x])
    return ret_val


def get_occupancy2(_x, _y, _lines):
    ret_val = []
    ret_val2 = []
    for z in range(1, max(len(_lines), len(_lines[0]))):
        ret_val.append([])
        for y in [_y - z, _y, _y + z]:
            for x in [_x - z, _x, _x + z]:
                if 0 <= y < len(_lines) and 0 <= x < len(_lines[y]):
                    if not (x == _x and y == _y):
                        ret_val[z - 1].append(_lines[y][x])
                else:
                    ret_val[z - 1].append(".")

    for q in range(0, 8):
        sight = [vis[q] for vis in ret_val]
        ret_val2.append(next((x for x in sight if x is not None and x != "."), "."))

    return ret_val2


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    iterations, count = get_stable(read_file(INPUT_FILE_TEST), get_occupancy, 4)
    print(f"(TEST) iterations={iterations}, count={count}")
    assert iterations == 6 and count == 37
    # puzzle 2 examples
    iterations, count = get_stable(read_file(INPUT_FILE_TEST), get_occupancy2, 5)
    print(f"(TEST) iterations={iterations}, count={count}")

    # puzzle1
    iterations, count = get_stable(read_file(INPUT_FILE), get_occupancy, 4)
    print(f"iterations={iterations}, count={count}")

    # puzzle2
    iterations, count = get_stable(read_file(INPUT_FILE), get_occupancy2, 5)
    print(f"iterations={iterations}, count={count}")
