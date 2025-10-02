import ast
import os
from pathlib import Path
from typing import List, Optional, Tuple
import requests
from textwrap import dedent

REPO_ROOT = Path.cwd()
SRC_DIR = REPO_ROOT / "src"

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "").strip()
MODEL = "mistral-small-latest"
API_URL = "https://api.mistral.ai/v1/chat/completions"
HTTP_TIMEOUT = 45
TEMPERATURE = 0.2

def _list_target_files(only_changed: bool, changed_files: Optional[List[str]]) -> List[Path]:
    """Lists Python files in the target directory, optionally filtering to only changed files.

Args:
    only_changed: If True, only include files that have changed.
    changed_files: List of changed file paths (relative to REPO_ROOT) if only_changed is True.

Returns:
    List of Path objects pointing to Python files in the target directory."""
    if only_changed and changed_files:
        out = []
        for p in changed_files:
            fp = (REPO_ROOT / p).resolve()
            if fp.suffix == ".py" and fp.is_file() and (SRC_DIR in fp.parents or fp.parent == SRC_DIR):
                out.append(fp)
        if out:
            return out
    return [p for p in SRC_DIR.rglob("*.py") if p.name != "__init__.py"]

def _has_docstring(node: ast.AST) -> bool:
    """Checks if an AST node has a docstring.

Returns:
    bool: True if the node has a docstring, False otherwise."""
    return ast.get_docstring(node) is not None

def _extract_code(lines: List[str], node: ast.AST) -> str:
    """Extracts source code from a list of lines for a given AST node.

Args:
    lines: List of source code lines.
    node: AST node with line number information.

Returns:
    The extracted source code as a string."""
    start = node.lineno - 1
    end = getattr(node, "end_lineno", node.lineno)
    return "".join(lines[start:end])

def _prompt(code: str, kind: str, name: str) -> str:
    """Generates a formatted prompt for creating a Google-style docstring for a given code snippet.

Args:
    code: The code snippet to document.
    kind: The type of the code (e.g., "function", "class").
    name: The name of the code entity being documented.

Returns:
    A formatted string containing the prompt instructions and code snippet."""
    return dedent(f"""
    Generate a concise Google-style Python docstring for the {kind} `{name}`.
    Return ONLY the docstring body (no triple quotes). Rules:
    - One-line summary, then a blank line.
    - Include Args/Returns/Raises only if applicable.
    - Infer types from annotations if present.
    - Keep lines ~90 chars max.

    {kind.capitalize()} code:
    ```python
    {code}
    ```
    """).strip()

def _call_mistral(prompt: str) -> Optional[str]:
    """Makes an API call to Mistral's LLM endpoint with the given prompt.

Args:
    prompt: The input prompt to send to the Mistral model.

Returns:
    The model's response as a string, or None if the request fails."""
    try:
        headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": TEMPERATURE}
        r = requests.post(API_URL, headers=headers, json=payload, timeout=HTTP_TIMEOUT)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"   ❌ LLM error: {e}")
        return None

def _insert_docstring(lines: List[str], node: ast.AST, text: str) -> List[str]:
    """Inserts a docstring into the specified line of code.

Args:
    lines: List of source code lines to modify.
    node: AST node containing the target function/method.
    text: Docstring text to insert (may include quotes).

Returns:
    Modified list of source code lines with docstring inserted."""
    insert_line = node.body[0].lineno if getattr(node, "body", None) else (node.lineno + 1)
    sig_line = lines[node.lineno - 1]
    base_indent = len(sig_line) - len(sig_line.lstrip(" "))
    indent = " " * (base_indent + 4)
    txt = text.strip()
    for q in ('"""', "'''"):
        if txt.startswith(q) and txt.endswith(q):
            txt = txt[len(q):-len(q)].strip()
    doc = f'{indent}"""' + txt + '"""\n'
    new_lines = list(lines)
    new_lines.insert(insert_line - 1, doc)
    return new_lines

def generate(only_changed: bool = False, changed_files: Optional[List[str]] = None) -> int:
    """Generates docstrings for Python functions and classes in files under 'src/'.

Args:
    only_changed: If True, only processes changed files (default: False).
    changed_files: Optional list of changed files to process.

Returns:
    int: 0 on success, 1 on error."""
    if not MISTRAL_API_KEY:
        print("❌ Missing MISTRAL_API_KEY in environment.")
        return 1
    if not SRC_DIR.exists():
        print("❌ 'src/' not found in current directory.")
        return 1

    files = _list_target_files(only_changed, changed_files)
    if not files:
        print("✅ No target files found under 'src/'.")
        return 0

    any_changed = False
    for path in files:
        if path.name == "__init__.py":
            continue
        print(f"\n📄 {path.relative_to(REPO_ROOT)}")
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        try:
            tree = ast.parse(text)
        except SyntaxError as e:
            print(f"   ❌ Syntax error: {e}")
            continue

        targets: List[Tuple[ast.AST, str, str]] = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if not _has_docstring(node):
                    code_block = _extract_code(lines, node)
                    kind = "class" if isinstance(node, ast.ClassDef) else "function"
                    targets.append((node, code_block, kind))

        if not targets:
            print("   ✅ Already documented.")
            continue

        print(f"   🔍 Missing docstrings: {len(targets)}")
        modified = False
        for node, code_block, kind in sorted(targets, key=lambda t: t[0].lineno, reverse=True):
            name = getattr(node, "name", "<unknown>")
            print(f"   ⏳ {kind} {name} ... ", end="", flush=True)
            doc = _call_mistral(_prompt(code_block, kind, name))
            if not doc:
                print("skip")
                continue
            lines = _insert_docstring(lines, node, doc)
            modified = True
            print("✅")

        if modified:
            path.write_text("".join(lines), encoding="utf-8")
            any_changed = True
            print(f"   💾 Updated: {path.name}")

    print("\n✅ No changes were necessary." if not any_changed else "\n✅ Docstrings generated and files updated.")
    return 0
