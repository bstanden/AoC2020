# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST1 = "input_test1.txt"
INPUT_FILE_TEST2 = "input_test2.txt"
INPUT_FILE_ALEX = "input_alex.txt"
INPUT_FILE = "input.txt"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [int(e.strip()) for e in lines]


def get_distribution(_lines):
    _lines.sort()
    _chain = [0]
    while len(_lines):
        _index = next((i for i, a in enumerate(_lines) if a - _chain[-1] <= 3))
        _chain.append(_lines.pop(_index))
    _chain.append(_chain[-1] + 3)
    return [[v - _chain[i] for i, v in enumerate(_chain[1:])].count(i) for i in range(1, 4)]


class ChainWalker:
    def __init__(self, _lines):
        self.lines = _lines
        self.lines.sort()
        self.lines.insert(0, 0)
        self.lines.append(self.lines[-1] + 3)
        self.counts = {}

    def walk(self, _o=0):
        forks = [i + 1 for i, a in enumerate(self.lines[_o + 1:_o + 4]) if a - self.lines[_o] <= 3]
        result = []
        if not forks:
            return 1
        for f in forks:
            if _o + f not in self.counts:
                self.counts[_o + f] = self.walk(_o + f)
            result.append(self.counts[_o + f])
        return sum(result)


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 examples
    distribution = get_distribution(read_file(INPUT_FILE_TEST1))
    print(f"(TEST 1a) distribution={distribution}")
    assert distribution == [7, 0, 5]

    distribution = get_distribution(read_file(INPUT_FILE_TEST2))
    print(f"(TEST 1b) distribution={distribution}")
    assert distribution == [22, 0, 10]

    # puzzle 2 examples
    count = ChainWalker(read_file(INPUT_FILE_TEST1)).walk()
    print(f"(TEST 2a) combs={count}")
    assert count == 8

    count = ChainWalker(read_file(INPUT_FILE_TEST2)).walk()
    print(f"(TEST 2b) combs={count}")
    assert count == 19208

    # puzzle1
    distribution = get_distribution(read_file(INPUT_FILE))
    print(f"distribution={distribution}; product={distribution[0] * distribution[2]}")

    # puzzle2
    # print(f"combs={ChainWalker(read_file(INPUT_FILE)).walk()}")
    print(f"combs={ChainWalker(read_file(INPUT_FILE_ALEX)).walk()}")
