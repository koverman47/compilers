grammar Tiny;


/* Statement List */
stmt_list       : stmt stmt_list | ;
stmt            : base_stmt | if_stmt | while_stmt;
base_stmt       : assign_stmt | read_stmt | write_stmt | return_stmt;

/* Basic Statements */

assign_stmt     : assign_expr ';' ;
assign_expr     : id ':=' expr;
read_stmt       : 'READ' '(' id_list ')' ';' ;
return_stmt     : 'RETURN' expr ';' ;

/* Expressions */
expr            : expr_prefix factor;
expr_prefix     : expr_prefix factor addop | ;
factor          : factor_prefic postfix_expr;
factor_prefix   : factor_prefix postfix_expr mulop | ;
postfix_expr    : primary | call_expr ;
call_expr       : id '(' expr_list ')'
expr_list       : expr expr_list_tail | ;
expr_list_tail  : ',' expr expr_list_tail | ;
primary         : '(' expr ')' | id | INTLITERAL | FLOATLITERAL ;
addop           : '+' | '-' ;
mulop           : '*' | '/' ;

/* Complex Statements and Condition */
if_stmt         : 'IF' '(' cond ')' decl stmt_list else_part 'ENDIF';
else_part       : 'ELSE' decl stmt_list | ;
cond            : expr compop expr;
compop          : '<' | '>' | '=' | '!=' | '<=' | '>=';

/* While statements */
while_stmt      : 'WHILE' '(' cond ')' decl stmt_list 'ENDWHILE';