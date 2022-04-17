# O programa deve colocar em letra maiuscula a primeira letra
# de um nomeex:
# entrada: 'fernando peres valverde'
# saida: 'Fernando Peres Valverde'
# observando numeros:
#
# entrada: 'a df g j t r e esd 3ab'
# saída: A Df G J T R E Esd 3ab


def solve(s):
    nome = ''
    space = True

    for caracter in s:
        if caracter == ' ':
            nome = nome + caracter
            space = True
        elif space:            
            nome = nome + caracter.capitalize()
            space = False
        elif caracter != ' ':
            nome = nome + caracter
            space = False

    return nome


s = input('Digite o seu nome:')

if __name__ == '__main__':
    print(solve(s))


#solução do Greidimar

# frase = " a d f e r g 3ab"
# espaco = bool(True)
# nova_frase_maiuscula = ""
#
# for letras in range(len(frase)):
#     print(frase[letras:letras+1])
#
#     if espaco:
#         nova_frase_maiuscula = nova_frase_maiuscula + frase[letras:letras + 1].upper()
#         espaco = False
#     else:
#         nova_frase_maiuscula = nova_frase_maiuscula + frase[letras:letras + 1]
#
#
#     if frase[letras:letras+1] == " ":
#         espaco = True
#     else:
#         espaco = False
#
#
#
# print (" Nova frase: ", nova_frase_maiuscula)