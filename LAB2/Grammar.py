import FiniteAutomaton
import random


class Grammar:

    def __init__(self, Vn, Vt, P, S):
        self.Vt = Vt
        self.Vn = Vn
        self.P = P
        self.S = S

    def classify_grammar(self):
        # Check if the grammar is a regular grammar
        if self.is_regular_grammar():
            return "Regular Grammar"

        # Check if the grammar is a context-free grammar
        if self.is_context_free_grammar():
            return "Context-Free Grammar"

        # Check if the grammar is a context-sensitive grammar
        if self.is_context_sensitive_grammar():
            return "Context-Sensitive Grammar"

        # If none of the above conditions are met, it's an unrestricted grammar
        return "Unrestricted Grammar"

    def is_regular_grammar(self):
        # Check if the grammar is right-linear
        is_right_linear = self.is_right_linear_grammar()

        # Check if the grammar is left-linear
        is_left_linear = self.is_left_linear_grammar()

        return is_right_linear or is_left_linear

    def is_right_linear_grammar(self):
        # A grammar is right-linear if all production rules are of the form A -> aB or A -> a, where A, B are non-terminals
        for production in self.P:
            parts = production.split("->")
            if len(parts[1]) == 1 and parts[1] in self.Vt:
                # Single terminal on the right side, no non-terminal
                continue
            elif len(parts[1]) == 2 and parts[1][0] in self.Vt and parts[1][1] in self.Vn:
                # One terminal followed by one non-terminal
                continue
            else:
                # Production rule doesn't match the form of a right-linear grammar
                return False
        return True

    def is_left_linear_grammar(self):
        # A grammar is left-linear if all production rules are of the form A -> Ba or A -> a, where A, B are non-terminals
        for production in self.P:
            parts = production.split("->")
            if len(parts[1]) == 1 and parts[1] in self.Vt:
                # Single terminal on the right side, no non-terminal
                continue
            elif len(parts[1]) == 2 and parts[1][0] in self.Vn and parts[1][1] in self.Vt:
                # One non-terminal followed by one terminal
                continue
            else:
                # Production rule doesn't match the form of a left-linear grammar
                return False
        return True

    def is_context_free_grammar(self):
        # A grammar is context-free if all production rules are of the form A -> β, where A is a single non-terminal
        for production in self.P:
            parts = production.split("->")
            if len(parts[0]) == 1 and parts[0] in self.Vn:
                # Single non-terminal on the left side
                continue
            else:
                # Production rule doesn't match the form of a context-free grammar
                return False
        return True

    def is_context_sensitive_grammar(self):
        # A grammar is context-sensitive if all production rules are of the form α -> β, where |α| <= |β|
        for production in self.P:
            parts = production.split("->")
            if len(parts[0]) <= len(parts[1]):
                # Left side is shorter or equal in length to the right side
                continue
            else:
                # Production rule doesn't match the form of a context-sensitive grammar
                return False
        return True

    def generate_string(self):
        result = []
        self.generate_string_helper(self.S, result)
        return ''.join(result)

    def generate_string_helper(self, symbol, result):
        if symbol in self.Vt:
            result.append(symbol)
        else:
            productions = self.get_productions(symbol)
            selected_production = productions[random.randint(0, len(productions) - 1)]
            for c in selected_production:
                self.generate_string_helper(c, result)

    def get_productions(self, symbol):
        productions = []
        for production in self.P:
            parts = production.split("->")
            if parts[0] == symbol:
                productions.append(parts[1])
        return productions

    def to_finite_automaton(self):
        Sigma = list(self.Vt)

        Q = list(self.Vn)
        Q.extend(self.Vn)
        Q.append("X")

        q0 = self.S
        F = "X"

        delta = []
        for production in self.P:
            parts = production.split("->")
            left_side = parts[0]
            right_side = parts[1]

            if len(right_side) == 1 and right_side in self.Vt:
                delta.append({'from_state': left_side, 'symbol': right_side, 'to_state': F})
            elif len(right_side) > 1:
                delta.append({'from_state': left_side, 'symbol': right_side[0], 'to_state': right_side[1]})

        return FiniteAutomaton(Q, Sigma, delta, q0, F)
