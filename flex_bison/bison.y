%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token SI
%token ALITER
%token OSTENDERE
%token PROPTER
%token DUM
%token INPUT
%token TYPUS_INTEGER
%token TYPUS_CATENA
%token L_BRACE
%token R_BRACE
%token NEWLINE
%token EQUALS
%token COLON
%token LPAREN
%token RPAREN
%token OR
%token AND
%token EQUAL_EQUAL
%token GREATER
%token LESS
%token PLUS
%token MINUS
%token TIMES
%token DIVIDE
%token ASSIGN
%token NOT
%token IDENTIFICATIO
%token INTEGER
%token CATENA_CHARACTERUM
%token DECLARE
%token RULE
%token COMMA

%%

program: statement
        | program statement
        ;

block: L_BRACE NEWLINE statements R_BRACE;

statements: statement
          | statements statement
          ;

statement: assigment NEWLINE
         | conditional NEWLINE
         | print NEWLINE
         | foreach NEWLINE
         | DUM NEWLINE
         | var NEWLINE
         | rule NEWLINE
         | traffic NEWLINE
         ;

assigment: IDENTIFICATIO ASSIGN rexpression
         | IDENTIFICATIO ASSIGN rexpression NEWLINE
         ;

conditional: SI bexpression block
           | SI bexpression block NEWLINE
           | SI bexpression block ALITER block NEWLINE
           ;

print: OSTENDERE LPAREN bexpression RPAREN
      ;

foreach: DUM assigment PROPTER assigment block
       ;

var: TYPUS_INTEGER DECLARE IDENTIFICATIO ASSIGN bexpression
   | TYPUS_INTEGER DECLARE IDENTIFICATIO
   | TYPUS_INTEGER DECLARE IDENTIFICATIO ASSIGN bexpression NEWLINE
   | TYPUS_INTEGER DECLARE IDENTIFICATIO NEWLINE
   | TYPUS_CATENA DECLARE IDENTIFICATIO ASSIGN bexpression
   | TYPUS_CATENA DECLARE IDENTIFICATIO
   | TYPUS_CATENA DECLARE IDENTIFICATIO ASSIGN bexpression NEWLINE
   | TYPUS_CATENA DECLARE IDENTIFICATIO NEWLINE
   ;

rule: RULE DECLARE IDENTIFICATIO L_BRACE NEWLINE var_list R_BRACE NEWLINE
    ;

var_list: var COMMA NEWLINE
        | var_list var COMMA NEWLINE
        ;

type: TYPUS_INTEGER
    | TYPUS_CATENA
    ;

match: IDENTIFICATIO
     ;

scanhost: IDENTIFICATIO
        ;

traffic: IDENTIFICATIO LPAREN RPAREN NEWLINE
       ;

bexpression: bterm
           | bexpression OR bterm
           ;

bterm: rexpression
     | bterm AND rexpression
     ;

rexpression: expression
           | rexpression EQUAL_EQUAL expression
           | rexpression GREATER expression
           | rexpression LESS expression
           ;

expression: term
          | expression PLUS term
          | expression MINUS term
          ;

term: factor
    | term TIMES factor
    | term DIVIDE factor
    ;

factor: PLUS factor
      | MINUS factor
      | NOT factor
      | INTEGER
      | CATENA_CHARACTERUM
      | LPAREN bexpression RPAREN
      | IDENTIFICATIO
      | match
      | scanhost
      | INPUT LPAREN RPAREN
      ;

%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}
