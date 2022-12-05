# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

from abc import ABC, abstractmethod


class EnergySource(ABC):
    def __init__(self, lines=None):
        self.cells = []
        if lines:
            self.read_lines(lines)

    @abstractmethod
    def read_lines(lines):
        pass

    def power_up(self):
        for x in range(0, 6):
            self.cycle()
        return len(self.cells)

    @abstractmethod
    def cycle(self):
        pass


class EnergySource3D(EnergySource):
    def __init__(self, lines=None):
        super().__init__(lines)

    def read_lines(self, lines):
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == "#":
                    self.cells.append((x, y, 0))

    def cycle(self):
        state = {}
        for (x, y, z) in self.cells:
            for _x in (-1, 0, 1):
                for _y in (-1, 0, 1):
                    for _z in (-1, 0, 1):
                        if (x + _x, y + _y, z + _z) not in state:
                            state[(x + _x, y + _y, z + _z)] = self.consider(x + _x, y + _y, z + _z)

        self.cells = [x for x in state if state[x]]

    def consider(self, x, y, z):
        active_count = 0
        for _x in (-1, 0, 1):
            for _y in (-1, 0, 1):
                for _z in (-1, 0, 1):
                    if (_x, _y, _z) != (0, 0, 0):
                        if (x + _x, y + _y, z + _z) in self.cells:
                            active_count = active_count + 1

        if (x, y, z) in self.cells:
            if active_count == 2 or active_count == 3:
                return True
            else:
                return False
        elif (x, y, z) not in self.cells and active_count == 3:
            return True

        return False


class EnergySource4D(EnergySource):
    def __init__(self, lines=None):
        super().__init__(lines)

    def read_lines(self, lines):
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == "#":
                    self.cells.append((x, y, 0, 0))

    def cycle(self):
        state = {}
        for (x, y, z, w) in self.cells:
            for _x in (-1, 0, 1):
                for _y in (-1, 0, 1):
                    for _z in (-1, 0, 1):
                        for _w in (-1, 0, 1):
                            if (x + _x, y + _y, z + _z, w + _w) not in state:
                                state[(x + _x, y + _y, z + _z, w + _w)] = self.consider(x + _x, y + _y, z + _z, w + _w)

        self.cells = [x for x in state if state[x]]

    def consider(self, x, y, z, w):
        active_count = 0
        for _x in (-1, 0, 1):
            for _y in (-1, 0, 1):
                for _z in (-1, 0, 1):
                    for _w in (-1, 0, 1):
                        if (_x, _y, _z, _w) != (0, 0, 0, 0):
                            if (x + _x, y + _y, z + _z, w + _w) in self.cells:
                                active_count = active_count + 1

        if (x, y, z, w) in self.cells:
            if active_count == 2 or active_count == 3:
                return True
            else:
                return False
        elif (x, y, z, w) not in self.cells and active_count == 3:
            return True

        return False


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    _es = EnergySource3D(read_file(INPUT_FILE_TEST))
    _active = _es.power_up()
    print(f"(TEST) active cells={_active}")
    assert _active == 112

    # puzzle 2 examples
    _es = EnergySource4D(read_file(INPUT_FILE_TEST))
    _active = _es.power_up()
    print(f"(TEST) active cells={_active}")
    assert _active == 848
    # puzzle1
    _es = EnergySource3D(read_file(INPUT_FILE))
    _active = _es.power_up()
    print(f"active cells={_active}")

    # puzzle2
    _es = EnergySource4D(read_file(INPUT_FILE))
    _active = _es.power_up()
    print(f"active cells={_active}")
