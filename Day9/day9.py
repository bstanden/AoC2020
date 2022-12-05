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
    return [int(e.strip()) for e in lines]


def get_invalid(_lines, _w_size):
    window = []
    while len(window) < _w_size:
        window.append(_lines.pop(0))

    for _x in _lines:
        if not valid(_x, window):
            return _x
        else:
            window.pop(0)
            window.append(_x)
    return None


def valid(_x, _window):
    for i in range(0, len(_window) - 1):
        for j in range(i + 1, len(_window)):
            if _window[i] + _window[j] == _x:
                return True
    return False


def get_weakness(_num, _lines):
    _sum = 0
    for i, _x in enumerate(_lines):
        _sum = _sum + _x
        if _sum == _num:
            return min(_lines[:i]), max(_lines[:i])
        elif _sum > _num:
            return get_weakness(_num, _lines[1:])
    return None, None, None


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    num = get_invalid(read_file(INPUT_FILE_TEST), 5)
    print(f"(TEST) Invalid number = {num}")
    assert num == 127
    # puzzle 2 examples
    x, y = get_weakness(num, read_file(INPUT_FILE_TEST))
    print(f"(TEST) Encryption Weakness: x={x}, y={y}, weakness={x + y}")
    assert x + y == 62

    # puzzle1
    num = get_invalid(read_file(INPUT_FILE), 25)
    print(f"Invalid number = {num}")

    # puzzle2
    x, y = get_weakness(num, read_file(INPUT_FILE))
    print(f"Encryption Weakness: x={x}, y={y}, weakness={x + y}")
