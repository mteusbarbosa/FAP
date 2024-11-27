"""Decomposição de Cédulas: Escreva um programa que leia um valor em reais  (R$) e calcule a quantidade mínima de cédulas necessárias para representar esse  valor.
Considere cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e R$ 1.
"""

while True:
  try:
      valor = int(input("Digite o valor a ser sacado: "))
      break
  except ValueError:
    print("Valor inválido. Digite números inteiros.")


cedulas = [100, 50, 20, 10, 5, 2, 1]
for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula}")

