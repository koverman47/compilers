from TinyListener import TinyListener

class Listener(TinyListener):
    symbol_t = {}

    def enterEveryRule(self,ctx:ParserRuleContext):

        #Need to use the parser rule context here

        pass

    def exitEveryRule(self, ctx:ParserRuleContext):
        #Dont know what to do
        pass

    def get_symbol_table(self):
        return self.symbol_t