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


class Navigator:
    def __init__(self, _x=0, _y=0):
        self.start_x = _x
        self.start_y = _y
        self.reset()
        self.hdg = 1
        self.pos_x = self.start_x
        self.pos_y = self.start_y

    def reset(self):
        self.hdg = 1
        self.pos_x = self.start_x
        self.pos_y = self.start_y

    def run(self, _lines):
        for line in _lines:
            self.exec(line)

        return self.manhattan()

    def exec(self, _line):
        i, m = _line[0], int(_line[1:])
        if i in "NESW":
            self.advance("NESW".index(i), m)
        elif i == "L":
            self.hdg = (self.hdg - (m / 90)) % 4
        elif i == "R":
            self.hdg = (self.hdg + (m / 90)) % 4
        elif i == "F":
            self.advance(self.hdg, m)
        else:
            pass

    def advance(self, _i, _m):
        if _i == 0:
            self.pos_y = self.pos_y + _m
        elif _i == 1:
            self.pos_x = self.pos_x + _m
        elif _i == 2:
            self.pos_y = self.pos_y - _m
        elif _i == 3:
            self.pos_x = self.pos_x - _m

    def manhattan(self):
        return abs(self.pos_x - self.start_x) + abs(self.pos_y - self.start_y)


class Navigator2(Navigator):
    def __init__(self, _wx=0, _wy=0, _x=0, _y=0):
        super().__init__(_x, _y)
        self.wx = _wx
        self.wy = _wy

    def exec(self, _line):
        i, m = _line[0], int(_line[1:])
        if i in "NESW":
            self.wadvance(i, m)
        elif i == "L":
            self.wrotate(int(-m / 90))
        elif i == "R":
            self.wrotate(int(m / 90))
        elif i == "F":
            self.approach(m)
        else:
            pass

    def wadvance(self, _i, _m):
        if _i == "N":
            self.wy = self.wy + _m
        elif _i == "E":
            self.wx = self.wx + _m
        elif _i == "S":
            self.wy = self.wy - _m
        elif _i == "W":
            self.wx = self.wx - _m

    def wrotate(self, _i):
        for n in range(0, abs(_i)):
            if _i > 0:
                self.wx, self.wy = self.wy, -self.wx
            else:
                self.wx, self.wy = -self.wy, self.wx

    def approach(self, m):
        for n in range(0, m):
            self.pos_x = self.pos_x + self.wx
            self.pos_y = self.pos_y + self.wy
        pass


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    nav = Navigator()
    dist = nav.run(read_file(INPUT_FILE_TEST))
    print(f"(TEST) dist={dist}")
    assert dist == 25
    # puzzle 2 examples
    nav = Navigator2(10, 1)
    dist = nav.run(read_file(INPUT_FILE_TEST))
    print(f"(TEST) dist={dist}")
    assert dist == 286

    # puzzle1
    nav = Navigator()
    dist = nav.run(read_file(INPUT_FILE))
    print(f"dist={dist}")
    # puzzle2
    nav = Navigator2(10, 1)
    dist = nav.run(read_file(INPUT_FILE))
    print(f"dist={dist}")
