from enum import Enum

class TokenType(Enum):
    INTEGER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    EOF = 7


import re

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

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return TokenType.INTEGER, self.integer()
            elif self.current_char == '+':
                self.advance()
                return TokenType.PLUS, '+'
            elif self.current_char == '-':
                self.advance()
                return TokenType.MINUS, '-'
            elif self.current_char == '*':
                self.advance()
                return TokenType.MULTIPLY, '*'
            elif self.current_char == '/':
                self.advance()
                return TokenType.DIVIDE, '/'
            elif self.current_char == '(':
                self.advance()
                return TokenType.LPAREN, '('
            elif self.current_char == ')':
                self.advance()
                return TokenType.RPAREN, ')'
            else:
                raise ValueError("Invalid character: {}".format(self.current_char))
        return TokenType.EOF, None


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'({self.left} {self.op} {self.right})'

class Num:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError("Invalid syntax")

    def factor(self):
        token = self.current_token
        if token[0] == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(token[1])
        elif token[0] == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

    def term(self):
        node = self.factor()

        while self.current_token[0] in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token[0] == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            elif token[0] == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)

            node = BinOp(left=node, op=token[1], right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token[0] in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token[0] == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token[0] == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token[1], right=self.term())

        return node

text = "3 + 4 * (2 - 1) - 10"
lexer = Lexer(text)
parser = Parser(lexer)
ast = parser.expr()

print(ast)
