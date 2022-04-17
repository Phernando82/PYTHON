def contar_caracteres(s):
    """Função que conta os caracteres de uma string'

   Ex:

   >>> contar_caracteres('fernando')
   a: 1
   d: 1
   e: 1
   f: 1
   n: 2
   o: 1
   r: 1
   >>> contar_caracteres('banana')
   a: 3
   b: 1
   n: 2

   :param s: string a ser contada

   """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:  # começa do 1 e vai até o final
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('fernando')
    print()
    contar_caracteres('banana')
