grammar Tiny;

/* Program */
program           : KEYWORD ID KEYWORD pgm_body KEYWORD;
pgm_body          : decl func_declarations;
decl		      : string_decl decl | var_decl decl | ;

/* Global String Declaration */
string_decl       : KEYWORD ID ':=' STR ';' ;
STR               : STRINGLITERAL;

/* Variable Declaration */
var_decl          : var_type id_list ';' ;
var_type	      : KEYWORD | KEYWORD;
any_type          : var_type | KEYWORD;
id_list           : ID id_tail;
id_tail           : ',' ID id_tail | ;

/* Function Paramater List */
param_decl_list   : '(' param_decl param_decl_tail ')' | '(' ')' | ;
param_decl        : var_type ID;
param_decl_tail   : ',' param_decl param_decl_tail | ;

/* Function Declarations */
func_declarations : func_decl func_declarations | ;
func_decl         : KEYWORD any_type ID param_decl_list KEYWORD func_body KEYWORD;
func_body         : decl stmt_list;

/* Statement List */
stmt_list         : stmt stmt_list | ;
stmt              : base_stmt | if_stmt | while_stmt;
base_stmt         : assign_stmt | read_stmt | write_stmt | return_stmt;

/* Basic Statements */
assign_stmt       : assign_expr ';' ;
assign_expr       : ID ':=' expr;
read_stmt         : KEYWORD '(' id_list ')' ';' ;
write_stmt        : KEYWORD '(' id_list ')' ';' ;
return_stmt       : KEYWORD expr ';' ;

/* Expressions */
expr              : expr_prefix factor;
expr_prefix       : expr_prefix factor addop | ;
factor            : factor_prefix postfix_expr;
factor_prefix     : factor_prefix postfix_expr mulop | ;
postfix_expr      : primary | call_expr;
call_expr         : ID '(' expr_list ')';
expr_list         : expr expr_list_tail | ;
expr_list_tail    : ',' expr expr_list_tail | ;
primary           : '(' expr ')' | ID | INTLITERAL | FLOATLITERAL;
addop             : '+' | '-';
mulop             : '*' | '/';

/* Complex Statements and Condition */
if_stmt           : KEYWORD '(' cond ')' decl stmt_list else_part KEYWORD;
else_part         : KEYWORD decl stmt_list | ;
cond              : expr compop expr;
compop            : '<' | '>' | '=' | '!=' | '<=' | '>=';


/* While statements */
while_stmt       : KEYWORD '(' cond ')' decl stmt_list KEYWORD;

start: .*? EOF;

WS: (' ' | '\t' | '\r' | '\n' ) -> skip;

INTLITERAL: [0-9]+;

FLOATLITERAL: [0-9]*'.'[0-9]+ ;

STRINGLITERAL: '"'.*?'"';

COMMENT: '--'.*?'\n' -> skip;

KEYWORD: 'PROGRAM'
    |'BEGIN'
    |'END'
    |'FUNCTION'
    |'READ'
    |'WRITE'
    |'IF'
    |'ELSE'
    |'ENDIF'
    |'WHILE'
    |'ENDWHILE'
    |'CONTINUE'
    |'BREAK'
    |'RETURN'
    |'INT'
    |'VOID'
    |'STRING'
    |'FLOAT';

ID				  : [A-Za-z]+[0-9]* ;


OPERATOR:':='
    |'+'
    |'-'
    |'*'
    |'/'
    |'='
    |'!='
    |'<'
    |'>'
    |'('
    |')'
    |';'
    |','
    |'<='
    |'>='
    ;
