# CryptoLogos

### Está é uma linguagem de programação que remete ao Classicismo Romano e mescla conceitos de criptografica em seus scripts




# LATIM

## EBNF

    PROGRAMMA = { DECLARATIO };

    BLOCUS = { "{", "\n", DECLARATIO, "}" };

    DECLARATIO = ( lambda | ASSIGNATIO | CONDITIO | IMPRIMERE | PROPTER | DUM | VARIABILIS ), "\n";

    ASSIGNATIO = IDENTIFICATIO, "=", EXPRESSIO_RELATIONIS;

    CONDITIO = "si", EXPRESSIO_BOOLEANA, {"aliter", BLOCUS | BLOCUS};

    IMPRIMERE = "ostendere", "(", EXPRESSIO_BOOLEANA, ")";

    PROPTER = "propter", ASSIGNATIO, "ad", ASSIGNATIO, BLOCUS;

    DUM = "dum", EXPRESSIO_BOOLEANA, BLOCUS;

    VARIABILIS = TYPUS, ":", IDENTIFICATIO, {"=", EXPRESSIO_BOOLEANA};

    TYPUS = (integer | catena_characterum);

    EXPRESSIO_BOOLEANA = TERMINUS_BOOLEANUS, {("||"), TERMINUS_BOOLEANUS};

    TERMINUS_BOOLEANUS = EXPRESSIO_RELATIONIS, {("&&"), EXPRESSIO_RELATIONIS};

    EXPRESSIO_RELATIONIS = EXPRESSIO, {("==" | ">" | "<"), EXPRESSIO};

    EXPRESSIO = TERMINUS, {("+" | "-"), TERMINUS};

    TERMINUS = FACTOR, {("*" | "/"), FACTOR};

    FACTOR = (("+" | "-" | "!"), FACTOR | INTEGER | CATENA_CHARACTERUM | "(", EXPRESSIO, ")" | IDENTIFICATIO | INPUT);

    IDENTIFICATIO = LITTERA, { LITTERA | DIGITUS | "_"};

    INPUT = "input", "(", ")";

    CATENA_CHARACTERUM = ", {LITTERA}+, ";

    INTEGER = {NUMERUS}+;

    NUMERUS = DIGITUS, { DIGITUS };

    LITTERA = (a | ... | z | A | .. | Z);

    DIGITUS = (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0);

# CRIPTOGRAFADA

## EBNF

    EGDVGPBBP = { STRAPGPIXD };

    QADRJH = { "{", "\c", STRAPGPIXD, "}" };

    STRAPGPIXD = ( apbqsp | PHHXVCPIXD | RDCSXIXD | XBEGXBTGT | EGDEITG | SJB | KPGXPQXAXH ), "\c";

    PHHXVCPIXD = XSTCIXUXRPIXD, "=", TMEGTHHXD_GTAPIXDCXH;

    RDCSXIXD = "hx", TMEGTHHXD_QDDATPCP, {"paxitg", QADRJH | QADRJH};

    XBEGXBTGT = "dhitcstgt", "(", TMEGTHHXD_QDDATPCP, ")";

    EGDEITG = "egdeitg", PHHXVCPIXD, "ps", PHHXVCPIXD, QADRJH;

    SJB = "sjb", TMEGTHHXD_QDDATPCP, QADRJH;

    KPGXPQXAXH = INEJH, ":", XSTCIXUXRPIXD, {"=", TMEGTHHXD_QDDATPCP};

    INEJH = (xcitvtg | higxcv);

    TMEGTHHXD_QDDATPCP = ITGBXCJH_QDDATPCJH, {("||"), ITGBXCJH_QDDATPCJH};

    ITGBXCJH_QDDATPCJH = TMEGTHHXD_GTAPIXDCXH, {("&&"), TMEGTHHXD_GTAPIXDCXH};

    TMEGTHHXD_GTAPIXDCXH = TMEGTHHXD, {("==" | ">" | "<"), TMEGTHHXD};

    TMEGTHHXD = ITGBXCJH, {("+" | "-"), ITGBXCJH};

    ITGBXCJH = UPRIDG, {("*" | "/"), UPRIDG};

    UPRIDG = (("+" | "-" | "!"), UPRIDG | XCITVTG | HIGXCV | "(", TMEGTHHXD, ")" | XSTCIXUXRPIXD | XCEJI);

    XSTCIXUXRPIXD = AXIITGP, { AXIITGP | SXVXIJH | "_"};

    XCEJI = "xceji", "(", ")";

    HIGXCV = ", {AXIITGP}+, ";

    XCITVTG = {CJBTGJH}+;

    CJBTGJH = SXVXIJH, { SXVXIJH };

    AXIITGP = (p | ... | o | P | .. | O);

    SXVXIJH = (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0);
