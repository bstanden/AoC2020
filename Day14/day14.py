# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK
from abc import ABC, abstractmethod

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE_TEST2 = "input_test2.txt"
INPUT_FILE = "input.txt"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def get_mask_value(mask_str, mask_key):
    return int("".join([mask_key if c == "X" else c for c in mask_str]), 2)


class DockingMemory(ABC):
    def __init__(self):
        self.or_mask = 0
        self.memory = {}

    @abstractmethod
    def write_memory(self, loc, v):
        pass

    def parse_input(self, lines):
        for line in lines:
            loc_str, val_str = line.split("=")
            if "[" in loc_str:
                self.write_memory(int(loc_str[4:-2]), int(val_str))
            else:
                self.parse_mask(val_str)

        return sum(self.memory.values())

    def parse_mask(self, val_str):
        self.or_mask = get_mask_value(val_str, "0")


class DockingMemoryV1(DockingMemory):
    def __init__(self):
        super().__init__()
        self.and_mask = 0

    def write_memory(self, loc, v):
        v = (v & self.and_mask) | self.or_mask
        self.memory[loc] = v

    def parse_mask(self, val_str):
        super().parse_mask(val_str)
        self.and_mask = get_mask_value(val_str, "1")


class DockingMemoryV2(DockingMemory):
    def __init__(self):
        super().__init__()
        self.float_bits = []

    def parse_mask(self, val_str):
        super().parse_mask(val_str)
        self.float_bits = [len(val_str) - i - 1 for i, v in enumerate(val_str) if v == "X"]

    def write_memory(self, loc, v):
        loc = (loc | self.or_mask)
        for i in range(0, 2 ** len(self.float_bits)):
            write_loc = loc
            for j in range(0, len(self.float_bits)):
                mask = 1 << self.float_bits[j]
                write_loc = write_loc & ~mask
                if i & (1 << j):
                    write_loc = write_loc | mask
            self.memory[write_loc] = v


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    _mem = DockingMemoryV1()
    _sum = _mem.parse_input(read_file(INPUT_FILE_TEST))
    print(f"(TEST) sum is {_sum}")
    assert _sum == 165

    # puzzle 2 example
    _mem = DockingMemoryV2()
    _sum = _mem.parse_input(read_file(INPUT_FILE_TEST2))
    print(f"(TEST) sum is {_sum}")
    assert _sum == 208

    # puzzle1
    _mem = DockingMemoryV1()
    _sum = _mem.parse_input(read_file(INPUT_FILE))
    print(f"sum is {_sum}")

    # puzzle2
    _mem = DockingMemoryV2()
    _sum = _mem.parse_input(read_file(INPUT_FILE))
    print(f"sum is {_sum}")
