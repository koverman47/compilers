from TinyListener import TinyListener
from TinyParser import TinyParser
from Scope import Scope
import sys

class Listener(TinyListener):
    
    def __init__(self):
        self.scope = Scope("GLOBAL")
        self.symbolTables = [self.scope]
        self.blockCt = 0
        self.currVarType = None
        self.writeVar = True

    def enterVar_decl(self, ctx:TinyParser.Var_declContext):
        self.writeVar = True

    def exitVar_decl(self, ctx:TinyParser.Var_declContext):
        self.writeVar = False

    def enterVar_type(self, ctx:TinyParser.Var_typeContext):
        self.currVarType = ctx.getText()

    def enterFunc_decl(self, ctx:TinyParser.Func_declContext):
        children = list(ctx.getChildren())
        self.scope = Scope(children[2], self.scope)
        self.symbolTables.append(self.scope)

    def exitFunc_decl(self, ctx: TinyParser.Func_declContext):
        self.scope = self.scope.parent

    def enterIf_stmt(self, ctx:TinyParser.If_stmtContext):
        self.blockCt += 1
        self.scope = Scope("BLOCK %d" % self.blockCt, self.scope)
        self.symbolTables.append(self.scope)

    def exitIf_stmt(self, ctx:TinyParser.If_stmtContext):
        self.scope = self.scope.parent

    def enterElse_part(self, ctx:TinyParser.Else_partContext):
        if len(ctx.getText()) > 0:
            self.blockCt += 1
            self.scope = Scope("BLOCK %d" % self.blockCt, self.scope)
            self.symbolTables.append(self.scope)
    
    def exitElse_part(self, ctx:TinyParser.Else_partContext):
        self.scope = self.scope.parent

    def enterWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        self.blockCt += 1
        self.scope = Scope("BLOCK %d" % self.blockCt, self.scope)
        self.symbolTables.append(self.scope)

    def exitWhile_stmt(self, ctx:TinyParser.While_stmtContext):
        self.scope = self.scope.parent

    def enterString_decl(self, ctx:TinyParser.String_declContext):
        children = list(ctx.getChildren())
        self.scope.symbols[children[1].getText()] = (children[0].getText(), children[3].getText())

    def enterId_list(self, ctx:TinyParser.Id_listContext):
        values = ctx.getText().split(",")
        if self.writeVar:
            for v in values:
                if v in self.scope.symbols:
                    print("DECLARATION ERROR %s" % v)
                    sys.exit(0)
                self.scope.symbols[v] = (self.currVarType, None)

    def enterParam_decl(self, ctx:TinyParser.Param_declContext):
        ct = list(ctx.getChildren())
        self.scope.symbols[ct[1].getText()] = (ct[0].getText(), None)

    def get_symbol_table(self):
        return self.symbolTables

    def print_symbol_tables(self):
        for t in self.symbolTables:
            print("Symbol table %s" % t.name)
            for k, v in t.symbols.items():
                if v[1]:
                    print("name %s type %s value %s" % (k, v[0], v[1]))
                else:
                    print("name, %s type %s" % (k, v[0]))

