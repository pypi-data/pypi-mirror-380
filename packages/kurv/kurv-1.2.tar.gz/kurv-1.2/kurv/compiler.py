import sys

def parse_be_like(line):
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
        return f'print("[ERROR parsing line: {line}]")'

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

# ← Add these two functions at the bottom
def run_kv(kv_code: str):
    py_code = kv_to_py(kv_code)
    exec(py_code, globals())

def run_file(kv_file: str):
    with open(kv_file, "r") as f:
        code = f.read()
    run_kv(code)
