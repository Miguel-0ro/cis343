# --- start AI code
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
    printer = AstPrinter()

    print("=== Running Lab 2 AST Printer Tests ===")

    expr1 = Binary(
        Unary(
            Token("MINUS", "-", None, 1),
            Literal(123)
        ),
        Token("STAR", "*", None, 1),
        Grouping(
            Literal(45.67)
        )
    )
    out1 = printer.print(expr1)
    print(f"Test 1 Output: {out1}")
    assert out1 == "(* (- 123) (group 45.67))", "Test 1 failed!"

    expr2 = Binary(
        Literal("hello"),
        Token("EQUAL_EQUAL", "==", None, 1),
        Literal("world")
    )
    out2 = printer.print(expr2)
    print(f"Test 2 Output: {out2}")
    assert out2 == "(== hello world)", "Test 2 failed!"

    expr3 = Binary(
        Unary(
            Token("BANG", "!", None, 1),
            Literal(True)
        ),
        Token("PLUS", "+", None, 1),
        Grouping(
            Literal(None)
        )
    )
    out3 = printer.print(expr3)
    print(f"Test 3 Output: {out3}")
    assert out3 == "(+ (! True) (group nil))", "Test 3 failed!"

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
# --- end AI code
#I will add, I did not only copy the code, I tried to understand it and modify it as needed.