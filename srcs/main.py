# Interação com usuário e chama as funções de conversão

from validacao import validar_numero
from conversor import *

def definir_base_destino(b_origem):
    print("\nEscolha a base de destino:\n")
    print("1 - Binário")
    print("2 - Decimal")
    print("3 - Hexadecimal")
    
    bs_destino = input("\nOpção escolhida: ")
    
    while (bs_destino != '1' and bs_destino != '2' and bs_destino != '3' or bs_destino == b_origem):
        if (bs_destino == b_origem):
            print("\nOpção inválida!\nA base de destino deve ser diferente da base de origem.")
        else:
            print("\nOpção inválida!\nEscolha entre as opções 1, 2 ou 3.")
        bs_destino = input("\nOpção escolhida: ")
        
    return bs_destino

def definir_base_origem():
    print("\nEscolha a base de origem:\n")
    print("1 - Binário")
    print("2 - Decimal")
    print("3 - Hexadecimal")
    
    bs_origem = input("\nOpção escolhida: ")
    
    while (bs_origem != '1' and bs_origem != '2' and bs_origem != '3'):
        print("\nOpção inválida!\nEscolha entre as opções 1, 2 ou 3.")
        bs_origem = input("\nOpção escolhida: ")
    
    return bs_origem


def exibir_menu():
    print("\n================== CALCULADORA DE CONVERSÃO DE BASES ==================")
    
    base_origem = definir_base_origem()
    
    numero = input("\nNúmero a ser convertido: ")
    while (validar_numero(numero, base_origem) != 1):
        bases = {'1': "binária", '2': "decimal", '3': "hexadecimal"}
        print(f"\nNúmero inválido para a base {bases[base_origem]}!\nPor favor, tente novamente.")
        numero = input("\nNúmero a ser convertido: ")
    
    base_destino = definir_base_destino(base_origem)
    
    return base_origem, numero, base_destino

def main():
    base_origem, numero, base_destino = exibir_menu()
    
    resultado = ""
    
    if (base_origem == '3' and base_destino == '1'):
        resultado = hexadecimal_para_binario(numero)
         
    bases = {'1': "Binária", '2': "Decimal", '3': "Hexadecimal"}
        
    print(f"\nBase de origem....: {bases[base_origem]}\nNúmero............: {numero}\nBase de destino...: {bases[base_destino]}")
    print(f"Resultado.........: {resultado}")
    
    print("\n========================================================================\n")
    

if __name__ == "__main__":
    main()