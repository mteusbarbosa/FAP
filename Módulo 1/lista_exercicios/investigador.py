"""Investigador Criminal: Crie um programa que faça 5 perguntas para uma pessoa  sobre um crime:  
 "Telefonou para a vítima?"  
 "Esteve no local do crime?"  
 "Mora perto da vítima?"  
 "Devia para a vítima?"  
 "Já trabalhou com a vítima?"  
O programa deve classificar a pessoa como:  
 "Inocente": 0-1 respostas positivas  
 "Suspeita": 2 respostas positivas  
 "Cúmplice": 3-4 respostas positivas  
 "Assassino": 5 respostas positivas """


def obter_resposta(pergunta):
  while True:
      resposta = input(pergunta).strip().lower()
      if resposta in ["sim", "não"]:
          return resposta
      else:
          print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        
# Função para centralizar e formatar a resposta
def formatar_resposta(texto):
    largura = 22  # Defina a largura desejada
    return f'|{texto.center(largura)}|'

print("Responda as perguntas com 'sim' ou 'não'")
pergunta1 = obter_resposta("Telefonou para a vítima? ")
pergunta2 = obter_resposta("Esteve no local do crime? ")
pergunta3 = obter_resposta("Mora perto da vítima? ")
pergunta4 = obter_resposta("Devia para a vítima? ")
pergunta5 = obter_resposta("Já trabalhou com a vítima? ")

respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

contagem_sim = respostas.count("sim")



print("\n" + "-" * 24)

if contagem_sim == 0 or contagem_sim == 1:
    print(formatar_resposta("Inocente"))
elif contagem_sim == 2:
    print(formatar_resposta("Suspeita"))
elif contagem_sim == 3 or contagem_sim == 4:
    print(formatar_resposta("Cúmplice"))
elif contagem_sim == 5:
    print(formatar_resposta("Assassino"))

print("-" * 24)