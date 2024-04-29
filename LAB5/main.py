class CFGNormalizer:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S

    def eliminate_epsilon(self):
        epsilon_productions = {key for key, value in self.P.items() if '' in value}
        new_productions = {key: value for key, value in self.P.items() if key not in epsilon_productions}
        for key, value in self.P.items():
            for production in value:
                if any(symbol in epsilon_productions for symbol in production):
                    for eps_key in epsilon_productions:
                        new_production = production.replace(eps_key, '')
                        if new_production != '':
                            new_productions[key] = new_productions.get(key, []) + [new_production]
        self.P = new_productions

    def eliminate_unit(self):
        unit_productions = {key for key, value in self.P.items() if len(value) == 1 and value[0] in self.VN}
        new_productions = {key: value for key, value in self.P.items() if key not in unit_productions}
        for key, value in self.P.items():
            for production in value:
                if any(symbol in unit_productions for symbol in production):
                    for unit_key in unit_productions:
                        new_productions[key] = new_productions.get(key, []) + self.P[unit_key]
        self.P = new_productions

    def eliminate_inaccessible(self):
        reachable = {self.S}
        changed = True
        while changed:
            changed = False
            for key, value in self.P.items():
                if key in reachable:
                    for production in value:
                        for symbol in production:
                            if symbol in self.VN and symbol not in reachable:
                                reachable.add(symbol)
                                changed = True
        self.P = {key: value for key, value in self.P.items() if key in reachable}

    def eliminate_nonproductive(self):
        productive = set()
        changed = True
        while changed:
            changed = False
            for key, value in self.P.items():
                if key in productive:
                    continue
                if all(symbol in (self.VT | productive) for production in value for symbol in production):
                    productive.add(key)
                    changed = True
        self.P = {key: value for key, value in self.P.items() if key in productive}

    def convert_to_cnf(self):
        new_productions = {}
        for key, value in self.P.items():
            for production in value:
                if len(production) > 2:
                    for i in range(len(production) - 1):
                        new_key = f'{key}#{i}'
                        new_productions[new_key] = [production[i:i + 2]]
                        key = new_key
                    new_productions[key] = [production[-1]]
                else:
                    new_productions[key] = value
        self.P = new_productions

    def normalize_grammar(self):
        self.eliminate_epsilon()
        self.eliminate_unit()
        self.eliminate_inaccessible()
        self.eliminate_nonproductive()
        self.convert_to_cnf()
        return self.P


# Unit tests
def test_cnf_normalization():
    VN = {'S', 'A', 'B', 'C', 'D'}
    VT = {'a', 'b'}
    P = {
        'S': ['aB', 'bA', 'A'],
        'A': ['B', 'Sa', 'bBA', 'b'],
        'B': ['b', 'bS', 'aD', ''],
        'D': ['AA'],
        'C': ['Ba']
    }
    S = 'S'

    normalizer = CFGNormalizer(VN, VT, P, S)
    normalized_grammar = normalizer.normalize_grammar()

    expected_normalized_grammar = {
        'S': ['aB', 'bA', 'A'],
        'A': ['B', 'Sa', 'B#0', 'b'],
        'B': ['b', 'bS', 'aD', ''],
        'B#0': ['B#1'],
        'B#1': ['A'],
        'D': ['AA'],
        'C': ['Ba']
    }

    assert normalized_grammar == expected_normalized_grammar
    print("Normalization Successful!")


if __name__ == "__main__":
    test_cnf_normalization()
