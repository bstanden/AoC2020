# AoC 2020
# Day 1
#
# Dr Bob, Tech Team, DigitalUK

SUM_TO_FIND = 2020
INPUT_FILE = "input.txt"


# slurp file into a list of numbers
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [int(e.strip()) for e in lines]


# recursive function to search an increasingly shorter list for items that sum to a given value (option 3rd param)
def find_sum(_numbers, _s, _c=None):
    if len(_numbers) > 0:
        _a = _numbers.pop()  # remove first item from list...
        sums = [_a + n + (_c if _c else 0) for n in _numbers]  # ...and find its sum with each remaining list element
        try:
            return _a, _numbers[sums.index(_s)]  # Return corresponding index in numbers if s found in sums
        except ValueError:
            return find_sum(_numbers, _s, _c)  # call recursively if s not found in sums
    else:
        return None, None  # list is exhausted.


# harness for puzzle 1.
def do_puzzle1(_filename, _s):
    print(f'searching {_filename} for two items that sum to {_s}')
    numbers = read_file(_filename)

    return find_sum(numbers, _s)


# harness for puzzle2
def do_puzzle2(_filename, _s):
    print(f'searching {_filename} for three items that sum to {_s}')
    numbers = read_file(_filename)

    _a = _b = _c = None

    while numbers:
        _c = numbers.pop()  # take each item from list in turn...
        _a, _b = find_sum(numbers.copy(), _s, _c)  # ... call find_sum, offsetting by the value taken from list
        if _a is not None:
            break

    return _a, _b, _c


# check we're being run directly
if __name__ == '__main__':
    a, b = do_puzzle1(INPUT_FILE, SUM_TO_FIND)
    if None not in (a, b):
        print(f"Found: a={a}, b={b}; product={a * b}")
    else:
        print( f"Not found :(")

    a, b, c = do_puzzle2(INPUT_FILE, SUM_TO_FIND)
    if None not in (a, b, c):
        print(f"Found: a={a}, b={b}, c={c}; product={a * b * c}")
    else:
        print( f"Not found :(")