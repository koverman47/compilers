#!/usr/bin/env python3

from TinyListener import TinyListener
from TinyParser import TinyParser
from Scope import Scope


class Listener(TinyListener):

    def __init__(self):
        self.scope = Scope("GLOBAL")
        self.blockCt = 0
        self.currVarType = None

    def enterFunc_decl(self, ctx:TinyParser.Func_declContext):
        children = list(ctx.getChildren())
        self.scope = Scope(children[2], self.scope)

    def enterEveryRule(self, ctx):
        if type(ctx) ==  TinyParser.String_declContext:
            print(ctx.parentCtx.getText())
            print(ctx.getText())
        elif type(ctx) == TinyParser.Var_declContext:
            print(ctx.getText())

    def enterVar_decl(self, ctx: TinyParser.Var_declContext):
        text = ctx.getText()
        self.scope = Scope("somesting", self.scope)

    def enterIf_stmt(self, ctx:TinyParser.If_stmtContext):
        pass

    def exitIf_stmt(self, ctx:TinyParser.If_stmtContext):
        pass

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

    def get_symbol_table(self):
        return self.scope
