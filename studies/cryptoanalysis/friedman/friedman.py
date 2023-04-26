from coincidence import index_of_coincidence, index_of_coincidence_avg
from vigenere import encrypt, decrypt, shift


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
            index_of_coincidence_avg()
        elif opt == '2':
            print(encrypt())
        elif opt == '3':
            print(decrypt())
        elif opt == '4':
            shift()
        else:
            break


if __name__ == '__main__':
    main()
