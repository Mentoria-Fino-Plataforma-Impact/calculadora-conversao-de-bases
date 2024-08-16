# Funções de conversão ficam aqui:


# binario para decimal


# binario para hexadecimal


# decimal para binario


# decimal para hexadecimal


# hexadecimal para binario
def hexadecimal_para_binario(num_hexadecimal):
    num_binario = ""
    for char in num_hexadecimal:
        resto = int(char, 16)
        binario_str = ""
        while (resto > 0 or len(binario_str) < 4):
            binario_str = str(resto % 2) + binario_str
            resto //= 2
        num_binario += binario_str.zfill(4)
    return num_binario


# hexadecimal para decimal