**Title: Laboratory Work Report: Lexer & Scanner**

**Course:** Formal Languages & Finite Automata

**Author:** Negai Marin

---

**Overview:**

The laboratory work focused on understanding the fundamental concepts of lexical analysis through the implementation of a lexer or scanner. Lexical analysis, a crucial phase in the compilation process, involves breaking down input text into smaller units called tokens. These tokens represent meaningful elements of the input, such as keywords, identifiers, operators, and literals. The primary objective was to gain familiarity with the inner workings of a lexer/scanner/tokenizer and implement a sample lexer to demonstrate its functionality.

---

**Objectives:**

1. Gain understanding of lexical analysis and its role in the compilation process.
2. Familiarize with the workings of a lexer, scanner, or tokenizer.
3. Implement a sample lexer and demonstrate its functionality.

---

### Defining Token Types:
I started the implementation by defining token types using regular expressions. Each token type corresponds to a specific pattern in the input text, such as numbers, operators, or parentheses. I used a dictionary named `TOKEN_TYPES` to map token names to their corresponding regular expression patterns.

### Token Class:
Next, I defined a `Token` class to represent individual tokens generated by the lexer. Each token has two attributes: `type` to store the token type and `value` to store the token's actual value. I also implemented a `__str__` method to provide a string representation of the token for easier debugging.

### Lexer Class:
The main part of the implementation is the `Lexer` class responsible for lexical analysis. The lexer scans through the input text character by character, matches patterns defined by token types, and generates tokens accordingly. I implemented methods such as `advance` to move to the next character, `skip_whitespace` to ignore whitespace characters, and `get_next_token` to retrieve the next token from the input text.

### Tokenization Process:
During the tokenization process, the lexer iterates over the input text, identifying tokens based on the defined token types and regular expression patterns. It skips whitespace characters and raises an error for invalid input characters. For each match found, the lexer creates a `Token` object with the corresponding type and value and advances to the next character.

### Testing:
To test the implemented lexer, I provided an example usage where the lexer tokenizes a simple arithmetic expression (`'3 + 4 * 5'`). The lexer successfully identifies tokens such as numbers, arithmetic operators, and whitespace, demonstrating its ability to analyze input text and generate tokens effectively.


---

**Code Snippets:**

```python
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position]

    def advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None

```

---

**Results:**

The implemented lexer successfully tokenizes input text according to predefined rules. It accurately identifies tokens such as identifiers, operators, and literals, producing a stream of tokens as output. Through testing with various input texts, the lexer demonstrates its ability to analyze input and generate tokens effectively.

---

**Conclusion:**

The laboratory work provided valuable insights into the process of lexical analysis and the role of lexers in the compilation process. By implementing a sample lexer, I gained practical experience in tokenizing input text and understanding the significance of tokens in language processing. The knowledge gained from this exercise will be beneficial for further exploration of compiler design and related topics.

---

**References:**

- [Python Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
- [Compiler Design: Lexical Analysis](https://www.geeksforgeeks.org/compiler-design-lexical-analysis/)
