class Scope():

    def __init__(name, parent=None):
        self.name = name
        self.parent = parent
        self.symbols = {}

