# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"


class Manifest:
    def __init__(self, lines=None):
        self.rules = {}
        self.tickets = []
        if lines:
            self.parse(lines)
        pass

    def parse(self, lines):
        for line in lines:
            if "-" in line:
                name, limits = line.split(":")
                q = limits.split(" ")
                a_min, a_max = q[1].split("-")
                b_min, b_max = q[3].split("-")
                self.rules[name] = {"lim": [int(a_min), int(a_max), int(b_min), int(b_max)]}
            elif "," in line:
                self.tickets.append([int(x) for x in line.split(",")])

    def error_rate(self):
        return sum([self.ticket_error(t) for t in self.tickets[1:]])

    def ticket_error(self, t):
        for x in t:
            if not any(
                    [(r["lim"][0] <= x <= r["lim"][1]) or (r["lim"][2] <= x <= r["lim"][3]) for r
                     in self.rules.values()]):
                return x
        return 0

    def prune(self):
        self.tickets = [t for t in self.tickets if not self.ticket_error(t)]

    def departure_sum(self):
        fields = [list(row) for row in zip(*reversed(self.tickets[1:]))]
        matches = []
        for i, f in enumerate(fields):
            for name, rule in self.rules.items():
                if all([(rule["lim"][0] <= x <= rule["lim"][1]) or (rule["lim"][2] <= x <= rule["lim"][3])
                        for x in f]):
                    matches.append([name, i])

        for _ in self.tickets[0]:
            for name, rule in self.rules.items():
                rule_match = [m for m in matches if
                              m[0] == name and m[1] not in [r.get("field") for r in self.rules.values()]]
                if len(rule_match) == 1:
                    self.rules[rule_match[0][0]]["field"] = rule_match[0][1]
        ret_val = 1
        for k, v in self.rules.items():
            if "departure" in k:
                ret_val = ret_val * (self.tickets[0][v["field"]])

        return ret_val


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    _manifest = Manifest(read_file(INPUT_FILE_TEST))
    _error_rate = _manifest.error_rate()
    print(f"(TEST) error rate = {_error_rate}")
    assert _error_rate == 71

    # puzzle 2 examples
    pass  # no example for puzzle 2

    # puzzle1
    _manifest = Manifest(read_file(INPUT_FILE))
    _error_rate = _manifest.error_rate()
    print(f"error rate = {_error_rate}")

    # puzzle2
    _manifest.prune()
    _departure_sum = _manifest.departure_sum()
    print(f"departure sum = {_departure_sum}")
