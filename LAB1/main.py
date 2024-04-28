import random

class FiniteAutomaton:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F


    def __iter__(self):
        for transition in self.delta:
            yield transition



    def string_belong_to_language(self, input_string):
        current_states = {self.q0}

        for symbol in input_string:
            input_symbol = str(symbol)

            next_states = set()

            for current_state in current_states:
                transitions = self.find_transitions(current_state, input_symbol)
                for transition in transitions:
                    next_states.add(transition['to_state'])

            if not next_states:
                return False

            current_states = next_states

        for current_state in current_states:
            if current_state in self.F:
                return True

        return False

    def find_transitions(self, current_state, input_symbol):
        result = []
        for transition in self.delta:
            if transition['from_state'] == current_state and transition['symbol'] == input_symbol:
                result.append(transition)
        return result


class Grammar:
    def __init__(self, Vn, Vt, P, S):
        self.Vt = Vt
        self.Vn = Vn
        self.P = P
        self.S = S

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


nr_words = 5
Vn = ["S", "B", "C"]
Vt = ["a", "b", "c", "d"]
P = ["S->dA", "A->d", "A->aB", "B->bC", "C->cA", "C->aS"]
grammar = Grammar(Vn, Vt, P, "S")

for i in range(nr_words):
    generated_word = grammar.generate_string()
    print(f"Generaed word {i + 1}: {generated_word}")

finite_automaton = grammar.to_finite_automaton()

print(finite_automaton.string_belong_to_language('dd'))


gen = finite_automaton.__iter__()

for value in gen:
    print(value)