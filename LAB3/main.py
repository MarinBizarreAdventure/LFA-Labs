import re

# Define token types
TOKEN_TYPES = {
    'NUMBER': r'\d+',
    'PLUS': r'\+',
    'MINUS': r'\-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'\/',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
}

# Define a token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

# Define a lexer class
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            for token_type, pattern in TOKEN_TYPES.items():
                match = re.match(pattern, self.text[self.pos:])
                if match:
                    token_value = match.group(0)
                    token = Token(token_type, token_value)
                    self.advance()
                    return token

            self.error()

        return None

# Example usage
text = '3 + 4 * 5'
lexer = Lexer(text)
token = lexer.get_next_token()
while token:
    print(token)
    token = lexer.get_next_token()