def ceasar(message, rot):
    alph_s = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    n = len(alph_s)
    alph = {alph_s[i]: i for i in range(len(alph_s))}
    # print(alph)
    return ''.join(alph_s[(i+rot) % n] for i in [alph[j] for j in message])


def main():
    # alph_s = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    # alph = {alph_s[i]: i for i in range(len(alph_s))}
    # n = len(alph)
    # print(alph)
    # ciphertetxt = 'ШМЦШЛЙЩКСЫЗЮЭЫЩОМНИРЪЙЫЯЖЖЖОМЛПЬХВЛ'.lower()
    # print(len(ciphertetxt))
    # key_part = 'ключшМЦШЛЙЩКСЫЗЮЭЫЩОМНИРЪЙЫЯЖЖЖОМЛП'.lower()
    # print(len(key_part))    
    # dc = ''
    # for i in range(len(ciphertetxt)):
    #     dc += alph_s[((alph[ciphertetxt[i]] - alph[key_part[i]])%n)-1]
    # print(dc)

    text = 'жтьхршхршжтьщлчш'

    'житьхорошохорошожитьещелучше'
    

    for i in range(32):
        print(ceasar(text, i))


if __name__ == '__main__':
    main()
