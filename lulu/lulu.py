import sys
import os
import warnings

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def preprocess_lulu_code(code: str) -> str:
    lines = code.splitlines()
    py_lines = []
    for line in lines:
        line = line.rstrip()
        if line.startswith('get '):
            remainder = line[4:]
            if ' import ' in remainder:
                module, names_str = remainder.split(' import ', 1)
                module = module.strip()
                names = names_str.strip()
                py_lines.append(f'from {module} import {names}')
                continue
            else:
                py_lines.append(line)
                continue
        if line.startswith('fctn '):
            py_lines.append(line.replace('fctn ', 'def ', 1))
            continue
        py_lines.append(line)
    return '\n'.join(py_lines)

def run_lulu_file(filename):
    with open(filename, 'r') as f:
        code = f.read()

    py_code = preprocess_lulu_code(code)

    # Capture warnings as exceptions so we can print them with :| |
    warnings.simplefilter("always")  

    try:
        with warnings.catch_warnings(record=True) as w:
            exec(py_code, globals())
            # print warnings, if any
            for warning in w:
                msg = warning.message
                print(f":| | {msg}")
    except SyntaxError as e:
        print(f":( | SyntaxError: {e.msg} (detected at line {e.lineno})")
    except Exception as e:
        print(f":( | {type(e).__name__}: {e}")
    else:
        print(":) | Script ran successfully")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lulu.py <script.lulu>")
        sys.exit(1)

    run_lulu_file(sys.argv[1])

