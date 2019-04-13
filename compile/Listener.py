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
        #print('func decl')
        children = list(ctx.getChildren())
        self.scope = Scope(children[2], self.scope)
        self.symbolTables.append(self.scope)

    def exitFunc_decl(self, ctx: TinyParser.Func_declContext):
        #print('exit funcl')
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
        if key in table.symbols.keys():
            return table.symbols[key][0]
        elif not table.parent:
            return
        return self.getTypeByKey(table.parent, key)

    # Enter a parse tree produced by TinyParser#assign_expr.
    def enterAssign_expr(self, ctx:TinyParser.Assign_exprContext):
        ct = list(ctx.getChildren())[0].getText()
        self.currVarType = self.getTypeByKey(self.scope, ct[0])
        tr = self.push()
        self.register_counter += 1
        if self.currVarType == "INT":
            self.assembly_code.append("STOREI %s %s" % (tr, ct[0]))
        elif self.currVarType == "FLOAT":
            self.assembly_code.append("STOREF %s %s" % (tr, ct[0]))

    # Exit a parse tree produced by TinyParser#assign_expr.
    def exitAssign_expr(self, ctx:TinyParser.Assign_exprContext):
        #print('exit assign')
        pass

    # Enter a parse tree produced by TinyParser#expr_list.
    def enterExpr_list(self, ctx:TinyParser.Expr_listContext):
        #print('enter expr list')
        pass

    # Exit a parse tree produced by TinyParser#expr_list.
    def exitExpr_list(self, ctx:TinyParser.Expr_listContext):
        #print('exit expr list')
        pass


    # Enter a parse tree produced by TinyParser#expr_list_tail.
    def enterExpr_list_tail(self, ctx:TinyParser.Expr_list_tailContext):
        #print('exit expr list tail')
        pass

    # Exit a parse tree produced by TinyParser#expr_list_tail.
    def exitExpr_list_tail(self, ctx:TinyParser.Expr_list_tailContext):
        #print('exit expr list tail')
        pass

    # Enter a parse tree produced by TinyParser#mulop.
    def enterMulop(self, ctx:TinyParser.MulopContext):
        opr = ctx.getText()
        if (opr == '*'):
            #print('enter multiply')
            #return mult(ctx)
            pass
        elif (opr == '/'):
            #print('enter divide')
	    #return divi(ctx)
            pass
        #print(ctx.getText())
        pass

    # Exit a parse tree produced by TinyParser#mulop.
    def exitMulop(self, ctx:TinyParser.MulopContext):
        #print('exit mul op')
        pass

    # Enter a parse tree produced by TinyParser#addop.
    def enterAddop(self, ctx:TinyParser.AddopContext):
        opr = ctx.getText()
        if (opr == '+'):
            #print('enter add')
            #return add(ctx)
            pass
        elif (opr == '-'):
            #print('enter subtract')
            #return sub(ctx)
            pass

    # Exit a parse tree produced by TinyParser#addop.
    def exitAddop(self, ctx:TinyParser.AddopContext):
        #print('exit add')
        pass

    # Enter a parse tree produced by TinyParser#write_stmt.
    def enterWrite_stmt(self, ctx:TinyParser.Write_stmtContext):
        #print('enter write')
        pass

    # Exit a parse tree produced by TinyParser#write_stmt.
    def exitWrite_stmt(self, ctx:TinyParser.Write_stmtContext):
        #print('exit write')
        pass

    # Enter a parse tree produced by TinyParser#read_stmt.
    def enterRead_stmt(self, ctx:TinyParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by TinyParser#read_stmt.
    def exitRead_stmt(self, ctx:TinyParser.Read_stmtContext):
        pass

    def enterFactor_prefix(self, ctx:TinyParser.Factor_prefixContext):
        if not ctx.mulop():
            return
        op = list(ctx.getChildren())[2]
        rf = self.registers.pop()
        rr = self.push()
        rl = self.push()
        code = ""
        if self.currVarType == "INT":
            if op == "*":
                code = "MULI %s %s %s" % (rl, rr, rf)
            elif op == "/":
                code = "DIVI %s %s %s" % (rl, rr, rf)
        elif self.currVarType == "FLOAT":
            if op == "*":
                code = "MULF %s %s %s" % (rl, rr, rf)
            elif op == "/":
                code = "DIVF %s %s %s" % (rl, rr, rf)
        self.assembly_code.append(code)

    def enterPrimary(self, ctx:TinyParser.PrimaryContext):
        result = self.registers.pop()
        line = ''
        if ctx.ID():
            line = "LOAD %s %s" % (ctx.ID(), result)
        elif ctx.INTLITERAL():
            line = "move %s %s" % (ctx.INTLITERAL(), result)
        elif ctx.FLOATLITERAL():
            line = "move %s %s" % (ctx.FLOATLITERAL(), result)
        self.assembly_code.append(line)

    # Enter a parse tree produced by TinyParser#expr_prefix.
    def enterExpr_prefix(self, ctx:TinyParser.Expr_prefixContext):
        #print('Prefix add op')
        if ctx.addop():
            op = list(ctx.getChildren())[2].getText()
            result = self.registers.pop()
            rr = self.push()
            rl = self.push()
            opper = ''
            if self.currVarType == 'INT':
                if op == '+':
                    opper = 'ADDI '
                elif op == '-':
                    opper = 'SUBI'
            elif self.currVarType == 'FLOAT':
                if op == '+':
                    opper = 'ADDF '
                elif op == '-':
                    opper = 'SUBF'
            print(opper)
            self.assembly_code.append("%s %s %s %s" % (opper, rl, rr, result))


