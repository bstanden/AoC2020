# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

from abc import ABC, abstractmethod

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE_TEST2 = "input_test2.txt"
INPUT_FILE_TEST3 = "input_test3.txt"
INPUT_FILE = "input.txt"
INPUT_FILE2 = "input2.txt"


class Parser:
    def __init__(self):
        self.ruleset = {}
        self.depth=[]

    def add_rule(self, line):
        rule_id, rules = line.split(":")
        rule_id = int(rule_id)
        if '"' in rules:
            self.ruleset[rule_id] = CharacterMatch(self, rules[2])  # character rule
        else:
            match_sequences = []
            for rule in rules.split("|"):
                ids = rule.lstrip().strip().split(" ")
                match_sequences.append([int(i) for i in ids])

            self.ruleset[rule_id] = SequentialMatch(self, match_sequences)

    def validate_message(self, message):
        #length= self.ruleset[0].is_match(message, 0)
        self.depth=[]
        length=self.validate_rule(message,0,0)
        return length == len(message)

    def validate_rule(self, message, rule, cursor):
        if (rule,cursor) in self.depth:
            return None
        else:
            self.depth.append((rule,cursor))
        match = self.ruleset[rule].is_match(message, cursor)
        self.depth.pop(-1)
        return match


class Match(ABC):
    def __init__(self, parser):
        self.parser = parser

    @abstractmethod
    def is_match(self, message, cursor):
        pass


class SequentialMatch(Match):
    def __init__(self, parser, match_sequences):
        super().__init__(parser)
        self.matchSequences = match_sequences

    def is_match(self, message, cursor):
        lcursor = cursor
        match = None
        for matchSequence in self.matchSequences:
            lcursor=cursor
            for rule_id in matchSequence:
                match = self.parser.validate_rule(message, rule_id, lcursor)
                if match:
                    lcursor = match
                else:
                    break

            if match:
                return lcursor
        return None


class CharacterMatch(Match):
    def __init__(self, parser, character):
        super().__init__(parser)
        self.character = character

    def is_match(self, message, cursor):
        if cursor >= len(message):
            return None
        if message[cursor] == self.character:
            return cursor + 1
        return None


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def parse_input(lines):
    p = Parser()
    m = []
    for line in lines:
        if ":" in line:
            p.add_rule(line)
        elif line != "":
            m.append(line)

    return p, m


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    _parser, _messages = parse_input(read_file(INPUT_FILE_TEST))
    _valid = sum([_parser.validate_message(m) for m in _messages])
    print(f"(TEST) There are {_valid} valid messages")
    assert _valid == 2

    # puzzle 2 examples
    _parser, _messages = parse_input(read_file(INPUT_FILE_TEST2))
    _valid = sum([_parser.validate_message(m) for m in _messages])
    print(f"(TEST) There are {_valid} valid messages")

    _parser, _messages = parse_input(read_file(INPUT_FILE_TEST3))
    _valid = sum([_parser.validate_message(m) for m in _messages])
    print(f"(TEST) There are {_valid} valid messages")
#    assert _valid == 3

    # puzzle1
    _parser, _messages = parse_input(read_file(INPUT_FILE))
    _valid = sum([_parser.validate_message(m) for m in _messages])
    print(f"There are {_valid} valid messages")

    # puzzle2
    _parser, _messages = parse_input(read_file(INPUT_FILE2))
    _valid = sum([_parser.validate_message(m) for m in _messages])
    print(f"There are {_valid} valid messages")
