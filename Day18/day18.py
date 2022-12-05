# AoC 2020
# Day n
#
# Dr Bob, Tech Team, DigitalUK

from abc import ABC, abstractmethod

INPUT_TEST = {
    "1 + 2 * 3 + 4 * 5 + 6": (71, 231),
    "1 + (2 * 3) + (4 * (5 + 6))": (51, 51),
    "2 * 3 + (4 * 5)": (26, 46),
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": (437, 1445),
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": (12240, 669060),
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": (13632, 23340)
}

INPUT_FILE = "input.txt"


class ExpressionError(Exception):
    pass


class ExpressionErrorExpectedCloseParenthesis(ExpressionError):
    pass


class ExpressionErrorExpectedOperator(ExpressionError):
    pass


class ExpressionErrorExpectedExpression(ExpressionError):
    pass


class ExpressionErrorSyntax(ExpressionError):
    pass


class Expression(ABC):
    def __init__(self, expr):
        self.expr = expr.replace("(", "( ").replace(")", " )").split(" ")

    @abstractmethod
    def eval(self, d=0):
        pass


class Expression1(Expression):
    def __init__(self, expr):
        super().__init__(expr)
        self.i = 0

    def eval(self, d=0):
        lvalue = op = rvalue = None
        while self.i < len(self.expr):
            if self.expr[self.i] == "":
                pass
            elif self.expr[self.i].isnumeric():
                if lvalue is None:
                    lvalue = int(self.expr[self.i])
                else:
                    if op is not None:
                        rvalue = int(self.expr[self.i])
                        lvalue = eval(f"{lvalue}{op}{rvalue}")
                        rvalue = op = None
                    else:
                        raise ExpressionErrorExpectedOperator
            elif self.expr[self.i] in "+*":
                if lvalue is not None:
                    if op is None:
                        op = self.expr[self.i]
                    else:
                        raise ExpressionErrorExpectedExpression
                else:
                    raise ExpressionErrorExpectedExpression

            elif self.expr[self.i] == "(":
                if lvalue is None:
                    self.i = self.i + 1
                    lvalue = self.eval(d + 1)
                else:
                    if op is not None:
                        self.i = self.i + 1
                        rvalue = self.eval(d + 1)
                        lvalue = eval(f"{lvalue}{op}{rvalue}")
                        op = rvalue = None
                    else:
                        raise ExpressionErrorExpectedOperator
            elif self.expr[self.i] == ")":
                # self.i = self.i + 1
                return lvalue
                pass
            else:
                raise ExpressionErrorSyntax
            self.i = self.i + 1

        if d != 0:
            raise ExpressionErrorExpectedCloseParenthesis

        if op is not None:
            raise ExpressionErrorExpectedExpression
        else:
            return lvalue


class MyNumber:  # define a number class in which addition and multiplication are transposed
    def __init__(self, val):
        self.val = val

    def __add__(self, other):  # really do multiply here :)
        return MyNumber(self.val * other.val)

    def __mul__(self, other):  # really do add here :)
        return MyNumber(self.val + other.val)


class Expression2(Expression):
    def __init__(self, expr):
        super().__init__(expr)
        for i, e in enumerate(self.expr):
            if e.isnumeric():
                self.expr[i] = f"MyNumber({e})"
            elif e == "*":
                self.expr[i] = "+"  # by swapping addition and multiplication, we can use eval() directly.
            elif e == "+":
                self.expr[i] = "*"

    def eval(self, d=0):
        return eval("".join(self.expr)).val


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    for _expr, (_result1, _result2) in INPUT_TEST.items():
        _calc1 = Expression1(_expr).eval()
        _calc2 = Expression2(_expr).eval()
        print(f"(TEST) {_expr} = (1) {_calc1}; (2) {_calc2}")
        assert _calc1 == _result1 and _calc2 == _result2
    # puzzle 2 examples
    pass

    # puzzle1
    _sum = sum(Expression1(_line).eval() for _line in read_file(INPUT_FILE))
    print(f"sum1 is {_sum}")

    # puzzle2
    _sum = sum(Expression2(_line).eval() for _line in read_file(INPUT_FILE))
    print(f"sum2 is {_sum}")
