# Regular Expressions Laboratory Report

**Course:** Formal Languages & Finite Automata  
**Author:** Negai Marin  

## Theory

Regular expressions are a powerful tool used for pattern matching in strings. They consist of a sequence of characters that define a search pattern, allowing you to find specific patterns within text data. Regular expressions are widely used in programming, text processing, and data validation tasks.

## Objectives

The objectives of this laboratory work are as follows:
1. Understand the concept and usage of regular expressions.
2. Write a code that generates valid combinations of symbols conforming to given regular expressions.
3. Implement a function that shows the sequence of processing a regular expression.

## Implementation Description

### Generating Valid Combinations of Symbols:
To generate valid combinations of symbols based on provided regular expressions, we implemented a Python function named `generate_word`. This function takes a regular expression string as input and parses it to generate a valid word that conforms to the specified pattern. It handles special characters such as `*`, `+`, and `^`, as well as grouped expressions within parentheses.

The `generate_word` function recursively traverses the regular expression, generating tokens for each part of the expression. It uses helper functions such as `generate_tokens` to handle special cases where a token can be repeated multiple times (denoted by `*` or `+`) or a specific character needs to be repeated a certain number of times (denoted by `^`). Additionally, the function uses `choose_letter` to select a random letter from a group of letters enclosed within parentheses.

### Function for Showing Processing Sequence:
The `process_regular_expression` function was developed to demonstrate the sequence of processing a regular expression. This function takes a regular expression string as input, splits it into tokens, and generates a valid word based on the pattern defined by the regular expression. Along with the generated word, the function also returns a list of processing steps indicating the sequence of operations performed during pattern matching.

Each processing step provides insight into the steps involved in generating the valid word from the regular expression. It includes information such as selecting letters from grouped expressions, generating multiple tokens for repeated characters, and handling special cases like repetition and grouping.

In conclusion, this laboratory work provided hands-on experience in understanding and implementing regular expressions in Python. By exploring the concept of regular expressions and their usage, we gained practical insights into their importance in text processing and pattern matching tasks. The implementation of functions to generate valid combinations of symbols and to demonstrate the sequence of processing a regular expression enhanced our understanding of regular expressions and their applications in real-world scenarios.

Through this laboratory work, we developed practical skills in using regular expressions effectively in programming tasks. This experience will be valuable in future projects and tasks that involve text processing, data validation, and pattern matching.

## Conclusion

Overall, this laboratory work provided a comprehensive overview of regular expressions and their implementation in Python, contributing to our proficiency in formal languages and finite automata.

