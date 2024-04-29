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

**Implementation:**

For the implementation, I created a Python program that serves as a simple lexer. The lexer scans through input text character by character and identifies tokens based on predefined rules. I used regular expressions to define patterns for different token types, such as identifiers, operators, and literals. The program breaks down the input text into tokens and generates a stream of tokens as output.

I structured the implementation into a `Lexer` class responsible for lexical analysis and a `Token` class to represent individual tokens. The `Lexer` class scans the input text, matches patterns, and creates `Token` objects for each identified token. I documented the implementation thoroughly, explaining the functionality of each component and providing code snippets for clarity.

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

