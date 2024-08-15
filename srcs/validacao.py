# Funções de validação do input do usuario ficam aqui

def validar_numero(numero, base_origem):
    if (base_origem == '1'):             # binario aceitar só 0 e 1
        for char in numero:
            if char not in '01':
                return False
            
    elif (base_origem == '2'):           # decimal aceitar só dígitos de 0 a 9
        return numero.isdigit()
    
    elif (base_origem == '3'):           # hexadecimal aceitar dígitos de 0-9 e letras de A-F (maiúsculas e minúsculas)
        for char in numero:
            if char not in '0123456789ABCDEFabcdef':
                return False
            
    return True