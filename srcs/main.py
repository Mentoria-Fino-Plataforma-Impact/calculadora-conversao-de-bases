# Interação com usuário e chama as funções de conversão

def definir_base_destino(b_origem):
    print("\nEscolha a base de destino:\n")
    print("1 - Binário")
    print("2 - Decimal")
    print("3 - Hexadecimal")
    
    bs_destino = input("\nOpção escolhida: ")
    
    while (bs_destino != '1' and bs_destino != '2' and bs_destino != '3' or bs_destino == b_origem):
        if (bs_destino == b_origem):
            print("Opção inválida! A base de destino deve ser diferente da base de origem.")
        else:
            print("Opção inválida!\nEscolha entre as opções 1, 2 ou 3.")
        bs_destino = input("\nOpção escolhida: ")
        
    return bs_destino

def definir_base_origem():
    print("\nEscolha a base de origem:\n")
    print("1 - Binário")
    print("2 - Decimal")
    print("3 - Hexadecimal")
    
    bs_origem = input("\nOpção escolhida: ")
    
    while (bs_origem != '1' and bs_origem != '2' and bs_origem != '3'):
        print("Opção inválida! Escolha entre as opções 1, 2 ou 3.")
        bs_origem = input("\nOpção escolhida: ")
    
    return bs_origem


def exibir_menu():
    print("\n================== CALCULADORA DE CONVERSÃO DE BASES ==================")
    
    base_origem = definir_base_origem()
        
    numero = input("\nNúmero a ser convertido: ")
    
    base_destino = definir_base_destino(base_origem)
    
    return base_origem, numero, base_destino

def main():
    base_origem, numero, base_destino = exibir_menu()
    
    if (base_origem == '1'):
        base_origem = "Binária"
    elif (base_origem == '2'):
        base_origem = "Decimal"
    else:
        base_origem = "Hexadecimal"
        
    if (base_destino == '1'):
        base_destino = "Binária"
    elif (base_destino == '2'):
        base_destino = "Decimal"
    else:
        base_destino = "Hexadecimal"
        
    print(f"\nBase de origem.: {base_origem}\nNúmero.........: {numero}\nBase de destino: {base_destino}")
    
    print("\n========================================================================\n")
    

if __name__ == "__main__":
    main()