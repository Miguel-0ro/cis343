# --- start AI code ---
from scanner import Scanner
from printer import AstPrinter
import sys
from pparser import Parser

def main():
    #---Start AI code---
    if len(sys.argv) > 2:
        print("Usage: python main.py [script]")
        sys.exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])

    else:
        run_prompt()
    #---End AI code--- (never used sys before)


def run_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()
    output, ok = run(source)
    print(output)
    #---Start AI code---
    if not ok:
        sys.exit(65)
    #--End AI code--- (never used sys before)

def run_prompt():
    while True:
        try:
            line = input("> ")
            if line == "":
                break
            output, _ = run(line)   
            print(output)
        except EOFError:
            break

def run(source):
    try:
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        if scanner.errors:
            return "\n".join(scanner.errors), False

        parser = Parser(tokens)
        expr = parser.parse()
        if expr is None:
            return "\n".join(str(e) for e in parser.errors), False

        return AstPrinter().print(expr), True
    except Exception as e:
        return f"Internal error: {e}", False

if __name__ == "__main__":
    main()
