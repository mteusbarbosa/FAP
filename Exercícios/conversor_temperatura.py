def fahrenheit_para_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius


def celsius_para_fahrenheit(celsius):
  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit


while True:
  try:
    print("1 - Fahrenheit para Celsius\n2 - Celsius para Fahrenheit")
    opcao = int(input("Escolha uma das duas opções: "))

    if opcao == 1:
      fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
      celsius = fahrenheit_para_celsius(fahrenheit)
      print(
          f"A temperatura de {fahrenheit:.0f}°F em Celsius é: {celsius:.0f}°C")
      break
    elif opcao == 2:
      celsius = float(input("Informe a temperatura em Celsius: "))
      fahrenheit = celsius_para_fahrenheit(celsius)
      print(
          f"A temperatura de {celsius:.0f}°C em Fahrenheit é: {fahrenheit:.0f}°F"
      )
      break
    else:
      print("Número inválida. Escolha 1 ou 2.")
  except ValueError:
    print("Valor inválido. Informe um número válido.")
