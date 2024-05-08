### Topic: Determinism in Finite Automata. Conversion from NDFA to DFA. Chomsky Hierarchy.

**Course:** Formal Languages & Finite Automata  
**Author:** Cretu Dumitru and kudos to the Vasile Drumea with Irina Cojuhari

#### Overview
A finite automaton is a mechanism used to represent processes of different kinds. It can be compared to a state machine as they both have similar structures and purpose as well. The word finite signifies the fact that an automaton comes with a starting and a set of final states. In other words, for a process modeled by an automaton, there is a clear beginning and ending.

Based on the structure of an automaton, non-determinism can arise when one transition leads to multiple states. Determinism characterizes how predictable a system is, and if randomness is involved, the system becomes non-deterministic. However, it's possible to achieve determinism through algorithms that modify the structure of the automaton.

#### Objectives:
- Understand the concept and usage of automata.
- Implement functions for classifying grammars based on Chomsky hierarchy.
- Convert finite automata to regular grammars.
- Determine if a finite automaton is deterministic or non-deterministic.
- Convert non-deterministic finite automata (NDFA) to deterministic finite automata (DFA).
- Represent finite automata graphically.

## Implementation Description

### Classification Function:
To classify grammars based on the Chomsky hierarchy, I implemented a function that analyzes the structure of grammars and determines their classification. The function examines the types of production rules present in the grammar and categorizes them as Type 0 (unrestricted), Type 1 (context-sensitive), Type 2 (context-free), or Type 3 (regular) grammars. By applying specific criteria defined by the Chomsky hierarchy, the function accurately classifies grammars into their respective types.

### Conversion to Regular Grammar:
I developed functionality to convert finite automata to regular grammars, enabling the transformation of automata-based representations to grammar-based representations. The conversion process involves analyzing the structure of the finite automaton, identifying transitions between states, and generating production rules for the regular grammar. By mapping transitions to production rules, the finite automaton is effectively converted into an equivalent regular grammar, preserving the language it represents.

### Determinism Check:
Implemented logic to determine whether a finite automaton is deterministic or non-deterministic. The determinism check examines the transition function of the finite automaton and verifies if each input symbol leads to exactly one next state. If any input symbol leads to multiple next states, the automaton is classified as non-deterministic. Conversely, if each input symbol has a unique next state, the automaton is deemed deterministic.

### NDFA to DFA Conversion:
I implemented functionality to convert non-deterministic finite automata (NDFA) to deterministic finite automata (DFA). The conversion process involves analyzing the transitions of the NDFA and constructing an equivalent DFA with a deterministic transition function. By systematically exploring the possible state combinations reachable from each DFA state, the NDFA is transformed into a DFA that retains the same language acceptance behavior.

### Graphical Representation:

Utilized external libraries/tools/APIs to represent finite automata graphically. The graphical representation enhances visualization and comprehension of automata structures by providing intuitive diagrams that depict states, transitions, and final states. By leveraging graphical visualization techniques, finite automata can be effectively communicated and analyzed, facilitating understanding and interpretation of their behavior.

However, during the implementation process, there were challenges encountered with setting up the graphical representation due to path issues with the environmental variables. The external libraries or tools required for graphical representation may have dependencies or specific installation requirements that necessitate proper configuration of the system environment. In such cases, troubleshooting path-related issues and ensuring correct setup of environmental variables become crucial for seamless integration and functioning of the graphical representation tools.



#### Conclusions
This laboratory work provided valuable insights into the concepts of determinism in finite automata and the conversion process from non-deterministic to deterministic finite automata. By implementing functions to classify grammars, convert automata, and visualize them graphically, we gained a deeper understanding of formal languages and automata theory.

For further details and code implementation, please refer to the respective files in the project repository.

---
**Note:** Screenshots, detailed implementation steps, and results can be provided upon request.
