Lab 2 Report: AST Printer

1. Expression Grammar and Design Choices
I designed this using the crafting interpreters textbook. 

Grammar Rules
```text
expression     → equality ;
equality       → comparison ( ( "!=" | "==" ) comparison )* ;
comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           → factor ( ( "-" | "+" ) factor )* ;
factor         → unary ( ( "/" | "*" ) unary )* ;
unary          → ( "!" | "-" ) unary
               | primary ;
primary        → NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")" ;

setup instructions:
 
1. Must have python installed. 
2. find the root directory and run "test/lab2/test_printer.py" 


Test cases and resutls: 
1. Verifying that the arithmetic with unary grouping worked 
 -Hard coded ast: binary(unary(-,123), *, Grouping(45.67))
 -expected output: (*(-123)(group 45.67))
 -actual output = matches

2. String literals and equality, verifying that it can handle string literals and comaprison
 -Hard coded: Binary("hello", ==, "world")
 - expected output: (== hello world)
 - actual output: Matches

3.booleans, nil, and unary logic, testing boolan literals, nil formatting and grouping
 -hard code: Binary(Unary(!, True), +, grouping(none))
 -expected: (+ (!, True) (group nil))
 -actual output: matched

Known limitations: 
- At the moment the printer depends on tokens having a lexeme` string that is ready to use. If a raw literal does not naturally turn into a string. If we add custom objects later the `visit_literal_expr` function will require more careful type-checking. Without this the output could become messy. 
