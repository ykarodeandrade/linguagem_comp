import sys
import re


class Token:
    def __init__(self, type: str, value):
        self.type = type
        self.value = value


class Tokenizer:

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
        # self.keywords = {'Println', 'if', 'else', 'for'}

    def selectNext(self):

        if self.position < len(self.source):
            char_atual = self.source[self.position]

            if char_atual == '\n':
                self.next = Token('LINHA_N', '\n')
                self.position += 1
            
            elif char_atual == ",":
                self.next = Token('VIRGULA', ',')
                self.position += 1 

            elif char_atual == '"':
                identicador = char_atual
                self.position += 1
                char_atual = self.source[self.position]

                while self.position < len(self.source) and char_atual != '"':
                    identicador += char_atual
                    self.position += 1
                    char_atual = self.source[self.position]

                if char_atual == '"':
                    identicador += char_atual
                    self.position += 1
                    identicador = identicador.strip('"')
                    self.next = Token('STRING', identicador)
                else:
                    raise SyntaxError("ERROR: String não fechada")

            elif char_atual.isspace():
                self.position += 1
                self.selectNext()

            elif char_atual.isalpha() or char_atual == "_":
                identicador = ""
                while self.position < len(self.source) and (char_atual.isalnum() or char_atual == "_"):
                    identicador += char_atual
                    self.position += 1
                    if self.position < len(self.source):
                        char_atual = self.source[self.position]

                if identicador == "ostendere":
                    self.next = Token('PRINTLN', 'ostendere')

                elif identicador == "officium":
                    self.next = Token('FUNC', 'officium')

                elif identicador == "gestus":
                    self.next = Token('SCANLN', 'gestus')

                elif identicador == "si":
                    self.next = Token('IF', 'si')

                elif identicador == "aliter":
                    self.next = Token('ELSE', 'aliter')

                elif identicador == "enim":
                    self.next = Token('FOR', 'enim')

                elif identicador == "variabilis":
                    self.next = Token('VAR', 'variabilis')

                elif identicador == "integri":
                    self.next = Token('TYPE', 'integri')

                elif identicador == "catena_characterum":
                    self.next = Token('TYPE', 'catena_characterum')

                elif identicador == "responsio":
                    self.next = Token('RETURN', 'responsio')

                else:
                    self.next = Token('IDENTIFIER', identicador)

            elif char_atual.isdigit():
                value = ""
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    value += self.source[self.position]
                    self.position += 1
                self.next = Token('INT', int(value))

            elif char_atual == "*":
                self.next = Token('MULTI', '*')
                self.position += 1
            elif char_atual == "/":
                self.next = Token('DIV', '/')
                self.position += 1
            elif char_atual == "+":
                self.next = Token('PLUS', '+')
                self.position += 1
            elif char_atual == "-":
                self.next = Token('MINUS', '-')
                self.position += 1
            elif char_atual == "(":
                self.next = Token('OPEN', '(')
                self.position += 1
            elif char_atual == ")":
                self.next = Token('CLOSE', ')')
                self.position += 1
            elif char_atual == "{":
                self.next = Token('CHAVES_A', '{')
                self.position += 1
            elif char_atual == "}":
                self.next = Token('CHAVES_F', '}')
                self.position += 1
            elif char_atual == ";":
                self.next = Token('PONTO_V', ';')
                self.position += 1
            elif char_atual == "=":
                if self.source[self.position+1] == "=":
                    self.next = Token('EQUALCON', '==')
                    self.position += 2
                else:
                    self.next = Token('EQUAL', '=')
                    self.position += 1
            elif char_atual == ">":
                self.next = Token('MAIOR', '>')
                self.position += 1

            elif char_atual == "<":
                self.next = Token('MENOR', '<')
                self.position += 1
            elif char_atual == "|":
                self.next = Token('OR', '||')
                self.position += 2
            elif char_atual == "&":
                self.next = Token('AND', '&&')
                self.position += 2
            elif char_atual == "!":
                self.next = Token('NOT', '!')
                self.position += 1
            elif char_atual == ".":
                self.next = Token('CONCATENAR', '.')
                self.position += 1
            else:
                raise SyntaxError("Error: letra não está no alfabeto")

        else:
            self.next = Token('EOF', 'EOF')

# classe para representar a tabela de símbolos


class SymbolTable:
    def __init__(self):  # inicializa a tabela de símbolos
        self.table = {}

    def setter(self, key, value):  # insere um novo símbolo na tabela
        if value[1] != self.table[key][1]:
            # tipo da variável, que poderá ser: Int ou String.
            raise SyntaxError("ERROR: tipo de variável diferente")
        self.table[key] = value

    def getter(self, key):  # retorna o valor de um símbolo
        return self.table[key]

    def create(self, key, value):
        if key in self.table.keys():
            raise SyntaxError("ERROR: variável já declarada no escopo")
        else:
            self.table[key] = value

class FuncTable: # tabela de funções
    def __init__(self):
        self.table = {}

    def setter(self, key, value):
        self.table[key] = value
        
    def getter(self, key):
        return self.table[key]

class Node:  # classe para representar os nós da árvore sintática
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, ST):
        pass


class BinOp(Node):  # classe para representar os operadores biniários
    def evaluate(self, ST):
        filho1 = self.children[0].evaluate(ST)
        filho2 = self.children[1].evaluate(ST)

        if self.value == '+':
            if filho1[1] !=filho2[1] or filho1[1] != "integri": # verifica se os tipos são iguais
                raise SyntaxError("ERROR")
            return (filho1[0] + filho2[0], "integri")
        elif self.value == "-":
            if filho1[1] !=filho2[1] or filho1[1] != "integri":
                raise SyntaxError("ERROR")
            return (filho1[0] - filho2[0], "integri")
        elif self.value == "*":
            if filho1[1] !=filho2[1] or filho1[1] != "integri":
                raise SyntaxError("ERROR")
            return (filho1[0] * filho2[0], "integri")
        elif self.value == "/":
            if filho1[1] !=filho2[1] or filho1[1] != "integri":
                raise SyntaxError("ERROR")
            return (filho1[0] // filho2[0], "integri")
        elif self.value == "&&":
            if filho1[1] !=filho2[1] or filho1[1] != "integri":
                raise SyntaxError("ERROR")
            return (int(filho1[0] and filho2[0]), "integri")
        elif self.value == "||":
            if filho1[1] !=filho2[1] or filho1[1] != "integri":
                raise SyntaxError("ERROR")
            return (int(filho1[0] or filho2[0]), "integri")
        elif self.value == "==":
            if filho1[1] !=filho2[1]:
                raise SyntaxError("ERROR")
            return (int(filho1[0] == filho2[0]), "integri")
        elif self.value == "<":
            return (int(filho1[0] < filho2[0]), "integri")
        elif self.value == ">":
            return (int(filho1[0] > filho2[0]), "integri")
        elif self.value == ".":
            return (str(filho1[0]) + str(filho2[0]), "catena_characterum")



class UnOp(Node):  # classe para representar os operadores unitários
    def evaluate(self, ST):
        if self.value == "+":
            # retorna o valor do filho
            return (self.children[0].evaluate(ST)[0], "integri")
        elif self.value == "-":
            # retorna o valor do filho negativo
            return (-self.children[0].evaluate(ST)[0], "integri")
        elif self.value == "!":
            return (not self.children[0].evaluate(ST)[0], "integri")


class IntVal(Node):  # classe para representar os números inteiros
    def evaluate(self, ST):
        return (int(self.value), "integri")  # retorna o valor do nó


class NoOp(Node):  # classe para representar os nós vazios
    def evaluate(self, ST):
        pass  # não faz nada


class Assigment(Node): # classe para representar a atribuição de valores
    def evaluate(self, ST):
        ST.setter(self.children[0].value, self.children[1].evaluate(ST))


class Identifier(Node): # classe para representar os identificadores
    def evaluate(self, ST):
        return ST.getter(self.value)


class Block(Node): # classe para representar os blocos
    def evaluate(self, ST):
        for child in self.children:
            if isinstance(child, ReturnNode):
                return child.evaluate(ST)
            child.evaluate(ST)


class Print(Node):
    def evaluate(self, ST):
        print(self.children[0].evaluate(ST)[0]) # imprime apenas o valor
        # return 0


class VarDec(Node): # var int x = numero;
    def evaluate(self, ST):
        if len(self.children) == 1: # verifica se tem valor
            if self.value == "integri":
                ST.create(self.children[0].value, (0, self.value)) # cria a variável na tabela de símbolos
            elif self.value == "catena_characterum":
                ST.create(self.children[0].value, ("", self.value)) 
        else:
            t = self.children[1].evaluate(ST)
            if self.value != t[1]:
                raise SyntaxError("ERROR TIPO incorreto") # verifica se o tipo é igual
            ST.create(self.children[0].value, (t[0], self.value))


class Scan(Node):  # scanln ( )
    def evaluate(self, ST):
        return (int(input()), "integri")


class IfCond(Node):
    def evaluate(self, ST):
        if self.children[0].evaluate(ST)[0]:  # if
            self.children[1].evaluate(ST)
        elif len(self.children) > 2:  # else
            self.children[2].evaluate(ST)


class ForLoop(Node):
    def evaluate(self, ST):
        self.children[0].evaluate(ST)
        while self.children[1].evaluate(ST)[0]:  # SELECIONA APENAS O VALOR
            self.children[3].evaluate(ST)
            self.children[2].evaluate(ST)


class StrVal(Node): # classe para representar os números inteiros
    def evaluate(self, ST):
        return (self.value, "catena_characterum")

class FuncDec(Node):
    def evaluate(self, ST):
        FT.setter(self.children[0].children[0].value, (self, self.children[0].value))

FT = FuncTable()

class FuncCall(Node):
    def evaluate(self, ST):
        # Obter a função a ser chamada
        function = FT.getter(self.value)
        # Verificar se o número de parâmetros está correto
        if len(function[0].children) != len(self.children) + 2:
            raise SyntaxError("ERROR quantidade de parâmetros incorreta")
        
        local_symbol_table = SymbolTable()
        for i in range(len(self.children)):
            function[0].children[i+1].evaluate(local_symbol_table) # Definir o parâmetro na tabela de símbolos local
            local_symbol_table.setter(function[0].children[i+1].children[0].value, self.children[i].evaluate(ST))
        # Avaliar a chamada da função
        result = function[0].children[-1].evaluate(local_symbol_table)
        
        if result is not None: # Verificar e retornar o resultado da função
            if function[1] != result[1]:
                raise SyntaxError("ERROR Tipo de retorno da função incorreto")
            else:
                return result 

class ReturnNode(Node):
    def evaluate(self, ST):
        return self.children[0].evaluate(ST)



class Parser:
    tokenizer = None

    def ParserProgram(self):
        children = []
        while self.tokenizer.next.type != 'EOF':
            children.append(self.parserDeclaration()) # declaração de função
        children_main = FuncCall("main", []) # chamada da função main
        children.append(children_main)
        return Block(None, children)

    
    def ParserBlock(self):
        c = []
        if self.tokenizer.next.type == 'CHAVES_F':
            raise SyntaxError("Error: bloco vazio não é permitido")

        if self.tokenizer.next.type == 'CHAVES_A':
            self.tokenizer.selectNext()

            if self.tokenizer.next.type == 'LINHA_N':
                self.tokenizer.selectNext()
                while self.tokenizer.next.type != 'CHAVES_F':
                    c.append(self.ParserStatement())
            else:
                raise SyntaxError("Erro: Esperado '}' no final do bloco")
            self.tokenizer.selectNext()
        return Block(None, c)
    
    def ParserBoolExpression(self):
        result = self.ParserBoolTerm()
        while self.tokenizer.next.type == 'OR':
            operador = self.tokenizer.next
            self.tokenizer.selectNext()
            result = BinOp(operador.value, [result, self.ParserBoolTerm()])

        return result

    def parserDeclaration(self):
        
        while self.tokenizer.next.type == 'LINHA_N':

            self.tokenizer.selectNext()
        
        if self.tokenizer.next.type == 'FUNC':
            self.tokenizer.selectNext()
            result = FuncDec(None, [])
            if self.tokenizer.next.type == 'IDENTIFIER':
                funcao = Identifier(self.tokenizer.next.value, [])
                self.tokenizer.selectNext()
                
                if self.tokenizer.next.type == 'OPEN':
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == 'CLOSE':
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == 'TYPE':
                            tf = self.tokenizer.next.value # tipo da função
                            #
                            self.tokenizer.selectNext()
                            blco = self.ParserBlock() # cria o bloco
                            variavel = VarDec(tf, [funcao]) # cria a variável na tabela de símbolos
                        
                            return FuncDec(None, [variavel, blco])
                            
                            
                    elif self.tokenizer.next.type == 'IDENTIFIER':
                        
                        arg = Identifier(self.tokenizer.next.value, [])
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == 'TYPE':
                            tipo = self.tokenizer.next.value
                            result.children.append(VarDec(tipo, [arg]))
                            self.tokenizer.selectNext()
                            
                            while self.tokenizer.next.type == 'VIRGULA':
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.type == 'IDENTIFIER':
                                    arg = Identifier(self.tokenizer.next.value, [])
                                    self.tokenizer.selectNext()
                                    if self.tokenizer.next.type == 'TYPE':
                                        tipo = self.tokenizer.next.value
                                        result.children.append(VarDec(tipo, [arg]))
                                        self.tokenizer.selectNext()
                                    
                            if self.tokenizer.next.type == 'CLOSE':
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.type == 'TYPE':
                                    tf = self.tokenizer.next.value
                                    self.tokenizer.selectNext()
                                    blco = self.ParserBlock()
                                    result.children.append(blco)
                                    variavel = VarDec(tf, [funcao])
                                    result.children.insert(0, variavel)
                                    return result
        else:
            raise SyntaxError("ERROR: função não declarada")


    def ParserAssigments(self):
        args = [] # lista de argumentos
        if self.tokenizer.next.type == 'IDENTIFIER':
            identificador = Identifier(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()

            if self.tokenizer.next.type == 'EQUAL':
                self.tokenizer.selectNext()
                result = Assigment(None, [identificador, self.ParserBoolExpression()])

                if self.tokenizer.next.type == 'IDENTIFIER' or self.tokenizer.next.type == 'VIRGULA' or self.tokenizer.next.type == 'CLOSE':
                    raise SyntaxError("Error")
                return result

            elif self.tokenizer.next.type == 'OPEN':
                self.tokenizer.selectNext()
                
                if self.tokenizer.next.type != 'CLOSE':
                    arg = self.ParserBoolExpression() # argumento
                    args.append(arg) # adiciona o argumento na lista de argumentos
                    while self.tokenizer.next.type == 'VIRGULA':
                        self.tokenizer.selectNext()
                        arg = self.ParserBoolExpression() # argumento para adicionar na lista de argumentos
                        args.append(arg)
                    
                    if self.tokenizer.next.type == 'CLOSE':
                        self.tokenizer.selectNext()
                        return FuncCall(identificador.value, args)
                    else:
                        raise SyntaxError("ERROR parenteses não fechado") 
                elif self.tokenizer.next.type == 'CLOSE':
                    self.tokenizer.selectNext()
                    return FuncCall(identificador.value, [])
                else:
                    raise SyntaxError("ERROR parenteses não fechado")
            else:
                raise SyntaxError("ERROR parenteses não fechado")

    def ParserStatement(self):
 
        if self.tokenizer.next.type == 'IDENTIFIER':
            a = self.ParserAssigments() # atribuição
            self.tokenizer.selectNext()
            return a

        elif self.tokenizer.next.type == 'PRINTLN':
            self.tokenizer.selectNext()

            if self.tokenizer.next.type == 'OPEN':
                self.tokenizer.selectNext()
                result = self.ParserBoolExpression() # expressão
                
                if self.tokenizer.next.type == 'CLOSE':
                    self.tokenizer.selectNext()
                    f = Print(None, [result]) 


                    if self.tokenizer.next.type == 'LINHA_N':
                        self.tokenizer.selectNext()
                        return f
                    elif self.tokenizer.next.type == 'EOF':
                        return f
                    else:
                        raise SyntaxError("Erro: Esperado quebra de linha LINHA_N após PRINTLN ( )")
                else:
                    raise SyntaxError("Erro: Esperado CLOSE após PRINTLN (")
            else:
                raise SyntaxError("Erro: Esperado OPEN após PRINTLN")

        elif self.tokenizer.next.type == 'VAR':
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'IDENTIFIER':
                identicador = Identifier(self.tokenizer.next.value, []) 
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'TYPE':
                    tipo = self.tokenizer.next.value
                    decvar = VarDec(tipo, [identicador])
                    self.tokenizer.selectNext()


                    if self.tokenizer.next.type == 'EQUAL':
                        self.tokenizer.selectNext()
                        result = VarDec(
                            tipo, [identicador, self.ParserBoolExpression()])
                        if self.tokenizer.next.type == 'LINHA_N' or self.tokenizer.next.type == 'EOF':
                            self.tokenizer.selectNext()
                            return result
                    elif self.tokenizer.next.type == 'LINHA_N' or self.tokenizer.next.type == 'EOF':
                        self.tokenizer.selectNext()
                        return decvar
                    else:
                        raise SyntaxError("Erro: Esperado EQUAL após TYPE")

        elif self.tokenizer.next.type == "IF":
            self.tokenizer.selectNext()
            condicional = self.ParserBoolExpression()
            blocoIf = self.ParserBlock()

            if self.tokenizer.next.type == "ELSE":
                self.tokenizer.selectNext()
                blocElse = self.ParserBlock()
                if self.tokenizer.next.type == "LINHA_N" or self.tokenizer.next.type == "EOF":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "CHAVES_A":
                        raise SyntaxError(
                            "Erro: Sintaxe incorreta no bloco ELSE")
                    return IfCond(None, [condicional, blocoIf, blocElse])


            elif self.tokenizer.next.type == "EOF" or self.tokenizer.next.type == "LINHA_N":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "ELSE" or self.tokenizer.next.type == "CHAVES_A":
                    raise SyntaxError("Erro: Sintaxe incorreta no bloco IF")
                return IfCond(None, [condicional, blocoIf])


            else:
                raise SyntaxError("Erro: Erro na formatação do IF")

        elif self.tokenizer.next.type == 'FOR':
            self.tokenizer.selectNext()
            init = self.ParserAssigments()
            if self.tokenizer.next.type == 'PONTO_V':
                self.tokenizer.selectNext()
                condicional = self.ParserBoolExpression()
                if self.tokenizer.next.type == 'PONTO_V':
                    self.tokenizer.selectNext()
                    i = self.ParserAssigments()
                    blocoFor = self.ParserBlock()
                    if self.tokenizer.next.type == 'LINHA_N':
                        self.tokenizer.selectNext()
                        return ForLoop("for", [init, condicional, i, blocoFor])
                    elif self.tokenizer.next.type == 'EOF':
                        return ForLoop("for", [init, condicional, i, blocoFor])
                    else:
                        raise SyntaxError(
                            "Erro: Esperado quebra de linha LINHA_N após FOR init; condition; increment")
            else:
                raise SyntaxError("Erro: Esperado PONTO_V ; após FOR init")
        #
        elif self.tokenizer.next.type == 'RETURN':
            self.tokenizer.selectNext()
            f = ReturnNode(None, [self.ParserBoolExpression()])
            if self.tokenizer.next.type == 'LINHA_N':
                self.tokenizer.selectNext()
                return f
            
                    #
        elif self.tokenizer.next.type == 'LINHA_N' or self.tokenizer.next.type == 'EOF':
            result = NoOp(None, None)
            return result
        else:
            raise SyntaxError("Error: letra nao existe no alfabeto")

    def ParserBoolTerm(self):
        result = self.ParserRLExpression()
        while self.tokenizer.next.type == 'AND':
            operador = self.tokenizer.next
            self.tokenizer.selectNext()
            result = BinOp(operador.value, [result, self.ParserRLExpression()])

        return result

    def ParserRLExpression(self):
        result = self.ParserExpression()
        while self.tokenizer.next.type == 'EQUALCON' or self.tokenizer.next.type == 'MAIOR' or self.tokenizer.next.type == 'MENOR':
            operador = self.tokenizer.next
            if operador.type == 'EQUALCON':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserExpression()])
            elif operador.type == 'MAIOR':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserExpression()])
            elif operador.type == 'MENOR':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserExpression()])

        return result

    def ParserFactor(self):
        if self.tokenizer.next.type == 'INT':
            p = self.tokenizer.next.value
            self.tokenizer.selectNext()
            r = IntVal(p, [])
            return r

        if self.tokenizer.next.type == 'STRING':
            p = self.tokenizer.next.value
            self.tokenizer.selectNext()
            str = StrVal(p, [])
            return str

        elif self.tokenizer.next.type == "IDENTIFIER":
            p = self.tokenizer.next.value
            identificador = Identifier(p, [])
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'OPEN':
                res = FuncCall(identificador.value, [])
                self.tokenizer.selectNext()
                
                if self.tokenizer.next.type != 'CLOSE':
                    arg = self.ParserBoolExpression()
                    res.children.append(arg)
                    while self.tokenizer.next.type == 'VIRGULA':
                        self.tokenizer.selectNext()
                        arg = self.ParserBoolExpression()
                        res.children.append(arg)
                    
                    if self.tokenizer.next.type == 'CLOSE':
                        self.tokenizer.selectNext()
                        return res
                    
                else:
                    self.tokenizer.selectNext()
                    return res
            else:
            
                return identificador

        elif self.tokenizer.next.type == 'PLUS':
            self.tokenizer.selectNext()
            return UnOp("+", [self.ParserFactor()])

        elif self.tokenizer.next.type == 'MINUS':
            self.tokenizer.selectNext()
            return UnOp("-", [self.ParserFactor()])

        elif self.tokenizer.next.type == 'NOT':
            self.tokenizer.selectNext()
            return UnOp("!", [self.ParserFactor()])

        elif self.tokenizer.next.type == 'OPEN':
            self.tokenizer.selectNext()
            p = self.ParserBoolExpression()
            if self.tokenizer.next.type == 'CLOSE':
                self.tokenizer.selectNext()
                return p
            else:
                raise SyntaxError("ERROR parser factor parenteses não fechado")

        elif self.tokenizer.next.type == "SCANLN":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'OPEN':
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'CLOSE':
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == 'LINHA_N':
                        return Scan("Scanln", [])
                else:
                    raise SyntaxError("ERROR parser factor SCANLN")
        else:
            raise SyntaxError("ERROR parser factor CARACTERE INVÁLIDO")

    def ParserExpression(self):
        result = self.ParserTerm()
        while self.tokenizer.next.type == 'PLUS' or self.tokenizer.next.type == 'MINUS' or self.tokenizer.next.type == 'CONCATENAR':
            operador = self.tokenizer.next
            if operador.type == 'PLUS':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserTerm()])
            elif operador.type == 'MINUS':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserTerm()])
            elif operador.type == 'CONCATENAR':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserTerm()])

        return result

    def ParserTerm(self):
        result = self.ParserFactor()
        while self.tokenizer.next.type == 'MULTI' or self.tokenizer.next.type == 'DIV':
            operador = self.tokenizer.next
            if operador.type == 'MULTI':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserFactor()])
            elif operador.type == 'DIV':
                self.tokenizer.selectNext()
                result = BinOp(operador.value, [result, self.ParserFactor()])

        return result

    def run(self, code):
        pre_pro = PrePro.filter(code)
        Parser.tokenizer = Tokenizer(pre_pro)
        self.tokenizer.selectNext()
        result = self.ParserProgram()
        if self.tokenizer.next.type != 'EOF':
            raise SyntaxError("Erro ao consumir a cadeia de caracteres EOF")
        return result


class PrePro:
    @staticmethod
    def filter(source):
        source = re.sub(r'\/\/[^\n]*', '', source)
        source = re.sub(r'\/\*.*?\*\/', '', source, flags=re.DOTALL)

        texto = source.split('\n')
        t = [line for line in texto if line.strip() != '']

        textofiltrado = '\n'.join(t)

        return textofiltrado.strip()


if __name__ == "__main__":
    ST = SymbolTable()
    p = Parser()
    pasta = sys.argv[1]
    with open(pasta, 'r') as arq:
        c = arq.read()+'\n'
    arq.close()
    chars = p.run(c)
    chars.evaluate(ST)
