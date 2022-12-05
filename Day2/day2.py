# AoC 2020
# Day 2
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE = "input.txt"


# slurp file into a list of strings
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# Validate passwords in each line for the form "a-b c:<password>" where  c must appear between a and b times
def do_puzzle1(filename):
    lines = read_file(filename)
    count = 0
    for line in lines:
        bounds, character, password = line.split(" ")  # NB character is a string that includes ":"; use character[0]
        occ_min, occ_max = (int(x) for x in bounds.split("-"))
        if password.count(character[0]) in range(occ_min, occ_max + 1):  # python range() does not include upper value
            count = count + 1

    return count


# Validate passwords in each line for the form "a-b c:<password>" where c must appear at position a or b, but not both
def do_puzzle2(filename):
    lines = read_file(filename)
    count = 0
    for line in lines:
        bounds, character, password = line.split(" ")  # NB character is a string that includes ":"; use character[0]
        a, b = (int(x) - 1 for x in bounds.split("-"))  # a and b are 1-based; python is not
        if (password[a] == character[0]) ^ (password[b] == character[0]):
            count = count + 1

    return count


# check we're being run directly
if __name__ == '__main__':
    valid_count = do_puzzle1(INPUT_FILE)
    print(f"There are {valid_count} valid passwords in puzzle 1")

    valid_count = do_puzzle2(INPUT_FILE)
    print(f"There are {valid_count} valid passwords in puzzle 2")
