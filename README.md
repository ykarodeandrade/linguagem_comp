# Logus

### Está é uma linguagem de programação que remete ao Classicismo Romano.

# LATIM

## EBNF

    PROGRAM = { STATEMENT };

    BLOCK = { "{", STATEMENT, "}"};

    STATEMENT = ( λ | ASSIGNMENT | CONDIT | PRINT | LOOP | VAR | DECLARATION | RETURN_DEC ), "\n" ;

    ASSIGMENT = IDENTIFIER, "=", BOOL_EXP;

    CONDIT = "si", EXPRESSION, {"aliter", BLOCK|BLOCK};

    PRINT = "ostendere", "(", BOOL_EXP, ")";

    LOOP = "enim", ASSIGMENT, ";", EXPRESSION, ";", ASSIGMENT, BLOCK;

    VARIABILIS = TYPUS, ":", IDENTIFIER, {"=", EXPRESSION_BOOLEANA};

    TYPUS = (integer | catena_characterum);

    BOOL_EXP = BOOLTERM, {("||"), BOOLTERM};

    BOOLTERM = RELEXPRESSION, {("&&"), RELEXPRESSION};

    RELEXPRESSION = EXPRESSION, {("==" | "<" | ">"), EXPRESSION};

    EXPRESSION = TERM, {("+" | "-" | "."), TERM};

    TERM = FACTOR, {("*" | "/"), FACTOR };

    FACTOR = (("+" | "-" | "!"), FACTOR | STRING | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER, [ "(", ( { BOOL_EXP, ( ",", λ | BOOL_EXP ) } | λ ), ")" ] | SCAN);

    SCAN = "input", "(", ")";

    IDENTIFIER = LETTER, { LETTER | DIGIT | "_"};

    NUMBER = DIGIT, {DIGIT};

    STRING = ( a | ... | z | A | .. | Z);

    DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );


## Para mais delathes veja a apresentação que se encontra neste repositório.
