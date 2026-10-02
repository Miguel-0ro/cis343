The name I elected to give my language is "migo" (just the first three letters of my name + first letter of my last name)

the regex for my num literals are as follow: [0-9]+([0=9]+)?
the regex for my string literals are as follow: \text{"[textasciicirc5f}\"]*"}
the regex for my identifiers are as follow: [a-zA-Z_][a-zA-z0-9]*

In terms of my design choice, I followed the guide from the textbook mostly. This included items such as not having to declare variable types, being class based, and it has automatic memory management.

In order to properly test the scanner, you would need to follow these steps: 
1. you have Python3.x installed and accessible.
2. clone or download the repository on to your machine. 
3. open a terminal (powershell) and find the directory
4. for source file mode, pass any file as an arguement, e.g: python src/main.py pathToTest/test_file.lox
5. for the interactive mode (typing within the terminal), you would simply need to run python src/main.py within the directory of the project.

I did two main test cases, one was through the interactive mode and the other was by passing a file. 
The purpose was to see if both worked on the scanner and if the scanner could take both as input. This test succeeded. Both of the token amounts were correct (at least to my count). Both results matched what was expected. 

No known limitations thus far, though I will say that I have not extensively tested this scanner with more complicated input. There may be some limitations once the input is complicated enough.


known limitations or failing tests