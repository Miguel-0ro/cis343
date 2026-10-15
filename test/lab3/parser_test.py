import subprocess, sys, tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent.parent / "src"
sys.path.insert(0, str(SRC))
from main import run 

VALID = [
    # literals
    ("number", "123", "123"),
    ("string", '"hello"', "hello"),
    ("true", "true", "true"),
    ("false", "false", "false"),
    ("nil", "nil", "nil"),
    # every operator
    ("+", "1 + 2", "(+ 1 2)"),
    ("-", "1 - 2", "(- 1 2)"),
    ("*", "2 * 3", "(* 2 3)"),
    ("/", "6 / 3", "(/ 6 3)"),
    ("<", "1 < 2", "(< 1 2)"),
    ("<=", "1 <= 2", "(<= 1 2)"),
    (">", "1 > 2", "(> 1 2)"),
    (">=", "1 >= 2", "(>= 1 2)"),
    ("==", "1 == 1", "(== 1 1)"),
    ("!=", "1 != 2", "(!= 1 2)"),
    ("unary -", "-5", "(- 5)"),
    ("unary !", "!true", "(! true)"),
    # precedence, associativity, grouping
    ("precedence", "1 + 2 * 3", "(+ 1 (* 2 3))"),
    ("left associativity", "1 - 2 - 3", "(- (- 1 2) 3)"),
    ("unary chain", "!!true", "(! (! true))"),
    ("grouping", "(1 + 2) * 3", "(* (group (+ 1 2)) 3)"),
    ("nested grouping", "((1))", "(group (group 1))"),
]

ERRORS = [
    ("unclosed paren", "(1 + 2"),
    ("unmatched )", ")"),
    ("missing right operand", "1 +"),
    ("missing left operand", "* 3"),
    ("unexpected token", "1 + * 3"),
    ("trailing tokens", "1 2"),
    ("lexical error", "1 @ 2"),
]

results = []  

for purpose, src, expected in VALID:
    try:
        out, ok = run(src)
    except Exception as e:
        out, ok = f"EXCEPTION: {e!r}", False
    results.append((purpose, src, expected, out.strip(),
                    ok and out.strip() == expected))

# invalid expressions
for purpose, src in ERRORS:
    try:
        out, ok = run(src)
        passed = (not ok) and "line" in out.lower()
    except Exception as e:
        out, passed = f"EXCEPTION: {e!r}", False
    results.append((purpose, src, "error with location", out.strip(), passed))

# source-file mode
#--- AI Code ---
with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
    f.write("1 + 2 * 3\n")
r = subprocess.run([sys.executable, str(SRC / "main.py"), f.name],
                   capture_output=True, text=True)
out = (r.stdout + r.stderr).strip()
results.append(("file mode", "1 + 2 * 3", "(+ 1 (* 2 3))", out,
                out == "(+ 1 (* 2 3))"))
#--- end AI code --- reasoning: have not touched file mode since my first year of College.

# interactive mode: good line, bad line, good line
r = subprocess.run([sys.executable, str(SRC / "main.py")],
                   input="1 + 2\n(1 +\n3 * 4\n", capture_output=True, text=True)
out = r.stdout + r.stderr
results.append(("REPL recovery", "1 + 2 | (1 + | 3 * 4",
                "two ASTs and one error", out.strip(),
                "(+ 1 2)" in out and "(* 3 4)" in out and "Traceback" not in out))

# report
#---AI Code INFLUENCE ---
for purpose, src, exp, act, ok in results:
    print(f"{'PASS' if ok else 'FAIL'}  {purpose}: {src!r}")
    if not ok:
        print(f"      expected: {exp}\n      actual:   {act}")
print(f"\n{sum(r[-1] for r in results)}/{len(results)} passed")
#--- end AI code INFLUENCE --- Explanation: I talked with AI to see what a quicker way to test the code would be. 
