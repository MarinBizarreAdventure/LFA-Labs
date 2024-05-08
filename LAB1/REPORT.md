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

## Implementation Description

### Grammar Class Creation:
To meet the objectives of this laboratory assignment, a Python class named `Grammar` was created to represent grammars. This class serves as a blueprint for defining various grammars, featuring attributes such as `Vn` (non-terminal symbols), `Vt` (terminal symbols), `P` (productions), and `S` (start symbol). The pivotal method `generate_string()` utilizes `generate_string_helper()` to generate valid strings based on the grammar's production rules.

### String Generation:
Utilizing the `Grammar` class, five strings were generated in the main class using a loop and a `Grammar` object. The `generate_string()` method of the `Grammar` class facilitates the generation of valid strings conforming to the language described by the grammar. This functionality demonstrates the practical application of grammar rules in generating language constructs.

### FiniteAutomaton Class Development:
A class named `FiniteAutomaton` was crafted to represent finite automata. This class encapsulates essential attributes and methods, including `Q` (set of states), `Sigma` (alphabet), `delta` (transition function), `q0` (initial state), and `F` (set of final states). Notably, a method was added to facilitate the transformation of a `Grammar` object into a `Finite Automaton`. Delta, representing transitions, is represented by a dictionary structure.

### String Verification:
The final implementation included a method in the `FiniteAutomaton` class to determine whether a given string belongs to the constructed Finite Automaton. This method iterates through each symbol of the input string, checking for appropriate transitions using the `find_transitions()` method. By leveraging the transition function defined by delta, the automaton efficiently validates input strings against its language.

### Conclusions:
This laboratory work provided invaluable hands-on experience in grasping the core concepts of formal languages, particularly regular grammars. By implementing concrete examples, we gained insights into how these concepts manifest in practice. The process of converting a `Grammar` into a `Finite Automaton` and utilizing it to validate strings deepened our understanding of language recognition and manipulation. These experiences lay a solid foundation for tackling future laboratory assignments with confidence.

