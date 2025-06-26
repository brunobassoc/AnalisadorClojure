# core/parser.py
from sly import Parser
from core.lexer import ClojureLexer

class ClojureParser(Parser):
    debugfile = 'parser.out'

    tokens = ClojureLexer.tokens
    literals = { '(', ')', '[', ']' }

    @_('exprs')
    def program(self, p):
        return ('program', p.exprs)

    @_('expr exprs')
    def exprs(self, p):
        return [p.expr] + p.exprs

    @_('')
    def exprs(self, p):
        return []

    @_('"(" SYMBOL SYMBOL expr ")"')
    def expr(self, p):
        if p.SYMBOL0 == 'def':
            return ('def', p.SYMBOL1, p.expr)
        return ('call', p.SYMBOL0, [p.SYMBOL1, p.expr])

    @_('"(" SYMBOL expr_list ")"')
    def expr(self, p):
        return ('call', p.SYMBOL, p.expr_list)

    @_('"(" SYMBOL expr expr expr ")"')
    def expr(self, p):
        if p.SYMBOL == 'if':
            return ('if', p.expr0, p.expr1, p.expr2)
        return ('call', p.SYMBOL, [p.expr0, p.expr1, p.expr2])

    @_('"(" SYMBOL SYMBOL "[" param_list "]" expr ")"')
    def expr(self, p):
        if p.SYMBOL0 == 'defn':
            return ('defn', p.SYMBOL1, p.param_list, p.expr)
        return ('call', p.SYMBOL0, [p.SYMBOL1, p.param_list, p.expr])

    @_('"(" SYMBOL "[" param_list "]" expr ")"')
    def expr(self, p):
        if p.SYMBOL == 'fn':
            return ('fn', p.param_list, p.expr)
        return ('call', p.SYMBOL, [p.param_list, p.expr])

    @_('"(" expr expr_list ")"')
    def expr(self, p):
        return ('apply', p.expr, p.expr_list)

    @_('expr expr_list')
    def expr_list(self, p):
        return [p.expr] + p.expr_list

    @_('')
    def expr_list(self, p):
        return []

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)

    @_('SYMBOL')
    def expr(self, p):
        return ('symbol', p.SYMBOL)

    @_('SYMBOL param_list')
    def param_list(self, p):
        return [p.SYMBOL] + p.param_list

    @_('')
    def param_list(self, p):
        return []
