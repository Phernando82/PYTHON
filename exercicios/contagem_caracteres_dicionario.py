def contar_caracteres(s):
    """Função que conta os caracteres de uma string'

   Ex:

   >>> contar_caracteres('fernando')
   {'a': 1, 'd': 1, 'e': 1,'f': 1, 'n': 2, 'o': 1, 'r': 1}

   >>> contar_caracteres('banana')
   {'a': 3, 'b': 1, 'n': 2}

   :param s: string a ser contada

   """
    caracteres_ordenados = sorted(s)

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('fernando'))
    print()
    print(contar_caracteres('banana'))
