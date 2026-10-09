# --- start AI code ----
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from expr_ast import Binary, Unary, Literal, Grouping
from printer import AstPrinter

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

def run_tests():
    expression = Binary(
        Unary(
            Token("MINUS", "-", None, 1),
            Literal(123)
        ),
        Token("STAR", "*", None, 1),
        Grouping(
            Literal(45.67)
        )
    )

    printer = AstPrinter()
    result = printer.print(expression)
    print("Test Output:", result)

if __name__ == "__main__":
    run_tests()
#--- end AI code ---