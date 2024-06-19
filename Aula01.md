# Introdução ao Python

Comando de impressão no terminal `print`

`print("Hello World!")` >> Hello World!

`print("Hello", "World!")` >> Hello World!

`print("Hello", "World!", sep = " ")` >> Hello World!
 <!-- A variável sep define o comportamento do separador -->

O caractere especial `\n` é o equivalente ao enter do teclado

`print("Hello\nWorld!")`

Hello

World!

Os comentários no código são feitos com `#Comentário` e ` ``` Comentário ``` `
>Comentários são importantes para documentar o código

## Tipos e variáveis

|Tipos|Descrição|
|-----|---------|
|int|Números Inteiros "1, 0, -5, 100"|
|float|Números reais "3.14,  1e-8,  12.34"|
|str|Cadeia de caracteres/Strings  "Mateus Barbosa"|
|bool|True ou False, 0 ou 1|

A função `type` é responsável por indicar o tipo do argumento:

`type("Hello World!")` >> `<class 'str'>`

### Atribuição de valores

`a = b = c = 3` Resulta nas três variáveis igual a 3

`a, b, c = 1, 2, 3` Resulta em a = 1, b = 2 e c = 3

### Regras de nomes de variáveis

Nomes de variáveis devem começar com uma letra maiúscula, minúscula ou sublinado _

## Operadores

- `+` Soma
- `-` Subtração
- `*` Multiplicação
- `/` Divisão
- `//` Divisão inteira (7//2 = 3)
- `**` Potenciação, elevado
- `%` Mod, resto da divisão

**Forma compacta** para atualizar variáveis:

- `x+= y` é equivalente a `x = x + y`
- `x-= y` é equivalente a `x = x - y`
- `x*= y` é equivalente a `x = x * y`
- `x/= y` é equivalente a `x = x / y`
- `x%= y` é equivalente a `x = x % y`

> Divisão por 0 gera erro

Concatenação de strings: `"Hello" + " World" = "Hello World"`
