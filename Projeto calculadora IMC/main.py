print("=== Calculadora de IMC ===")
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau I"
elif imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
