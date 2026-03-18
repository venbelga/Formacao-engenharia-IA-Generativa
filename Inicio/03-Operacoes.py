def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = input("Digite a opção: ")
        
        if opcao == '5':
            break
        
        match opcao:
            case '1' | '2' | '3' | '4':
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                match opcao:
                    case '1':
                        resultado = num1 + num2
                        print(f"Resultado: {resultado}")
                    case '2':
                        resultado = num1 - num2
                        print(f"Resultado: {resultado}")
                    case '3':
                        resultado = num1 * num2
                        print(f"Resultado: {resultado}")
                    case '4':
                        if num2 != 0:
                            resultado = num1 / num2
                            print(f"Resultado: {resultado}")
                        else:
                            print("Erro: Divisão por zero")
            case _:
                print("Opção inválida")

if __name__ == "__main__":
    calculadora()