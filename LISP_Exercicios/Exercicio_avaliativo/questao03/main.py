import math

while True:
    # Input do usuario - forma a ser calculada:
    forma = int(input("Digite o número da respectiva forma a ser calculada (1-triângulo, 2-círculo, 3-retângulo, "
                      "4-sair): "))

    # Se o usuario inserir um número inválido:
    if forma not in [1, 2, 3, 4]:
        print("Opção inválida. Digite novamente a opção desejada:")
        continue

    # Cálculo da área do triângulo:
    if forma == 1:
        base = input("Digite o valor da base: ")
        altura = input("Digite o valor da altura: ")

        # Validação dos valores para realizar o calculo:
        if not (base.isnumeric() and altura.isnumeric()) or float(base) <= 0 or float(altura) <= 0:
            print("Valores inválidos. Digite novamente os respectivos valores:")
            continue

        # Cálculo e impressão da área do triângulo:
        print(f"A área do triângulo é {float(base) * float(altura) / 2}")

    # Cálculo da área do círculo:
    elif forma == 2:
        raio = input("Digite o valor do raio do círculo: ")

        # Validação dos valores para realizar o calculo:
        if not raio.isnumeric() or float(raio) <= 0:
            print("Valores inválidos. Digite novamente os respectivos valores:")
            continue

        # Cálculo e impressão da área do círculo:
        print(f"A área do círculo é {math.pi * float(raio) ** 2}")

    # Cálculo da área do retângulo:
    elif forma == 3:
        base = input("Digite o valor da base: ")
        altura = input("Digite o valor da altura: ")

        # Validação dos valores para realizar o calculo:
        if not (base.isnumeric() and altura.isnumeric()) or float(base) <= 0 or float(altura) <= 0:
            print("Valores inválidos. Digite novamente os respectivos valores:")
            continue

        # Cálculo e impressão da área do retângulo:
        print(f"A área do círculo é {float(base) * float(altura)}")

    else:
        break
