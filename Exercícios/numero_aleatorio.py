import random

numero_aleatorio = random.randrange(1,100)
tentativas = 1

while True:
  try:
    numero_escolhido = int(input("Escolha um número entre 1 e 100: "))
    if numero_escolhido < 0 or numero_escolhido > 100:
      print(f"O número escolhido deve estar entre 1 e 100. Tente novamente.")
    else:
      if numero_aleatorio == numero_escolhido:
        break
      else:
        if numero_escolhido < numero_aleatorio:
          print("%i é menor que o número aleatório" % numero_escolhido)
          tentativas += 1
        else:
          print("%i é maior que o número aleatório" % numero_escolhido)
          tentativas += 1
  except ValueError:
    print("Valor inválido. Informe um número válido.")
print(f"Parabéns, você acertou o número aleatório em {tentativas} tentativas!")
