# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_TEST = [0, 3, 6]
INPUT = [0, 1, 4, 13, 15, 12, 16]


def get_number(input, iterations):
    history = {}
    for n, i in enumerate(input):
        history[i] = [n + 1]

    last_num = input[-1]
    turn = len(input) + 1

    while (turn <= iterations):
        last_time = history.get(last_num)
        if last_time:
            if len(last_time) > 1:
                last_num = last_time[-1] - last_time[-2]
                if last_num in history:
                    history[last_num].append(turn)
                else:
                    history[last_num] = [turn]
            else:
                last_num = 0
                history[last_num].append(turn)
        else:
            last_num = 0
            history[last_num].append(turn)

        turn = turn + 1

    return last_num


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    _num = get_number(INPUT_TEST, 2020)
    print(F"(TEST) num={_num}")
    assert _num == 436

    # puzzle 2 examples

    # puzzle1
    _num = get_number(INPUT, 2020)
    print(F"num={_num}")
    # puzzle2
    _num = get_number(INPUT, 30000000)
    print(F"num={_num}")
