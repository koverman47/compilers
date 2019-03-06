from TinyListener import TinyListener
from TinyParser import TinyParser
from Scope import Scope

class Listener(TinyListener):
    scope = Scope("GLOBAL")
    blockCt = 0
    currVarType = None

    def enterEveryRule(self, ctx):
        if type(ctx) ==  TinyParser.String_declContext:
            print(ctx.parentCtx.getText())
            print(ctx.getText())
        elif type(ctx) == TinyParser.Var_declContext:
            print(ctx.getText())
        #Need to use the parser rule context here

    def enterVar_decl(self, ctx: TinyParser.Var_declContext):
        text = ctx.getText()
        self.scope = Scope("somesting", self.scope)

    def enterId_list(self, ctx: TinyParser.Id_listContext):
        pass

    def enterIf_stmt(self, ctx:TinyParser.If_stmtContext):
        pass

    def exitIf_stmt(self, ctx:TinyParser.If_stmtContext):
        pass

    def enterWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        pass


    def exitWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        pass


    def enterString_decl(self, ctx:TinyParser.String_declContext):
        pass

    def exitEveryRule(self, ctx):
        #Dont know what to do
        pass

    def get_symbol_table(self):
        return self.symbol_t
    # enter String_declContext
    #enter

