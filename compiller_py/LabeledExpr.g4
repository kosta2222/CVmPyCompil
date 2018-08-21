grammar LabeledExpr; // rename to distinguish from Expr.g4

init: prog tochka ;
prog:   stat+  ;

stat:   expr ';'               # toExpr
    |   ID '=' expr ';'         # assign
    |   'print' '(' expr ')'  ';'      #toPrint 
    |   'def' NAME ':'  suite        #toDef    
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ;

suite:  '[' prog end_func                #toSuite
;

end_func:  ']'                           #toEndFunc
;
tochka: '.' #toTochka
;
NAME: [a-z]+ ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
//NL:[\r? \n]+ ;     // return newlines to parser (is end-statement signal)
WS:[ \t\r\n]+ -> skip ; // toss out whitespace
