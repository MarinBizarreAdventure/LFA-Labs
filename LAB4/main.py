import random
import re


def choose_letter(pattern, steps):
    if '|' in pattern:
        letters = pattern[1:-1].split('|')
        selected_letter = random.choice(letters)
        steps.append(f"Choose letter from {pattern}: {selected_letter}")
        return selected_letter
    else:
        selected_letter = pattern[1]
        steps.append(f"Select letter from {pattern}: {selected_letter}")
        return selected_letter

def generate_tokens(token, steps):
    num_tokens = 1
    if token[-1] == '*':
        num_tokens = random.randint(0, 5)
        steps.append(f"Generate {num_tokens} tokens for {token}")
    elif token[-1] == '+':
        num_tokens = random.randint(1, 5)
        steps.append(f"Generate {num_tokens} tokens for {token}")
    return num_tokens

def generate_word(tokens, steps):
    word = ''
    for token in tokens:
        if token[-1] in ['*', '+']:
            generated_tokens = generate_tokens(token, steps)
            for i in range(generated_tokens):
                if token[0] == '(':
                    selected_letter = choose_letter(token[:-1], steps)
                    word += selected_letter
                else:
                    word += token[:-1]
        elif "^" in token:
            letter, size = token.split("^")
            for i in range(int(size)):
                if token[0] == '(':
                    selected_letter = choose_letter(token[:-2], steps)
                    word += selected_letter
                else:
                    word += letter
        elif token[0] == '(':
            selected_letter = choose_letter(token[:], steps)
            word += selected_letter
        else:
            word += token
    return word

def process_regular_expression(expression):
    tokens = expression.split()
    steps = []
    word = generate_word(tokens, steps)
    return word, steps

# Example usage
regex1 = "(S|T) (U|V) W* Y+ 24"
regex2 = "L (M|N) D^3 P* Q (2|3)"
regex3 = "R* S (T|U|V) W (X|Y|Z)^2 "
expression = "(S|T)* (U|V) W* Y+ 24"

print("Regular Expression:", expression)
generated_word, processing_steps = process_regular_expression(expression)

print("\nGenerated Word:", generated_word)
print("\nProcessing Steps:")
for step in processing_steps:
    print(step)