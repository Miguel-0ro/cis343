from expr_ast import Binary, Grouping, Literal, Unary
from scanner import TokenType


class ParseError(Exception):
    def __init__(self, token, message):
        super().__init__(message)
        self.token = token
        self.message = message

    def __str__(self):
        where = "at end" if self.token.token_type == TokenType.EOF \
            else f"at '{self.token.lexeme}'"
        return f"[line {self.token.line_num}] Error {where}: {self.message}"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []

    def parse(self):
        try:
            expr = self.expression()
            if not self.is_at_end():
                raise ParseError(self.peek(), "Unexpected token after expression.")
            return expr
        except ParseError as e:
            self.errors.append(e)
            return None

    def expression(self):
        return self.equality()

    def equality(self):
        return self._binary(self.comparison,
                            TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL)

    def comparison(self):
        return self._binary(self.term, TokenType.GREATER, TokenType.GREATER_EQUAL,
                            TokenType.LESS, TokenType.LESS_EQUAL)

    def term(self):
        return self._binary(self.factor, TokenType.MINUS, TokenType.PLUS)

    def factor(self):
        return self._binary(self.unary, TokenType.SLASH, TokenType.STAR)

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            return Unary(operator, self.unary())
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().value)
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        if self.check(TokenType.RIGHT_PAREN):
            raise ParseError(self.peek(), "Unmatched ')'.")
        raise ParseError(self.peek(), "Expect expression.")

    def _binary(self, next_level, *types):
        expr = next_level()
        while self.match(*types):
            operator = self.previous()
            right = next_level()
            expr = Binary(expr, operator, right)
        return expr

    def match(self, *types):
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def consume(self, type_, message):
        if self.check(type_):
            return self.advance()
        raise ParseError(self.peek(), message)

    def check(self, type_):
        return not self.is_at_end() and self.peek().token_type == type_

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().token_type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]
