%{
#include "bison.tab.h" 
%}
 
%%

"si"                    { return SI; }
"aliter"                { return ALITER; }
"ostendere"             { return OSTENDERE; }
"propter"               { return PROPTER; }
"dum"                   { return DUM; }
"input"                 { return INPUT; }
"integer"               { return TYPUS_INTEGER; }
"catena_characterum"    { return TYPUS_CATENA; }

"{"                     { return L_BRACE; }
"}"                     { return R_BRACE; }
"\n"                    { return NEWLINE; }
"="                     { return EQUALS; }
":"                     { return COLON; }
"("                     { return LPAREN; }
")"                     { return RPAREN; }
"||"                    { return OR; }
"&&"                    { return AND; }
"=="                    { return EQUAL_EQUAL; }
">"                     { return GREATER; }
"<"                     { return LESS; }
"+"                     { return PLUS; }
"-"                     { return MINUS; }
"*"                     { return TIMES; }
"/"                     { return DIVIDE; }
"!"                     { return NOT; }
","                     { return COMMA; }

[a-zA-Z_][a-zA-Z0-9_]*  { return IDENTIFICATIO; }
[0-9]+                  { return INTEGER; }
[a-zA-Z]+               { return CATENA_CHARACTERUM; }
.                       { /* Ignorar outros caracteres */ }

%%

int yywrap() {
    return 1;
}
