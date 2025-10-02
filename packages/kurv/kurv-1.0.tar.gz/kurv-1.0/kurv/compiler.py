import sys
import re

def parse_be_like(line):
    # strip leading "be like "
    content_part = line[len("be like "):].strip()

    if not content_part.startswith("|"):
        return f'print("[ERROR parsing line: {line}]")'

    content = ""
    i = 1
    while i < len(content_part):
        if content_part[i] == "|" and content_part[i-1] != "\\":
            break
        content += content_part[i]
        i += 1
    else:
        # no closing pipe
        return f'print("[ERROR parsing line: {line}]")'

    # replace escaped pipes
    content = content.replace(r"\|", "|")

    rest = content_part[i+1:].strip()
    if rest.startswith(","):
        exprs = rest[1:].split(",")
        exprs = [e.strip() for e in exprs]
        return f'print("{content}", {", ".join(exprs)})'
    else:
        return f'print("{content}")'

def kv_to_py(kv_code: str) -> str:
    py_lines = []
    for line in kv_code.splitlines():
        line = line.strip()

        if line.startswith("pull up "):
            module = line[len("pull up "):].strip()
            py_lines.append(f"import {module}")
        elif line.startswith("be like "):
            py_lines.append(parse_be_like(line))
        else:
            py_lines.append(f'# Unknown line: {line}')

    return "\n".join(py_lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python kv_compiler.py <file.kv>")
        sys.exit(1)

    kv_file = sys.argv[1]
    try:
        with open(kv_file, "r") as f:
            kv_code = f.read()
    except FileNotFoundError:
        print(f"File not found: {kv_file}")
        sys.exit(1)

    py_code = kv_to_py(kv_code)
    # exec in globals so imports and print work
    exec(py_code, globals())

if __name__ == "__main__":
    main()