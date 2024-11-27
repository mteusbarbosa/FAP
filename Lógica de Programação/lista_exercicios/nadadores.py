"""Classificador de Nadadores: Crie um programa que leia a idade de um nadador e  o classifique em uma das seguintes categorias:  
 Infantil A: 5 a 7 anos  
 Infantil B: 8 a 11 anos  
 Juvenil A: 12 a 13 anos  
 Juvenil B: 14 a 17 anos  
 Adultos: Maiores de 18 anos"""

while True:
  try:
    idade = int(input("Digite a idade do nadador: "))
    if idade < 5:
      print("Idade inválida!")
    else:
      if idade <= 7:
        print("Categoria: Infantil A")
      elif idade <= 11:
        print("Categoria: Infantil B")
      elif idade <= 13:
        print("Categoria: Juvenil A")
      elif idade <= 17:
        print("Categoria: Juvenil B")
      elif idade <= 100:
        print("Categoria: Adultos")
      else:
        print("Idade Inválida!")
      break
  except ValueError:
    print("Valor inválido. Matrículas devem ser apenas números")
