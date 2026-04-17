# Lexical Analyzer - Compiler Design Task
# String: "this is a int sum = 10, a+b = 20"

# Define token types
KEYWORDS = {'this', 'is', 'int', 'if', 'else', 'while', 'for', 'return'}
OPERATORS = {'+', '-', '*', '/', '=', '<', '>', '!'}
SEPARATORS = {',', ';', '(', ')', '{', '}'}

def get_token_type(token):
    if token in KEYWORDS:
        return "Keyword"
    elif token.isdigit():
        return "Integer Literal"
    elif token in OPERATORS:
        return "Operator"
    elif token in SEPARATORS:
        return "Separator / Punctuation"
    elif token.isidentifier():
        return "Identifier"
    else:
        return "Unknown"

def tokenize(input_string):
    # Manually split while keeping operators and separators as separate tokens
    tokens = []
    current = ""

    for char in input_string:
        if char in OPERATORS or char in SEPARATORS:
            if current.strip():
                tokens.append(current.strip())
            tokens.append(char)
            current = ""
        elif char == ' ':
            if current.strip():
                tokens.append(current.strip())
            current = ""
        else:
            current += char

    if current.strip():
        tokens.append(current.strip())

    return tokens

# Input string
input_string = "this is a int sum = 10, a+b = 20"

print("Input String:", input_string)
print("-" * 40)
print(f"{'Token':<15} {'Type'}")
print("-" * 40)

tokens = tokenize(input_string)
for token in tokens:
    token_type = get_token_type(token)
    print(f"{token:<15} {token_type}")

print("-" * 40)
print(f"Total Tokens: {len(tokens)}")