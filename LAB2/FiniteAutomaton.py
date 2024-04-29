from graphviz import Digraph

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

    def is_deterministic(self):
        # Check if there are multiple transitions defined for the same state and input symbol
        seen_transitions = set()
        for (state, symbol), next_states in self.delta.items():
            for next_state in next_states:
                if (state, symbol) in seen_transitions:
                    return False  # Non-deterministic
                seen_transitions.add((state, symbol))
        return True  # Deterministic

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

    def convert_to_dfa(self):
        dfa_states = set()  # States of the DFA
        dfa_delta = {}  # Transition function of the DFA
        dfa_q0 = frozenset([self.q0])  # Initial state of the DFA

        # Initialize worklist with the initial state of the NFA
        worklist = [dfa_q0]

        while worklist:
            current_states = worklist.pop()
            dfa_states.add(current_states)

            for symbol in self.Sigma:
                next_states = set()
                for state in current_states:
                    next_states |= self.delta.get((state, symbol), set())

                next_states = frozenset(next_states)

                if next_states not in dfa_states:
                    worklist.append(next_states)

                dfa_delta[(current_states, symbol)] = next_states

        # Compute final states of the DFA
        dfa_final_states = {state for state in dfa_states if state & self.F}

        return FiniteAutomaton(dfa_states, self.Sigma, dfa_delta, dfa_q0, dfa_final_states)

    def iterate_automaton(self):
        # Convert frozenset objects to sets for readability
        converted_delta = {tuple(key): set(value) for key, value in self.delta.items()}
        converted_q = set(self.Q)
        converted_f = set(self.F)

        # Yield each component of the automaton
        yield "States:", converted_q
        yield "Alphabet:", self.Sigma
        yield "Transition Functions:", converted_delta
        yield "Initial State:", self.q0
        yield "Final States:", converted_f

    def visualize(self, filename='automaton'):
        dot = Digraph()
        dot.attr(rankdir='LR')

        # Add states
        for state in self.Q:
            dot.node(state, shape='circle')

        # Add initial state
        dot.node(self.q0, shape='doublecircle')

        # Add final states
        for state in self.F:
            dot.node(state, shape='doublecircle')

        # Add transitions
        for (from_state, symbol), to_states in self.delta.items():
            for to_state in to_states:
                dot.edge(from_state, to_state, label=symbol)

        # Save the graph
        dot.render(filename, format='png', cleanup=True)
        print(f"Graph saved as {filename}.png")
