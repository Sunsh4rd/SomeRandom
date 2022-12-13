from random import randint
from elliptic import pp, gen_curve


def is_on_curve(x, y, a, p):
    return pow(y, 2, p) == (pow(x, 3, p) + a*x) % p


def f(p, r):
    return p[0] % r


def main():
    while True:
        opt = input('0 - Задать секретный ключ\n'
                    + '1 - Генерация кривой\n'
                    + '2 - Генерация открытого ключа\n'
                    + '3 - Выбрать случайное k\n'
                    + '4 - Вычислить R = kQ\n'
                    + '5 - Вычислить h(M)\n'
                    + '6 - Найти s из h(m)=lf(R) + ks(mod r)\n'
                    + '7 - Вычислисть h(m)Q\n'
                    + '8 - Вычислисть f(R)P\n'
                    + '9 - Вычислисть sR\n'
                    + '10 - Проверить равенство h(m)Q = f(R)P + sR\n')
        if opt == '0':
            l = int(input('Секретный ключ l = '))
            with open('elgamal_params/private_key.txt', 'w', encoding='utf-8') as privkw:
                privkw.write(f'{l}')
        elif opt == '1':
            p, a, q, r = gen_curve()
            print(p, a, q, r)
            with open('elgamal_params/curve.txt', 'w', encoding='utf-8') as curvew:
                curvew.write(f'{p}\n{a}\n{q}\n{r}')
        elif opt == '2':
            with open('elgamal_params/curve.txt', 'r', encoding='utf-8') as curver:
                p, a, q, r = curver.read().split('\n')
                p = int(p)
                a = int(a)
                q = tuple(int(x) for x in q[1:-1].split(','))
                r = int(r)
            eq = f'y**2 = x**3 + {a}*x'
            print(eq)
            # a = 3
            # r = 73
            # p = 137
            # q = (30, 52)
            with open('elgamal_params/private_key.txt', 'r', encoding='utf-8') as privkr:
                l = int(privkr.read())
            _p = (q[0], q[1])
            print('1 _p', _p)
            for i in range(l-1):
                np = pp(*_p, q[0], q[1], a, p)
                _p = (np[0], np[1])
                print(f'{i+2} _p', _p)
            with open('elgamal_params/public_key.txt', 'w', encoding='utf-8') as pubkw:
                pubkw.write(f'{eq}\n{q}\n{_p}\n{r}\n{a}\n{p}')
        elif opt == '3':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            k = randint(1, r-1)
            with open('elgamal_params/k.txt', 'w', encoding='utf-8') as kw:
                kw.write(f'{k}')
        elif opt == '4':
            with open('elgamal_params/k.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            _r = (q[0], q[1])
            print('1 _r', _r)
            for i in range(k-1):
                np = pp(*_r, *q, a, p)
                _r = (np[0], np[1])
                print(f'{i+2} _r', _r)
            print('Точка не принадлежит кривой' if not is_on_curve(*_r, a, p) else '')
            if f(_r, r) % r == 0:
                print('Повторите шаги 3-4 т.к. f(R) mod r = 0!!!!')
            else:
                with open('elgamal_params/R.txt', 'w', encoding='utf-8') as Rw:
                    Rw.write(f'{_r}')
        elif opt == '5':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('elgamal_params/message.txt', 'r', encoding='utf-8') as msgr:
                message = msgr.read()
                print(message)
                hm = int.from_bytes(message.encode(), byteorder='big') % r
                print(hm)
            with open('elgamal_params/hm.txt', 'w', encoding='utf-8') as hmw:
                hmw.write(str(hm))
        elif opt == '6':
            with open('elgamal_params/private_key.txt', 'r', encoding='utf-8') as privkr:
                l = int(privkr.read())
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('elgamal_params/hm.txt', 'r', encoding='utf-8') as hmr:
                hm = int(hmr.read())
                print(hm)
            with open('elgamal_params/k.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
                print(k)
            with open('elgamal_params/R.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
                print(_r)
            s = ((hm-l*f(_r, r)) % r * pow(k, -1, r)) % r
            print(s)
            with open('elgamal_params/s.txt', 'w', encoding='utf-8') as sw:
                sw.write(f'{s}')
            with open('elgamal_params/message.txt', 'r', encoding='utf-8') as msgr:
                message = msgr.read()
                print(message)
            with open('elgamal_params/signature.txt', 'w', encoding='utf-8') as sigw:
                sigw.write(f'{message} {_r} {s}')
        elif opt == '7':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
            _q = (q[0], q[1])
            with open('elgamal_params/hm.txt', 'r', encoding='utf-8') as hmr:
                hm = int(hmr.read())
                print(hm)
            print('1 _q', _q)
            for i in range(hm-1):
                np = pp(*_q, q[0], q[1], a, p)
                _q = (np[0], np[1])
                print(f'{i+2} _q', _q)
            print('Точка не принадлежит кривой' if not is_on_curve(*_q, a, p) else '')
            with open('elgamal_params/h(m)Q.txt', 'w', encoding='utf-8') as hmqw:
                hmqw.write(f'{_q}')
        elif opt == '8':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
            __p = (_p[0], _p[1])
            with open('elgamal_params/R.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
                print(_r)
            if not is_on_curve(*_r,a,p):
                print('Точка R не принадлежит кривой, повторите предыдущие шаги')
                exit()
            print('1 __p', __p)
            for i in range(f(_r, r)-1):
                np = pp(*__p, _p[0], _p[1], a, p)
                __p = (np[0], np[1])
                print(f'{i+2} __p', __p)
            print('Точка не принадлежит кривой' if not is_on_curve(
                *__p, a, p) else '')
            with open('elgamal_params/f(R)P.txt', 'w', encoding='utf-8') as frpw:
                frpw.write(f'{__p}')
        elif opt == '9':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
            with open('elgamal_params/R.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
                print(_r)
            if not is_on_curve(*_r,a,p):
                print('Точка R не принадлежит кривой, повторите предыдущие шаги')
                exit()
            __r = (_r[0], _r[1])
            print('1 __r', __r)
            with open('elgamal_params/s.txt', 'r', encoding='utf-8') as sr:
                s = int(sr.read())
                print(s)
            for i in range(s-1):
                np = pp(*__r, _r[0], _r[1], a, p)
                __r = (np[0], np[1])
                print(f'{i+2} __r', __r)
            print('Точка не принадлежит кривой' if not is_on_curve(
                *__r, a, p) else '')
            with open('elgamal_params/sR.txt', 'w', encoding='utf-8') as sRw:
                sRw.write(f'{__r}')
        elif opt == '10':
            with open('elgamal_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
            with open('elgamal_params/h(m)Q.txt', 'r', encoding='utf-8') as hmqr:
                hmq = tuple(int(x) for x in hmqr.read()[1:-1].split(','))
            with open('elgamal_params/f(R)P.txt', 'r', encoding='utf-8') as frpr:
                frp = tuple(int(x) for x in frpr.read()[1:-1].split(','))
            with open('elgamal_params/sR.txt', 'r', encoding='utf-8') as sr:
                sr = tuple(int(x) for x in sr.read()[1:-1].split(','))
            print('Подпись верна' if hmq == pp(
                *frp, *sr, a, p) else 'Подпись неверна')
        else:
            break
        # elif opt =='1':
        #     with open('elgamal_params/public_key.txt','r',encoding='utf-8') as pubkr:
        #         _,q,_p,r,a,p = pubkr.read().split('\n')
        #         q = tuple(int(x) for x in q[1:-1].split(','))
        #         _p = tuple(int(x) for x in _p[1:-1].split(','))
        #         r = int(r)
        #         a = int(a)
        #         p = int(p)
        #         print(q,_p,r)
        #     with open('elgamal_params/message.txt','r',encoding='utf-8') as msgr:
        #         message = msgr.read()
        #         print(message)
        #         hm = int.from_bytes(message.encode(), byteorder='big') %r
        #         print(hm)
        #     with open('elgamal_params/hm.txt','w',encoding='utf-8') as hmw:
        #         hmw.write(str(hm))
        # elif opt =='2':
        #     with open('elgamal_params/private_key.txt','r',encoding='utf-8') as privkr:
        #         l = int(privkr.read())
        #     with open('elgamal_params/public_key.txt','r',encoding='utf-8') as pubkr:
        #         _,q,_p,r,a,p = pubkr.read().split('\n')
        #         q = tuple(int(x) for x in q[1:-1].split(','))
        #         _p = tuple(int(x) for x in _p[1:-1].split(','))
        #         r = int(r)
        #         a = int(a)
        #         p = int(p)
        #         print(q,_p,r)
        #     with open('elgamal_params/hm.txt','r',encoding='utf-8') as hmr:
        #         hm = int(hmr.read())
        #         print(hm)
        #     while True:
        #         k = randint(1, r-1)
        #         print('k', k)
        #         print(pow(k, -1, r))
        #         _r = (q[0], q[1])
        #         print('1 _r', _r)
        #         for i in range(k-1):
        #             np = pp(*_r, *q, a, p)
        #             _r = (np[0], np[1])
        #             print(f'{i+2} _r', _r)
        #         if f(_r, r) % r != 0:
        #             s = ((hm-l*f(_r, r)) % r * pow(k, -1, r)) % r
        #             print(s)
        #             break
        #     with open('elgamal_params/s.txt','w',encoding='utf-8') as sw:
        #         sw.write(str(s))
        #     with open('elgamal_params/message.txt','r',encoding='utf-8') as msgr:
        #         message = msgr.read()
        #         print(message)
        #     with open('elgamal_params/signature.txt','w',encoding='utf-8') as sigw:
        #         sigw.write(f'{message} {_r} {s}')
        # elif opt == '3':
        #     pass

    # print('sign:')

    # signed = (message, _r, s)
    # print(signed)
    # print('check:')
    # print(is_on_curve(*_r, a, p))
    # _q = (q[0], q[1])
    # print('1 _q', _q)
    # for i in range(hm-1):
    #     np = pp(*_q, q[0], q[1], a, p)
    #     _q = (np[0], np[1])
    #     print(f'{i+2} _q', _q)
    # __p = (_p[0], _p[1])
    # print('1 __p', __p)
    # for i in range(f(_r, r)-1):
    #     np = pp(*__p, _p[0], _p[1], a, p)
    #     __p = (np[0], np[1])
    #     print(f'{i+2} __p', __p)
    # __r = (_r[0], _r[1])
    # print('1 __r', __r)
    # for i in range(s-1):
    #     np = pp(*__r, _r[0], _r[1], a, p)
    #     __r = (np[0], np[1])
    #     print(f'{i+2} __r', __r)

    # print(_q, __p, __r)
    # print(pp(*__p, *__r, a, p))
    # print(hm)
    # print(_q == pp(*__p, *__r, a, p))


if __name__ == '__main__':
    main()
