from sly import Lexer

class ClojureLexer(Lexer):
    # Lista de tokens que o analisador irá reconhecer
    tokens = { NUMBER, STRING, SYMBOL }

    # Símbolos literais (não precisam de regex)
    literals = { '(', ')', '[', ']' }

    # Ignora espaços e tabs
    ignore = ' \t'

    # Ignora comentários iniciados por ;
    ignore_comment = r';.*'

    # Define como reconhecer números inteiros ou reais
    @_(r'\d+(\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t

    # Define strings entre aspas duplas
    @_(r'"([^"\\]|\\.)*"')
    def STRING(self, t):
        t.value = t.value[1:-1]  # remove aspas
        return t

    # Símbolos e identificadores (nomes de funções, operadores, variáveis)
    @_(r'[\+\-\*/<>=a-zA-Z_?!][\w+\-\*/<>=!?]*')
    def SYMBOL(self, t):
        return t

    # Ignora quebras de linha, mas conta linhas
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Tratamento de erro léxico
    def error(self, t):
        print(f'Caractere ilegal: {t.value[0]!r} na linha {self.lineno}')
        self.index += 1
