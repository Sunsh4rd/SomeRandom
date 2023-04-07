from gen_key import gen_key
from encrypt import encrypt
from decrypt import decrypt
from kasiski_test import kasiski
from brute import brute


def main():
    while True:
        opt = input(
            '0 - Генерация ключа моноциклической перестановки\n1 - Зашифровать\n2 - Расшифровать\n3 - Тест Казиски\n4 - Перебор перестановок\n')
        if opt == '0':
            n = int(input('Длина перестановки: '))
            gen_key(n)
        elif opt == '1':
            encrypt()
        elif opt == '2':
            decrypt()
            with open('params/message.txt', 'r', encoding='utf-8') as m:
                msg = m.read()
            with open('params/deciphertext.txt', 'r', encoding='utf-8') as d:
                dec = d.read()
            print('all correct' if msg == dec else 'not')
        elif opt == '3':
            kasiski()
        elif opt == '4':
            brute()
        else:
            break


if __name__ == '__main__':
    main()
