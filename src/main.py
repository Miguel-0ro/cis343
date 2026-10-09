from scanner import Scanner
import sys

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
    run(source)

def run_prompt():
    
    while True:
        try:
            line = input("> ")
            if line == "":
                break
            run(line)
        except EOFError:
            break

def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)
    
if __name__ == "__main__":
    main()


