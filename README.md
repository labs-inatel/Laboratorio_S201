# S201 - Paradigmas da Programação

Este repositório reúne os exercícios e relatórios produzidos durante a disciplina **S201 - Paradigmas da Programação**.

## Paradigmas Explorados

Durante a disciplina, foram abordados os seguintes paradigmas de programação, com exercícios práticos em diferentes linguagens:

- **Imperativo:** BASIC, C#, Go, Lua, Python
- **Funcional:** Lisp, Scala
- **Orientado a Objetos:** C#, Scala, Python
- **Concorrente e Seguro:** Go, Rust

## Tecnologias Utilizadas:

- **BASIC:**

Uma linguagem clássica de fácil leitura, ideal para introduzir conceitos fundamentais da programação imperativa.

- **C# (C-Sharp):**

Linguagem moderna da plataforma .NET, combinando orientação a objetos, programação imperativa e recursos funcionais.

- **Go (Golang):**

Desenvolvida pelo Google, destaca-se pela simplicidade, desempenho e suporte nativo a concorrência (paradigma concorrente).

- **Lisp:**

Uma das linguagens mais antigas ainda em uso, fortemente baseada em programação funcional e símbolo-recursiva.

- **Lua:**

Leve e embutível, muito usada em scripts e jogos. Permite uma abordagem imperativa com sintaxe enxuta.

- **Python:**

Versátil e de fácil leitura, com suporte a múltiplos paradigmas: imperativo, orientado a objetos e funcional.

- **Rust:**

Linguagem moderna focada em segurança de memória e concorrência segura, sem coletor de lixo.

- **Scala:**

Combina perfeitamente os paradigmas funcional e orientado a objetos, rodando sobre a JVM (Java Virtual Machine).

## Estrutura do Repositório

```
├── BASIC_Exercicios/
│   └── eqbhaskara.bas         # Equação de Bhaskara em BASIC
│
├── CSharp_Exercicios/
│   ├── exercicio01.cs         # Exercícios básicos em C#
│   └── exercicio02.cs
│
├── GO_Exercicios/
│   ├── Exercicio01            # Exercício introdutório em Go
│   └── Exercicio02
│
├── LISP_Exercicios/
│   ├── Exercicio_LISP         # Sintaxe e funções básicas
│   └── Exercicio_avaliativo   # Avaliação prática
│
├── LUA_Exercicios/
│   ├── Pares                  # Verificação de números pares
│   └── Tabuada                # Geração de tabuada
│
├── Python_Exercicios/
│   ├── exercicio01.py         # Scripts simples em Python
│   └── exercicio02.py
│
├── RUST_Exercicios/
│   ├── exercicio01_Rust       # Exercício básico com segurança de tipos
│   └── exercicio02_Rust
│
└── SCALA_Exercicios/
    ├── exercicio01            # Funcional e orientado a objetos em Scala
    └── exercicio02
```

## Ambiente de Execução

Todos os exercícios foram desenvolvidos e testados na plataforma online [Replit](https://replit.com).

## Como executar pelo Replit

1. Acesse [https://replit.com](https://replit.com).
2. Crie um novo repl para a linguagem correspondente.
3. Copie e cole o conteúdo do exercício desejado.
4. Execute e analise o resultado.

## Como Executar pelo Repositório Localmente

Para rodar os exercícios localmente no seu computador:

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/labs-inatel/Laboratorio_S201.git
   cd Laboratorio_S201
   ```

2. **Navegue até o diretório da linguagem e execute o arquivo correspondente.**  
   Por exemplo:

   - **Python (requer Python instalado):**
     ```bash
     cd Python_Exercicios
     python exercicio01.py
     ```

   - **C# (requer .NET SDK):**
     ```bash
     cd CSharp_Exercicios
     dotnet run exercicio01.cs
     ```

   - **Go:**
     ```bash
     cd GO_Exercicios
     go run Exercicio01.go
     ```

   - **LISP, Lua, Rust, Scala, etc.:**  
     Verifique se o interpretador ou compilador da linguagem está instalado e use o comando adequado (`sbcl`, `lua`, `rustc`, `scala`, etc.).

3. Para qualquer linguagem, certifique-se de ter o ambiente e compilador/interpretador configurado no seu sistema.
