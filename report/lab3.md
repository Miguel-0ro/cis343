
**Level of precedence: 
expression → equality
equality   → comparison ( ( "!=" | "==" ) comparison )*
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )*
term       → factor ( ( "-" | "+" ) factor )*
factor     → unary ( ( "/" | "*" ) unary )*
unary      → ( "!" | "-" ) unary | primary
primary    → NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")"

precedence and associativity: 
equality, comparison, term and factor: left
Unary : right 
Primary: n/a 


Design Choices: 
Expression grammar is the same as the lox textbook. It supports number, string, true, false, and nil literals, the four operators, unary - and !, equality, comparison, and grouping. 

and/or are not parsed. Identifiers, assignment, and statements are also not a parsed. 
Parse() returns None on a syntax error. 
Errors are collected as strings or ParseError objects and retuend to main. 
The AST printer prints booleans as true/false and None as nil. 

I had to change a couple of methods within both main and Scanner to allow the parser to work. 
The scanner also now records errors in a list instead of printing them out. peek returns "\0" at the end of input and the number scanner checks bounds before looking past a period. 

Setup and running: 
1. Have Python installed 
2. run the rpo from its root: python src/main.py 
OR source file : python src/main.py path/to/fle.txt
OR python test/lab3/parser_test.py 

test cases: 
31/31 test cases passed. Although, I did have trouble with a couple, in specific, I had trouble with testing the file mode. 
The entire list is a bit comprehensive, I recommend checking the parser test file so I do not have to relist them. 
The purpose of each test was to ensure that each type was able to be parsed. Some include each type of all of the operands (<,>, +, =, -, / etc.) Unary, left associativity grouping, nested groups, true/false/nil/number/string literals, precedence etc. 

Syntax and lexical errors: 
unmatched () - leaving one out of the paranthesis. This output was as expected and gave an error since it was not closed out. 
Missing operands: also passed since. It was not able to find either left or right and so, it gave an error. 
Unexpected Token: when adding a seperate operand (1 +* 3), the error was raised correctly.

Known limitations:

1. Scanner errors get collected but the error stops the pipeline before parsing. 

2. None of the tests failed, one did fail at first but I was referencing the wrong file. After fixing this, I was able correctly get the expected output. 

3. and/or are not parsed in this lab. Using them raises an "Expect expressio" or "unexpected token" error. 

4. NUM ')' returns unexpected token rather than unmatched because the number appears after a whole expression. 

** I did use some Ai in this lab, reason being I had some trouble understanding what I was doing conceptually and how to put it into code**