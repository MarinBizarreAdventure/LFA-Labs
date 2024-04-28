# Laboratory Work Nr.2: Regular Grammars

**Course:** Formal Languages & Finite Automata  
**Student:** Negai Marin  

## Theory

In this laboratory work, we delve into the fundamental concepts of formal languages, particularly focusing on regular grammars. We explore the key attributes that define a formal language and understand the necessary components for a language to be formally recognized.

## Objectives:

1. Understand the essence of formal languages and their defining characteristics.
2. Set up the initial framework for the evolving project throughout the semester.
    a. Create a GitHub repository for project storage and updates.
    b. Select a programming language suitable for addressing the tasks efficiently.
    c. Organize reports separately to facilitate verification of work.

3. Tasks specific to this laboratory assignment:
    a. Implement a type/class for the given grammar.
    b. Develop a function to generate 5 valid strings from the language described by the grammar.
    c. Create functionality to convert a Grammar object to a Finite Automaton.
    d. Incorporate a method in the Finite Automaton to verify if an input string can be obtained through state transitions.

## Implementation:

To fulfill the objectives of this laboratory assignment, the following steps were undertaken:

1. **Grammar Class Creation:** A Python class named `Grammar` was created, serving as a blueprint for various grammars. It features attributes with descriptive names and a crucial method, `generateString()`, which utilizes `generateStringHelper()` to generate valid strings based on the grammar's rules.

2. **String Generation:** Utilizing the `Grammar` class, five strings were generated in the main class using a loop and a Grammar object.

3. **FiniteAutomaton Class Development:** A class named `FiniteAutomaton` was crafted, featuring specific attributes and methods. Notably, a method was added to facilitate the transformation of a Grammar object into a Finite Automaton. Delta is represented by a dictionary.

4. **String Verification:** The final implementation included a method to determine whether a given string belongs to the constructed Finite Automaton. This method iterates through each symbol, checking for appropriate transitions using the `findTransitions()` method.

## Conclusions:

This laboratory work provided invaluable hands-on experience in grasping the core concepts of formal languages, particularly regular grammars. By working through concrete examples, we gained insights into how these concepts manifest in practice. Additionally, the process of converting a Grammar into a Finite Automaton and utilizing it to validate strings deepened our understanding of language recognition and manipulation. These experiences lay a solid foundation for tackling future laboratory assignments with confidence.

