#!/usr/bin/env python3

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
        self.registers = []
        self.register_counter = 1
        self.assembly_code = []

    def push(self):
        reg = "T%d" % (self.register_counter)
        self.registers.append(reg)
        self.register_counter += 1
        return reg

    def enterVar_decl(self, ctx:TinyParser.Var_declContext):
        self.writeVar = True

    def exitVar_decl(self, ctx:TinyParser.Var_declContext):
        self.writeVar = False

    def enterVar_type(self, ctx:TinyParser.Var_typeContext):
        self.currVarType = ctx.getText()

    def enterFunc_decl(self, ctx:TinyParser.Func_declContext):
        print('func decl')
        children = list(ctx.getChildren())
        self.scope = Scope(children[2], self.scope)
        self.symbolTables.append(self.scope)

    def exitFunc_decl(self, ctx: TinyParser.Func_declContext):
        print('exit funcl')
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

    def getTypeByKey(self, table, key):
        if key in table.symbols:
            return table.symbols[key][0]
        elif not self.table.parent:
            pass
        return self.getTypeByKey(table.parent, key)

    # Enter a parse tree produced by TinyParser#assign_expr.
    def enterAssign_expr(self, ctx:TinyParser.Assign_exprContext):
        ct = list(ctx.getChildren())
        t = self.getTypeByKey(self.scope, ct[0])
        tr = self.push()
        self.register_counter += 1
        if t == "INT":
            store = "STOREI %s %s" % (tr, ct[0])
        elif t == "INT":
            store = "STOREF %s %s" % (tr, ct[0])

    # Exit a parse tree produced by TinyParser#assign_expr.
    def exitAssign_expr(self, ctx:TinyParser.Assign_exprContext):
        print('exit assign')

    # Enter a parse tree produced by TinyParser#expr_list.
    def enterExpr_list(self, ctx:TinyParser.Expr_listContext):
        print('enter expr list')

    # Exit a parse tree produced by TinyParser#expr_list.
    def exitExpr_list(self, ctx:TinyParser.Expr_listContext):
        print('exit expr list')


    # Enter a parse tree produced by TinyParser#expr_list_tail.
    def enterExpr_list_tail(self, ctx:TinyParser.Expr_list_tailContext):
        print('exit expr list tail')

    # Exit a parse tree produced by TinyParser#expr_list_tail.
    def exitExpr_list_tail(self, ctx:TinyParser.Expr_list_tailContext):
        print('exit expr list tail')

    # Enter a parse tree produced by TinyParser#mulop.
    def enterMulop(self, ctx:TinyParser.MulopContext):
        opr = ctx.getText()
	if (opr == '*'):
		print('enter multiply')
		#return mult(ctx)
	elif (opr == '/'):
		print('enter divide')
		#return divi(ctx)
        print(ctx.getText())

    # Exit a parse tree produced by TinyParser#mulop.
    def exitMulop(self, ctx:TinyParser.MulopContext):
        print('exit mul op')

    # Enter a parse tree produced by TinyParser#addop.
    def enterAddop(self, ctx:TinyParser.AddopContext):
	opr = ctx.getText()
	if (opr == '+'):
		print('enter add')
		#return add(ctx)
	elif (opr == '-'):
		print('enter subtract')
		#return sub(ctx)

    # Exit a parse tree produced by TinyParser#addop.
    def exitAddop(self, ctx:TinyParser.AddopContext):
        print('exit add')

    # Enter a parse tree produced by TinyParser#write_stmt.
    def enterWrite_stmt(self, ctx:TinyParser.Write_stmtContext):
        print('enter write')

    # Exit a parse tree produced by TinyParser#write_stmt.
    def exitWrite_stmt(self, ctx:TinyParser.Write_stmtContext):
        print('exit write')

    # Enter a parse tree produced by TinyParser#read_stmt.
    def enterRead_stmt(self, ctx:TinyParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by TinyParser#read_stmt.
    def exitRead_stmt(self, ctx:TinyParser.Read_stmtContext):
        pass
