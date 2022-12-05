# AoC 2020
# Day 8
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"


class CPUErrorUnknownInstruction(Exception):
    def __init__(self, _i):
        self.i = _i


class CPUErrorInfiniteLoop(Exception):
    def __init__(self, _pc, _acc):
        self.pc, self.acc = _pc, _acc


class CPUErrorProgramExhausted(Exception):
    pass


class CPU:  # CPU with software interrupts for loop detection & program end, and debug code insertion at breakpoints :)
    def __init__(self, _code):
        self.code = _code
        self.acc = 0
        self.pc = 0

    def debug(self, _int_complete=None, _int_loop=None):
        debug_instr = ["jmp", "nop"]

        def debug_code(_i):
            return debug_instr[0] if _i == debug_instr[1] else debug_instr[1] if _i == debug_instr[0] else _i

        for b in [pc for pc, i in enumerate(self.code) if i.split(" ")[0] in debug_instr]:
            try:
                self.run(_int_complete, _int_loop, b, debug_code)  # try injecting debug code at each breakpoint
            except CPUErrorInfiniteLoop:  # handle infinite loop by running again with next breakpoint
                pass

    def run(self, _int_complete=None, _int_loop=None, _breakpoint=None, _debug_code=None):
        history = []
        self.acc = 0
        self.pc = 0
        while self.pc < len(self.code):
            if self.pc in history:
                if _int_loop:
                    _int_loop(self.pc, self.acc)
                    return
                else:
                    raise CPUErrorInfiniteLoop(self.pc, self.acc)
            history.append(self.pc)
            self.exec(_breakpoint, _debug_code)
        if not _int_complete:
            raise CPUErrorProgramExhausted
        _int_complete(self.acc)

    def exec(self, _breakpoint, _debug_code):
        i, op = self.code[self.pc].split(" ")
        if self.pc == _breakpoint:
            i = _debug_code(i)

        if i == "acc":
            self.acc = self.acc + int(op)
        elif i == "jmp":
            self.pc = self.pc + int(op) - 1  # auto increment of PC below
        elif i == "nop":
            pass
        else:
            raise CPUErrorUnknownInstruction(i)
        self.pc = self.pc + 1


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as _f:
        _lines = _f.readlines()
    return [_line.strip() for _line in _lines]


def int_complete(_acc, _test=None):  # software interrupt handler for program completion
    print(f"{'(TEST) ' if _test else ''}Program complete, acc={_acc}")
    if _test:
        assert _acc == _test


def int_loop(_pc, _acc, _test=None):  # software interrupt handler for infinite loop detection
    print(f"{'(TEST) ' if _test else ''}Infinite loop, pc={_pc}, acc={_acc}")
    if _test:
        assert _acc == _test


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    cpu = CPU(read_file(INPUT_FILE_TEST))
    cpu.run(None, lambda pc, acc: int_loop(pc, acc, 5))  # use lambda to insert option assertion value

    # puzzle 2 example
    cpu.debug(lambda acc: int_complete(acc, 8), None)  # use lambda to insert option assertion value

    # puzzle1
    cpu = CPU(read_file(INPUT_FILE))
    cpu.run(None, int_loop)

    # puzzle2
    cpu.debug(int_complete, None)
