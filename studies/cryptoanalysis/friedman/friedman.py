from coincidence import index_of_coincidence, index_of_coincidence_avg
from vigenere import encrypt, decrypt


def main():
    while True:
        opt = input('0 - Индекс совпадения\n'
                    '1 - Средний индекс совпадения\n'
                    '2 - Шифровать\n'
                    '3 - Расшифровать\n'
                    '4 - Сдвиг\n')

        if opt == '0':
            index_of_coincidence()
        elif opt == '1':
            print(f'{index_of_coincidence_avg():.3f}')
        elif opt == '2':
            print(encrypt())
        elif opt == '3':
            print(decrypt())
        else:
            break
    # print(index_of_coincidence('bbcdf', 'abcdef'))
    # print(index_of_coincidence_avg('the', 'thf'))


if __name__ == '__main__':
    main()
