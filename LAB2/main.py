import random
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammar
from FiniteAutomatonToRegularGrammarConverter import FiniteAutomatonToRegularGrammarConverter


nr_words = 5
Vn = ["S", "B", "C"]
Vt = ["a", "b", "c", "d"]
P = ["S->dA", "A->d", "A->aB", "B->bC", "C->cA", "C->aS"]

# Vn = ["S", "A", "B", "C"]
# Vt = ["a", "b", "c", "d"]
# P = ["S->dA", "A->aB", "B->bC", "C->aS", "A->d", "C->cA"]

grammar = Grammar(Vn, Vt, P, "S")

grammar_type = grammar.classify_grammar()
print("Grammar Type:", grammar_type)


# Define the finite automaton
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c'}
delta = {('q0', 'a'): {'q0', 'q1'}, ('q2', 'a'): {'q2'}, ('q1', 'b'): {'q2'}, ('q2', 'c'): {'q3'}, ('q3', 'c'): {'q3'}}
q0 = 'q0'
F = {'q3'}


# Convert finite automaton to regular grammar
converter = FiniteAutomatonToRegularGrammarConverter(Q, Sigma, delta, q0, F)
regular_grammar = converter.convert_to_regular_grammar()

# Print the regular grammar
print("Regular Grammar:")
print("Vn:", regular_grammar.Vn)
print("Vt:", regular_grammar.Vt)
print("P:")
for rule in regular_grammar.P:
    print("  ", rule)
print("S:", regular_grammar.S)


fa = FiniteAutomaton(Q, Sigma, delta, q0, F)
dfa = fa.convert_to_dfa()
# b. Determine if the FA is deterministic or non-deterministic
if fa.is_deterministic():
    print("The finite automaton is deterministic.")
else:
    print("The finite automaton is non-deterministic.")


print("Converted DFA:")
for component, values in fa.iterate_automaton():
    print(component)
    print(values)
print("Converted DFA:")
for component, values in dfa.iterate_automaton():
    print(component)
    print(values)

# d. Draw the finite automaton graphically
fa.visualize()


