#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"

errors = []
if not HTML.exists():
    errors.append("index.html is missing")
else:
    text = HTML.read_text(encoding="utf-8")

    required = [
        "<!doctype html>",
        '<meta name="viewport"',
        '<meta name="description"',
        "<title>Particles with an asymmetric funnel</title>",
        '<canvas id="simCanvas"',
        "<script>",
    ]
    for item in required:
        if item.lower() not in text.lower():
            errors.append(f"missing required markup: {item}")

    # The public visualiser is intentionally standalone.
    external_script = re.search(r'<script[^>]+src\s*=\s*["\']', text, re.I)
    external_css = re.search(r'<link[^>]+rel\s*=\s*["\']stylesheet["\'][^>]+href\s*=\s*["\']', text, re.I)
    if external_script:
        errors.append("external script dependency found")
    if external_css:
        errors.append("external stylesheet dependency found")

    for token in ("TODO", "FIXME", "console.log("):
        if token in text:
            errors.append(f"development token found: {token}")

    start = text.rfind("<script>")
    end = text.rfind("</script>")
    if start == -1 or end == -1 or end <= start:
        errors.append("embedded JavaScript block could not be extracted")
    else:
        script = text[start + len("<script>"):end]
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as f:
            f.write(script)
            temp_path = f.name
        try:
            result = subprocess.run(["node", "--check", temp_path], capture_output=True, text=True)
            if result.returncode:
                errors.append("embedded JavaScript failed node --check:\n" + result.stderr.strip())
        except FileNotFoundError:
            errors.append("Node.js is required for JavaScript syntax validation")
        finally:
            Path(temp_path).unlink(missing_ok=True)

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed: standalone markup and embedded JavaScript are clean.")
