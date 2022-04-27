"""
Defina uma constante EXPECTED_BAKE_TIME que retorne quantos minutos a lasanha deve assar no forno.
De acordo com o seu livro de receitas, a lasanha deve ficar no forno por 40 minutos:

>>> lasagna.EXPECTED_BAKE_TIME
40

Implemente a função bake_time_remaining() que leva os minutos reais que a lasanha esteve no forno como um argumento
e retorna quantos minutos a lasanha ainda precisa assar com base no EXPECTED_BAKE_TIME.

>>> bake_time_remaining(30)
10

Implemente a função prepare_time_in_minutes() que leva o número de camadas que você deseja adicionar à lasanha como
um argumento e retorna quantos minutos você gastaria para criá-los. Suponha que cada camada leve 2 minutos para preparar..

>>> preparation_time_in_minutes(2)
4

Implemente a função elapsed_time_in_minutes() que possui dois parâmetros: number_of_layers (o número de camadas
adicionadas à lasanha) e elapsed_bake_time (o número de minutos que a lasanha está assando no forno). Esta função
deve retornar o número total de minutos que você está cozinhando, ou a soma do seu tempo de preparo e o tempo que
a lasanha já passou assando no forno.

>>> elapsed_time_in_minutes(3, 20)
26

Volte pela receita, adicionando notas e documentação.

"""


# TODO: define the 'EXPECTED_BAKE_TIME' constant

class Lasagna:
    def __init__(self, EXPECTED_BAKE_TIME = 40):
        self.EXPECTED_BAKE_TIME = EXPECTED_BAKE_TIME


lasagna = Lasagna()

lasagna.EXPECTED_BAKE_TIME


# # TODO: define the 'bake_time_remaining()' function

def bake_time_remaining(min):
    btr = 40 - min
    return btr

bake_time_remaining(30)


# # TODO: consider defining the 'PREPARATION_TIME' constant
# #       equal to the time it takes to prepare a single layer

def preparation_time_in_minutes(layers):
    ptim = layers * 2
    return ptim

preparation_time_in_minutes(2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    number_of_layers *= 2
    etim = number_of_layers + elapsed_bake_time
    return etim

elapsed_time_in_minutes(3, 20)


