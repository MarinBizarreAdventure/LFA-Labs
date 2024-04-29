from Grammar import Grammar


# Variant 20
# Q = {q0,q1,q2,q3},
# ∑ = {a,b,c},
# F = {q3},
# δ(q0,a) = q0,
# δ(q0,a) = q1,
# δ(q2,a) = q2,
# δ(q1,b) = q2,
# δ(q2,c) = q3,
# δ(q3,c) = q3.

class FiniteAutomatonToRegularGrammarConverter:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def convert_to_regular_grammar(self):
        Vn = list(self.Q)  # Non-terminal symbols are the states
        Vt = list(self.Sigma)  # Terminal symbols are the alphabet
        S = self.q0  # Start symbol is the initial state

        P = []

        # Add production rules based on transitions
        for state in self.Q:
            for symbol in self.Sigma:
                next_states = self.delta.get((state, symbol), set())
                for next_state in next_states:
                    P.append(f"{state}->{symbol}{next_state}")

        return Grammar(Vn, Vt, P, S)


