from gen_key import gen_key
from encrypt import encrypt
from decrypt import decrypt


def main():
    block = [''] * 5
    print(block)
    ts = 'abcde'
    block[0] = ts[4]
    block[2] = ts[1]
    print(block)
    # while True:
    #     opt = input(
    #         '0 - Генерация ключа моноциклической перестановки\n1 - Зашифровать\n2 - Расшифровать\n')
    #     if opt == '0':
    #         n = int(input('Длина перестановки: '))
    #         gen_key(n)
    #     elif opt == '1':
    #         encrypt()
    #     elif opt == '2':
    #         decrypt()
    #     else:
    #         break


if __name__ == '__main__':
    main()
