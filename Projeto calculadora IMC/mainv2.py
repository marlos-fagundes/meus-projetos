from imc import calcular_imc, classificar_imc
from utils import obter_float

def main():
    print("=== Calculadora de IMC ===")
    peso = obter_float("Informe seu peso (kg): ")
    altura = obter_float("Informe sua altura (m): ")

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
