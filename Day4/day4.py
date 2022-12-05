# AoC 2020
# Day 4
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_VALID = "input_valid.txt"
INPUT_INVALID = "input_invalid.txt"
INPUT_FILE = "input.txt"


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


def get_passports(_lines):
    passports = []
    passport = {}
    for line in _lines:
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            for field in line.split(' '):
                (k, v) = field.split(":")
                passport[k] = v
    passports.append(passport)
    return passports


def count_valid(_filename, _extended=False):
    count = 0
    lines = read_file(_filename)
    for passport in get_passports(lines):
        if all(field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
            count = count + (1 if not _extended else 1 if extended_validation(passport) else 0)

    return count


def extended_validation(_passport):
    return (
            validate_byr(_passport['byr'])
            and validate_iyr(_passport['iyr'])
            and validate_eyr(_passport['eyr'])
            and validate_hgt(_passport['hgt'])
            and validate_hcl(_passport['hcl'])
            and validate_ecl(_passport['ecl'])
            and validate_pid(_passport['pid'])
    )


def validate_byr(_s):
    year = int(_s)
    return 1920 <= year <= 2002


def validate_iyr(_s):
    year = int(_s)
    return 2010 <= year <= 2020


def validate_eyr(_s):
    year = int(_s)
    return 2020 <= year <= 2030


def validate_hgt(_s):
    if 4 <= len(_s) <= 5:
        hgt = int(_s[:-2])
        units = _s[-2:]

        if units == "cm":
            return 150 <= hgt <= 193
        elif units == "in":
            return 59 <= hgt <= 76

    return False


def validate_hcl(_s):
    return set(_s[1:]) <= set("0123456789abcdef") if len(_s) == 7 and _s[0] == '#' else False


def validate_ecl(_s):
    return _s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(_s):
    return set(_s) <= set("0123456789") if len(_s) == 9 else False


# check we're being run directly
if __name__ == '__main__':

    # assertions against known, worked examples
    # puzzle 1 example
    assert count_valid(INPUT_FILE_TEST) == 2
    # puzzle 2 examples
    assert count_valid(INPUT_INVALID, True) == 0
    assert count_valid(INPUT_VALID, True) == 4

    # puzzle1
    valid_count = count_valid(INPUT_FILE)
    print(f"number of valid passports is {valid_count}")

    # puzzle2
    valid_count = count_valid(INPUT_FILE, True)
    print(f"number of valid passports is {valid_count}")
