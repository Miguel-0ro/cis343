from enum import Enum, auto

class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    #forogot these
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()

    EOF = auto()

class Token:
    def __init__(self, token_type, lexeme, value, line_num):
        self.token_type = token_type
        self.lexeme = lexeme
        self.value = value
        self.line_num = line_num

    def __repr__(self):
        return f"Token({self.token_type}, {repr(self.lexeme)}, {repr(self.value)})"
    
    
    

class Scanner:
    KEYWORDS = {
        'and': TokenType.AND,
        'class': TokenType.CLASS,
        'else': TokenType.ELSE,
        'false': TokenType.FALSE,
        'for': TokenType.FOR,
        'fun': TokenType.FUN,
        'if': TokenType.IF,
        'nil': TokenType.NIL,
        'or': TokenType.OR,
        'print': TokenType.PRINT,
        'return': TokenType.RETURN,
        'super': TokenType.SUPER,
        'this': TokenType.THIS,
        'true': TokenType.TRUE,
        'var': TokenType.VAR,
        'while': TokenType.WHILE,
    }

    def __init__(self, source):
        self.source = source 
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while self.current < len(self.source):
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
    
        #token map
        tokens_map = {
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            ',': TokenType.COMMA,
            '.': TokenType.DOT,
            '-': TokenType.MINUS,
            '+': TokenType.PLUS,
            ';': TokenType.SEMICOLON,
            '*': TokenType.STAR,
    }

        if c in tokens_map:
            self.tokens.append(Token(tokens_map[c], c, None, self.line))

        #if new line 
        elif c == '\n':
            self.line += 1

        #check for bang 
        #START AI CODE//
        elif c == '!':
            if self.peek() == '=':
                self.advance()
                self.tokens.append(Token(TokenType.BANG_EQUAL, "!=", None, self.line))
            else:
                self.tokens.append(Token(TokenType.BANG, "!", None, self.line))
        # END AI CODE// 

        #check for less than 
        elif c == '<':
            if self.peek() == '=':
                self.advance()
                self.tokens.append(Token(TokenType.LESS_EQUAL, "<=", None, self.line))
            else:
                self.tokens.append(Token(TokenType.LESS, "<", None, self.line))

        #check for greater than 
        elif c == '>':
            if self.peek() == '=':
                self.advance()
                self.tokens.append(Token(TokenType.GREATER_EQUAL, ">=", None, self.line))
            else:
                self.tokens.append(Token(TokenType.GREATER, ">", None, self.line))

        #check for =        
        elif c == '=':
            if self.peek() == '=':
                self.advance()
                self.tokens.append(Token(TokenType.EQUAL_EQUAL, "==", None, self.line))
            else:
                self.tokens.append(Token(TokenType.EQUAL, "=", None, self.line))

        # check for SLASH
        elif c == '/':
            if self.peek() == '/':
                while self.peek() != '\n' and self.current < len(self.source):
                    self.advance()
            else:
                self.tokens.append(Token(TokenType.SLASH, "/", None, self.line))

        #check for empty spaces 
        elif c == ' ' or c == '\r' or c == '\t':
            pass

        #checking for string literals     
        elif c == '"':
            while self.peek() != '"' and self.current < len(self.source):
                if self.peek() == '\n':
                    self.line += 1
                self.advance()

            if self.current >= len(self.source):
                print(f"[Line {self.line}] Error: Weird String")
                return

            self.advance()

            value = self.source[self.start + 1: self.current - 1]
            self.tokens.append(Token(TokenType.STRING, value, value, self.line))

        #checl for nums 
        elif c.isdigit():
            # Consume all preceding integer digits
            while self.peek().isdigit() and self.current < len(self.source):
                self.advance()

            if self.peek() == '.' and self.source[self.current + 1].isdigit():
                self.advance()
        
            while self.peek().isdigit() and self.current < len(self.source):
                self.advance()

            lexeme = self.source[self.start : self.current]
            value = float(lexeme) if '.' in lexeme else int(lexeme)
            self.tokens.append(Token(TokenType.NUMBER, lexeme, value, self.line))

        #checks for keywords
        elif c.isalpha() or c == '_':
            while self.peek().isalnum() or self.peek() == '_':
                self.advance()

            text = self.source[self.start : self.current]
            token_type = self.KEYWORDS.get(text, TokenType.IDENTIFIER)
            self.tokens.append(Token(token_type, text, None, self.line))

        #incase char isnt recognized 
        else:
            print(f"[Line {self.line}] Error: Character Uknown: {c}")


        

    def advance(self):
        char = self.source[self.current]
        self.current += 1
        return char

    def peek(self):
        if self.current >= len(self.source):
            return "O"
        return self.source[self.current]

    
    