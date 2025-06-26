# main.py
from core.lexer import ClojureLexer
from core.parser import ClojureParser

def main():
    print("=== Analisador Léxico e Sintático de Clojure ===\n")
    
    caminho = input("Digite o caminho do arquivo (.txt) para análise (ex: examples/valido.txt): ").strip()

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o caminho e tente novamente.")
        return

    lexer = ClojureLexer()
    parser = ClojureParser()

    try:
        resultado = parser.parse(lexer.tokenize(codigo))
        if resultado is not None:
            print("\n✅ Código analisado com sucesso!")
            print("Árvore sintática:")
            print(resultado)
        else:
            print("\n❌ Erro: código incompleto ou inválido.")
    except Exception as e:
        print("\n❌ Erro durante análise sintática:")
        print(e)

if __name__ == '__main__':
    main()
