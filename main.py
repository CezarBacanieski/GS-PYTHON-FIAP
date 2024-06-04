import os
import re  # Importa o módulo re para trabalhar com expressões regulares

def limpar_terminal():
    """
    Limpa o terminal de acordo com o sistema operacional.
    """
    if os.name == "nt":
        _ = os.system("cls")  # Limpa o terminal no Windows
    else:
        _ = os.system("clear")  # Limpa o terminal em sistemas Unix

def verificar_condicoes_climaticas():
    """
    Verifica as condições climáticas antes da saída do barco.
    """
    limpar_terminal()  # Limpa o terminal antes de exibir o menu
    print("VERIFICAÇÃO DE CONDIÇÕES CLIMÁTICAS\n")
    print("Selecione as condições climáticas atuais:")
    print("1 - Clima ensolarado e mar calmo")
    print("2 - Chuva leve")
    print("3 - Chuva intensa")
    print("4 - Risco de tempestade")
    print("5 - Mar agitado")
    opcao = input("\nOpção: ")

    if opcao == '1':
        return True  # Condições climáticas favoráveis
    elif opcao in ['2', '3', '4', '5']:
        print("\nCondições climáticas adversas. Saída do barco recusada.")
        return False  # Condições climáticas adversas
    else:
        print("\nOpção inválida.")
        return None  # Opção inválida

def registrar_entrada_saida():
    """
    Registra a entrada e saída de um barco, assim como a quantidade de lixo trazida.
    """
    barco = input("Nome do barco: ")
    entrada = input("Digite 's' para saída ou 'e' para entrada: ")

    if entrada.lower() == 's':
        condicoes_ok = verificar_condicoes_climaticas()  # Verifica as condições climáticas antes da saída
        if condicoes_ok is False:
            return None, None, None, None  # Retorna None se as condições climáticas não forem adequadas
        else:
            return barco, 'Saída', None, None  # Retorna os detalhes do registro de saída do barco
    elif entrada.lower() == 'e':
        while True:
            peso_lixo = input("Quantidade de lixo trazida (em kg): ")
            if re.match("^[0-9]+$", peso_lixo):  # Verifica se a entrada é um número inteiro
                break
            else:
                print("Quantidade de lixo inválida. Por favor, digite apenas números.")
        funcionarios = input("Funcionários presentes (separados por vírgula): ").split(',')
        return barco, 'Entrada', float(peso_lixo), funcionarios  # Retorna os detalhes do registro de entrada do barco
    else:
        print("Opção inválida.")
        return None, None, None, None  # Retorna None se a opção for inválida

def menu():
    """
    Exibe o menu principal e solicita a opção do usuário.
    """
    limpar_terminal()  # Limpa o terminal antes de exibir o menu
    print("MONITORAMENTO DE BARCOS E LIXO\n")
    print("1 - Registrar entrada/saída de barco")
    print("2 - Visualizar registro de barcos e lixo")
    print("3 - Sair\n")
    opcao = input("Opção: ")
    return opcao  # Retorna a opção selecionada pelo usuário

registros = []

while True:
    opcao = menu()

    if opcao == '1':
        registro = registrar_entrada_saida()
        if registro:
            registros.append(registro)  # Adiciona o registro à lista de registros se não for None
            print("Registro realizado com sucesso.")
        input("\nPressione Enter para continuar...")
    elif opcao == '2':
        limpar_terminal()  # Limpa o terminal antes de exibir os registros
        print("REGISTRO DE BARCOS E LIXO\n")
        if registros:
            for registro in registros:
                if registro[1] == 'Entrada':
                    print(f"Barco: {registro[0]}, Tipo: {registro[1]}, Lixo trazido (kg): {registro[2]}, Funcionários: {', '.join(registro[3])}")
                else:
                    print(f"Barco: {registro[0]}, Tipo: {registro[1]}")
        else:
            print("Nenhum registro encontrado.")
        input("\nPressione Enter para continuar...")
    elif opcao == '3':
        print("\nPrograma finalizado.")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
