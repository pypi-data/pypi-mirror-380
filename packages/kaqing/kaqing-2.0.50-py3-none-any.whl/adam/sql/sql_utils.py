import re

def safe_terms(text: str):
    tokens = re.findall(r'"[^"]+"|\b\w+\b|\S', text)
    return tokens, len(tokens) > 1 or text.startswith(' ') or text.endswith(' ')