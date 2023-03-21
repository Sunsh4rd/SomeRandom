from random import choice, randint
from elliptic import pp, gen_curve

from cryptography.fernet import Fernet


def is_on_curve(x, y, a, p):
    return pow(y, 2, p) == (pow(x, 3, p) + a*x) % p


def main():
    iteration = 0
    while True:
        opt = input('0 - Генерация кривой\n'
                    + '1 - Генерация ключей\n'
                    + '2 - Выбор k\n'
                    + '3 - Вычислить k\'\n'
                    + '4 - Вычислить точку R = kP\n'
                    + '5 - Сгенерировать случайный ключ шифрования z\n'
                    + '6 - Зашифровать точку R на ключе z\n'
                    + '7 - Сгенерировать случайный бит i\n'
                    + '8 - Передача по каналам\n'
                    + '9 - Проверить, что точка R лежит на кривой и имеет порядок r\n'
                    + '10 - Проверить что R = kP или R = k\'Q\n'
                    + 'e - Выход из протокола\n')
        if opt == '0':
            p, a, q, r = gen_curve()
            print(p, a, q, r)
            with open('zkp_params/curve.txt', 'w', encoding='utf-8') as curvew:
                curvew.write(f'{p}\n{a}\n{q}\n{r}')
        elif opt == '1':
            with open('zkp_params/curve.txt', 'r', encoding='utf-8') as curver:
                p, a, q, r = curver.read().split('\n')
                p = int(p)
                a = int(a)
                q = tuple(int(x) for x in q[1:-1].split(','))
                r = int(r)
            l = int(input('l = '))
            _p = (q[0], q[1])
            print('1 _p', _p)
            for i in range(l-1):
                np = pp(*_p, q[0], q[1], a, p)
                _p = (np[0], np[1])
                print(f'{i+2} _p', _p)
            with open('zkp_params/prover_key.txt', 'w', encoding='utf-8') as prvw:
                prvw.write(f'{q}\n{_p}\n{r}\n{a}\n{p}\n{l}')
            with open('zkp_params/verifier_key.txt', 'w', encoding='utf-8') as vrfw:
                vrfw.write(f'{q}\n{_p}\n{r}\n{a}\n{p}')

        elif opt == '2':
            with open('zkp_params/prover_key.txt', 'r', encoding='utf-8') as prvr:
                q, _p, r, a, p, l = prvr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                l = int(l)
                print(q, _p, r, l)
            k = randint(1, r-1)
            with open('zkp_params/k.txt', 'w', encoding='utf-8') as kw:
                kw.write(f'{k}')
        elif opt == '3':
            with open('zkp_params/prover_key.txt', 'r', encoding='utf-8') as prvr:
                q, _p, r, a, p, l = prvr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                l = int(l)
                print(q, _p, r, l)
            with open('zkp_params/k.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            k1 = (l*k) % r
            with open('zkp_params/k\'.txt', 'w', encoding='utf-8') as k1w:
                k1w.write(f'{k1}')
        elif opt == '4':
            with open('zkp_params/prover_key.txt', 'r', encoding='utf-8') as prvr:
                q, _p, r, a, p, l = prvr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                l = int(l)
                print(q, _p, r, l)
            if not is_on_curve(*_p, a, p):
                print('Точка P не принадлежит кривой')
                exit()
            with open('zkp_params/k.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            R = (_p[0], _p[1])
            print('1 R', R)
            for i in range(k-1):
                np = pp(*R, *_p, a, p)
                R = (np[0], np[1])
                print(f'{i+2} R', R)
            with open('zkp_params/R.txt', 'w', encoding='utf-8') as Rw:
                Rw.write(f'{R}')
        elif opt == '5':
            z = Fernet.generate_key()
            with open('zkp_params/z.txt', 'w', encoding='utf-8') as zw:
                zw.write(str(z))
        elif opt == '6':
            with open('zkp_params/prover_key.txt', 'r', encoding='utf-8') as prvr:
                q, _p, r, a, p, l = prvr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                l = int(l)
                print(q, _p, r, l)
            with open('zkp_params/R.txt', 'r', encoding='utf-8') as Rr:
                R = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            with open('zkp_params/R.txt', 'rb') as Rcr:
                Rc = Rcr.read()
            if not is_on_curve(*R, a, p):
                print('Точка R не принадлежит кривой')
                exit()
            with open('zkp_params/z.txt', 'rb') as zr:
                z = zr.read()[2:-1]
            ct = Fernet(z).encrypt(Rc)
            with open('zkp_params/e(R).txt', 'w', encoding='utf-8') as eRw:
                eRw.write(str(ct))
        elif opt == '7':
            i = choice([0, 1])
            with open('zkp_params/i.txt', 'w', encoding='utf-8') as iw:
                iw.write(f'{i}')
        elif opt == '8':
            with open('zkp_params/i.txt', 'r', encoding='utf-8') as ir:
                i = int(ir.read())
            with open('zkp_params/k.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            with open('zkp_params/k\'.txt', 'r', encoding='utf-8') as k1r:
                k1 = int(k1r.read())
            with open('zkp_params/z.txt', 'rb') as zr:
                z = zr.read()[2:-1]
            if i == 0:
                with open('zkp_params/c0.txt', 'w', encoding='utf-8') as c0w:
                    c0w.write(str(z)+f'\n{k}')
                with open('zkp_params/c1.txt', 'w', encoding='utf-8') as c1w:
                    c1w.write(str(z)+f'\n{k1}')
            else:
                with open('zkp_params/c0.txt', 'w', encoding='utf-8') as c0w:
                    c0w.write(str(z)+f'\n{k1}')
                with open('zkp_params/c1.txt', 'w', encoding='utf-8') as c1w:
                    c1w.write(str(z)+f'\n{k}')
        elif opt == '9':
            with open('zkp_params/verifier_key.txt', 'r', encoding='utf-8') as vrfr:
                q, _p, r, a, p = vrfr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r, p)
            thr = choice([0, 1])
            with open(f'zkp_params/c{thr}.txt', 'r') as cr:
                data = cr.read().split('\n')
                z = data[0][2:-1].encode()
                somek = int(data[1])
            with open(f'zkp_params/e(R).txt', 'rb') as eRr:
                er = eRr.read()[2:-1]
                R = Fernet(z).decrypt(er).decode()
            R = tuple(int(x) for x in R[1:-1].split(','))
            print(R)
            if not is_on_curve(*R, a, p):
                print('Точка R не принадлежит кривой')
                exit()
            _R = (R[0], R[1])
            print(R)
            print('1 _R', _R)
            for it in range(r):
                try:
                    np = pp(*_R, *R, a, p)
                    _R = (np[0], np[1])
                    print(f'{it+2} _R', _R)
                except Exception as e:
                    break
            if it + 2 != r:
                print('Порядок точки R не равен r')
                exit()
            else:
                print('Проверка пройдена')
        elif opt == '10':
            with open('zkp_params/verifier_key.txt', 'r', encoding='utf-8') as vrfr:
                q, _p, r, a, p = vrfr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r, p)
            thr = choice([0, 1])
            with open(f'zkp_params/c{thr}.txt', 'r') as cr:
                data = cr.read().split('\n')
                z = data[0][2:-1].encode()
                somek = int(data[1])
            with open(f'zkp_params/e(R).txt', 'rb') as eRr:
                er = eRr.read()[2:-1]
                R = Fernet(z).decrypt(er).decode()
            R = tuple(int(x) for x in R[1:-1].split(','))
            with open('zkp_params/i.txt', 'r', encoding='utf-8') as ir:
                i = int(ir.read())
            if i == 0 and thr == 0:
                _R = (_p[0], _p[1])
                print(_R)
                print('1 _R', _p)
                for it in range(somek-1):
                    np = pp(*_R, *_p, a, p)
                    _R = (np[0], np[1])
                    print(f'{it+2} _R', _R)
                if R == _R:
                    print('ok1')
                    iteration += 1
                else:
                    print('Ошибка! Выход из протокола!')
                    exit()
            if i == 1 and thr == 0:
                _R = (q[0], q[1])
                print(_R)
                print('1 _R', q)
                for it in range(somek-1):
                    np = pp(*_R, *q, a, p)
                    _R = (np[0], np[1])
                    print(f'{it+2} _R', _R)
                if R == _R:
                    print('ok2')
                    iteration += 1
                else:
                    print('Ошибка! Выход из протокола!')
                    exit()
            if i == 0 and thr == 1:
                _R = (q[0], q[1])
                print(_R)
                print('1 _R', q)
                for it in range(somek-1):
                    np = pp(*_R, *q, a, p)
                    _R = (np[0], np[1])
                    print(f'{it+2} _R', _R)
                if R == _R:
                    print('ok3')
                    iteration += 1
                else:
                    print('Ошибка! Выход из протокола!')
                    exit()
            if i == 1 and thr == 1:
                _R = (_p[0], _p[1])
                print(_R)
                print('1 _R', _p)
                for it in range(somek-1):
                    np = pp(*_R, *_p, a, p)
                    _R = (np[0], np[1])
                    print(f'{it+2} _R', _R)
                if R == _R:
                    print('ok4')
                    iteration += 1
                else:
                    print('Ошибка! Выход из протокола.')
                    exit()
        else:
            print(
                f'Претендент знает логарифм с вероятностью {1 - (1/2)**iteration}')
            break


if __name__ == '__main__':
    main()
