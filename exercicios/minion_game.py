# o programa recebe uma string como entrada e vai testar quantas
# substrings consegue fazer com vogais e quantas consegue fazer com consoantes
# dois competidores, Kevin e Stuart, deve ser apresentado o ganhardor e seu score

import string
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    lista_consonant_stuart = []
    lista_vowel_kevin = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in range(len(string):
        if string[char:char +1] == 'a':
            for c in string[char:len(string)]:
                lista_vowel_kevin.append(string[char:len(string) -1])
                kevin_score += 1
        if char not in vowels:
            for c in string[char:len(string)]:
                lista_consonant_stuart.append(string[char:len(string) -1])
                stuart_score += 1

    if kevin_score < stuart_score:
        print(f'Stuart {stuart_score}')

    if kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')



if __name__ == '__main__':
    print(minion_game('banana'))