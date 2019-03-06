from TinyListener import TinyListener
from TinyParser import TinyParser
from Scope import Scope

class Listener(TinyListener):
    scope = Scope("GLOBAL")
    blockCt = 0
    currVarType = None

    def enterVar_decl(self, ctx: TinyParser.Var_declContext):
        text = ctx.getText()
        self.scope = Scope("somesting", self.scope)

    def enterFunc_decl(self, ctx:TinyParser.Func_declContext):
        children = list(ctx.getChildren())
        self.scope = Scope(children[2], self.scope)

    def exitFunc_decl(self, ctx: TinyParser.Func_declContext):
        self.scope = self.scope.parent

    def enterIf_stmt(self, ctx:TinyParser.If_stmtContext):
        self.blockCt += 1
        self.scope = Scope("BLOCK %d" % self.blockCt, self.scope)

    def exitIf_stmt(self, ctx:TinyParser.If_stmtContext):
        self.scope = self.scope.parent
        print(ctx.getText())

    def enterWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        self.blockCt += 1
        self.scope = Scope("Block%d" % self.blockCt)

    def exitWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        self.scope = self.scope.parent

    def enterString_decl(self, ctx:TinyParser.String_declContext):
        pass

    def enterId_list(self, ctx:TinyParser.Id_listContext):
        values = ctx.getText().split(",")
        for v in values:
            self.scope.symbols[v] = self.currVarType

    def enterParam_decl(self, ctx:TinyParser.Param_declContext):
        ct = list(ctx.getChildren())
        self.scope.symbols[ct[1].getText()] = ct[0].getText()

    def get_symbol_table(self):
        return self.scope

