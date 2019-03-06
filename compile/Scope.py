class Scope:
    def __init__(self, name, parentScope = None):
        self.name = name
        symbols = {}
        self.parentScope = parentScope