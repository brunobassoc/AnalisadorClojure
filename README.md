# 📘 Analisador Léxico e Sintático de Clojure

Este projeto implementa um analisador léxico e sintático da linguagem Clojure, utilizando a biblioteca [Sly (Sly Lex-Yacc)](https://sly.readthedocs.io/en/latest/) em Python.

Desenvolvido para a disciplina **Linguagens Formais e Autômatos** (G2), com foco em reconhecer estruturas básicas de Clojure como `def`, `defn`, expressões matemáticas prefixadas, `if`, `fn`, entre outras.

---

## ⚙️ Estrutura do Projeto

```
AnalisadorClojure/
├── core/
│   ├── lexer.py       # Definição de tokens
│   └── parser.py      # Definição das regras gramaticais
├── examples/
│   ├── valido.txt     # Exemplo de código Clojure válido
│   └── invalido.txt   # Exemplo de código com erro de sintaxe
├── main.py            # Script de execução no terminal
├── parser.out         # Arquivo gerado automaticamente pela Sly
```

---

## ✅ O que o projeto reconhece:

- `(def x 10)` – definição de variável
- `(defn nome [args] corpo)` – declaração de função
- `(+ a b)` – operações matemáticas prefixadas
- `(if cond then else)` – estrutura condicional
- `((fn [x] (* x x)) 5)` – aplicação de função anônima

---

## ▶️ Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/AnalisadorClojure.git
cd AnalisadorClojure
```

> ⚠️ Certifique-se de estar na branch `dev`.

---

### 2. Instalar dependência

O único requisito externo é a biblioteca `sly`:

```bash
pip install sly
```

---

### 3. Executar o analisador

```bash
python main.py
```

Digite o caminho para um dos arquivos de exemplo:

```
examples/valido.txt
```

---

## 🧪 Exemplos de Teste

### ✅ Válido:
```clojure
(def x 10)
(defn soma [a b] (+ a b))
(if (> x 5) "maior" "menor")
```

### ❌ Inválido:
```clojure
(def x)
(defn [a b] (+ a b))
((+ 1 2)
```

---

## 🔀 Branches

- `main` → versão final e estável.
- `dev` → ambiente de desenvolvimento ativo.

---

## 👨‍🏫 Professor

Projeto solicitado por: **Prof. Me. Fahad Kalil**

Usuário para compartilhamento: `fahadkalil` (no GitHub)

---

## 👤 Autor

Desenvolvido por Bruno Basso — [brunobasso](https://github.com/brunobassoc)
