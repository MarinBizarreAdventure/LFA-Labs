import random
import re


def choose_letter(pattern):
    if '|' in pattern:
        letters = pattern[1:-1].split('|')
        return random.choice(letters)
    else:
        return pattern[1]

def generate_tokens(token):
    if token[-1] == '*':
        num_tokens = random.randint(0, 5)
    elif token[-1] == '+':
        num_tokens = random.randint(1, 5)
    return num_tokens

def generate_word(tokens):
    word = ''
    for token in tokens:
        if token[-1] in ['*', '+']:

            generated_tokens = generate_tokens(token)
            for i in range(generated_tokens):
                if token[0] == '(':
                    word += choose_letter(token[:-1])
                else:
                    word += token[:-1]

        elif "^" in token:
            letter, size = token.split("^")
            for i in range(int(size)):
                if token[0] == '(':
                    word += choose_letter(token[:-2])
                else:
                    word += letter
        elif token[0] == '(':
            word += choose_letter(token[:])
        else:
            word += token
    return word

# Example usage
regex1 = "(S|T) (U|V) W* Y+ 24"
regex2 = "L (M|N) D^3 P* Q (2|3)"
regex3 = "R* S (T|U|V) W (X|Y|Z)^2 "
expression = "(S|T)* (U|V) W* Y+ 24"
tokens = regex3.split()



print("Tokens:", tokens)
word = generate_word(tokens)
print("Generated Word:", word)








