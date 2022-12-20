from random import randint
from elliptic import pp, gen_curve


def is_on_curve(x, y, a, p):
    return pow(y, 2, p) == (pow(x, 3, p) + a*x) % p


def f(p, r):
    return p[0] % r


def main():
    while True:
        opt = input('0 - Генерация кривой\n'
                    + '1 - Генерация ключей\n'
                    + '2 - Выбор показателя k\'\n'
                    + '3 - Вычислить R\' = k\'Q\n'
                    + '4 - Проверить, что R\' принадлежит кривой\n'
                    + '5 - Выбрать показатель alpha\n'
                    + '6 - Вычислить R = alpha*R\'\n'
                    + '7 - Вычислить beta = f(R)*f(R\')^-1(mod r)\n'
                    + '8 - Наложить маску m\' = alpha*beta^-1*m(mod r)\n'
                    + '9 - Проверить, что m\' != 0\n'
                    + '10 - Вычислить l(f(R\'))\n'
                    + '11 - Вычислить k\'m\'\n'
                    + '12 - Вычислить s\' = lf(R\') + k\'m\' (mod r)\n'
                    + '13 - Вычислить s\'Q\n'
                    + '14 - Вычислить f(R\')P\n'
                    + '15 - Вычислить m\'R\'\n'
                    + '16 - Проверить s\'Q = f(R\')P + m\'R\'\n'
                    + '17 - Проверить m != 0\n'
                    + '18 - Проверить f(R) != 0\n'
                    + '19 - Вычислить sQ\n'
                    + '20 - Вычислить f(R)P\n'
                    + '21 - Вычислить mR\n'
                    + '22 - Проверить sQ = f(R)P + mR\n')
        if opt == '0':
            p, a, q, r = gen_curve()
            print(p, a, q, r)
            with open('money_params/curve.txt', 'w', encoding='utf-8') as curvew:
                curvew.write(f'{p}\n{a}\n{q}\n{r}')
        elif opt == '1':
            with open('money_params/curve.txt', 'r', encoding='utf-8') as curver:
                p, a, q, r = curver.read().split('\n')
                p = int(p)
                a = int(a)
                q = tuple(int(x) for x in q[1:-1].split(','))
                r = int(r)
            eq = f'y**2 = x**3 + {a}*x'
            print(eq)
            l = int(input('Секретный ключ l = '))
            _p = (q[0], q[1])
            print('1 _p', _p)
            for i in range(l-1):
                np = pp(*_p, q[0], q[1], a, p)
                _p = (np[0], np[1])
                print(f'{i+2} _p', _p)
            with open('money_params/public_key.txt', 'w', encoding='utf-8') as pubkw:
                pubkw.write(f'{eq}\n{q}\n{_p}\n{r}\n{a}\n{p}')
            with open('money_params/private_key.txt', 'w', encoding='utf-8') as privkw:
                privkw.write(f'{l}')
        elif opt == '2':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            k = randint(1, r-1)
            if not is_on_curve(*q, a, p):
                print('Точка Q не принадлежит кривой')
                exit()
            with open('money_params/k\'.txt', 'w', encoding='utf-8') as kw:
                kw.write(f'{k}')
        elif opt == '3':
            with open('money_params/k\'.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            if not is_on_curve(*q, a, p):
                print('Точка Q не принадлежит кривой')
                exit()
            _r = (q[0], q[1])
            print('1 _r', _r)
            for i in range(k-1):
                np = pp(*_r, *q, a, p)
                _r = (np[0], np[1])
                print(f'{i+2} _r', _r)
            print('Точка не принадлежит кривой' if not is_on_curve(*_r, a, p) else '')
            if f(_r, r) % r == 0:
                print('Повторите шаги 2-3 т.к. f(R\') mod r = 0!!!!')
            else:
                with open('money_params/R\'.txt', 'w', encoding='utf-8') as Rw:
                    Rw.write(f'{_r}')
        elif opt == '4':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
        elif opt == '5':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            alpha = randint(1, r-1)
            with open('money_params/alpha.txt', 'w', encoding='utf-8') as alphaw:
                alphaw.write(f'{alpha}')
        elif opt == '6':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
            __r = (_r[0], _r[1])
            print('1 __r', __r)
            with open('money_params/alpha.txt', 'r', encoding='utf-8') as alphar:
                alpha = int(alphar.read())
                print(alpha)
            for i in range(alpha-1):
                np = pp(*__r, _r[0], _r[1], a, p)
                __r = (np[0], np[1])
                print(f'{i+2} __r', __r)
            if f(__r, r) % r == 0:
                print('Повторите шаги 5-6 т.к. f(R) mod r = 0!!!!')
            else:
                with open('money_params/R.txt', 'w', encoding='utf-8') as _Rw:
                    _Rw.write(f'{__r}')
        elif opt == '7':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
            with open('money_params/R.txt', 'r', encoding='utf-8') as _Rr:
                __r = tuple(int(x) for x in _Rr.read()[1:-1].split(','))
            if not is_on_curve(*__r, a, p):
                print('Точка R не принадлежит кривой')
                exit()
            beta = (f(__r, r) % r * pow(f(_r, r), -1, r)) % r
            with open('money_params/beta.txt', 'w', encoding='utf-8') as betaw:
                betaw.write(f'{beta}')
        elif opt == '8':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/alpha.txt', 'r', encoding='utf-8') as alphar:
                alpha = int(alphar.read())
            with open('money_params/beta.txt', 'r', encoding='utf-8') as betar:
                beta = int(betar.read())
            with open('money_params/m.txt', 'r', encoding='utf-8') as msgr:
                message = msgr.read()
                print(message)
                m = int.from_bytes(message.encode(), byteorder='big') % r
                print(m)
            m1 = (alpha * pow(beta, -1, r) * m) % r
            with open('money_params/m\'.txt', 'w', encoding='utf-8') as m1w:
                m1w.write(f'{m1}')
        elif opt == '9':
            with open('money_params/m\'.txt', 'r', encoding='utf-8') as m1r:
                m1 = int(m1r.read())
            if m1 == 0:
                print('m\' = 0')
                exit()
        elif opt == '10':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/private_key.txt', 'r', encoding='utf-8') as privkr:
                l = int(privkr.read())
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
            lfr = (l * f(_r, r)) % r
            with open('money_params/lf(R\').txt', 'w', encoding='utf-8') as lfrw:
                lfrw.write(f'{lfr}')
        elif opt == '11':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/k\'.txt', 'r', encoding='utf-8') as kr:
                k = int(kr.read())
            with open('money_params/m\'.txt', 'r', encoding='utf-8') as m1r:
                m1 = int(m1r.read())
            km1 = (k*m1) % r
            with open('money_params/k\'m\'.txt', 'w', encoding='utf-8') as km1w:
                km1w.write(f'{km1}')
        elif opt == '12':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/lf(R\').txt', 'r', encoding='utf-8') as lfrr:
                lfr = int(lfrr.read())
            with open('money_params/k\'m\'.txt', 'r', encoding='utf-8') as km1r:
                km1 = int(km1r.read())
            s = (lfr + km1) % r
            with open('money_params/s\'.txt', 'w', encoding='utf-8') as sw:
                sw.write(f'{s}')
        elif opt == '13':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            if not is_on_curve(*q, a, p):
                print('Точка Q не принадлежит кривой')
                exit()
            with open('money_params/s\'.txt', 'r', encoding='utf-8') as sr:
                s = int(sr.read())
            sq = (q[0], q[1])
            print('1 sq', sq)
            for i in range(s-1):
                np = pp(*sq, *q, a, p)
                sq = (np[0], np[1])
                print(f'{i+2} sq', sq)
            with open('money_params/s\'Q.txt', 'w', encoding='utf-8') as sQw:
                sQw.write(f'{sq}')
        elif opt == '14':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
            if not is_on_curve(*_p, a, p):
                print('Точка P не принадлежит кривой')
                exit()
            frp = (_p[0], _p[1])
            print('1 frp', frp)
            for i in range(f(_r, r)-1):
                np = pp(*frp, *_p, a, p)
                frp = (np[0], np[1])
                print(f'{i+2} frp', frp)
            with open('money_params/f(R\')P.txt', 'w', encoding='utf-8') as fRPw:
                fRPw.write(f'{frp}')
        elif opt == '15':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/R\'.txt', 'r', encoding='utf-8') as Rr:
                _r = tuple(int(x) for x in Rr.read()[1:-1].split(','))
            if not is_on_curve(*_r, a, p):
                print('Точка R\' не принадлежит кривой')
                exit()
            with open('money_params/m\'.txt', 'r', encoding='utf-8') as m1r:
                m1 = int(m1r.read())
            m1r = (_r[0], _r[1])
            print('1 m1r', m1r)
            for i in range(m1-1):
                np = pp(*m1r, *_r, a, p)
                m1r = (np[0], np[1])
                print(f'{i+2} m1r', m1r)
            with open('money_params/m\'R\'.txt', 'w', encoding='utf-8') as mRw:
                mRw.write(f'{m1r}')
        elif opt == '16':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/s\'Q.txt', 'r', encoding='utf-8') as sQr:
                sq = tuple(int(x) for x in sQr.read()[1:-1].split(','))
            with open('money_params/f(R\')P.txt', 'r', encoding='utf-8') as frpr:
                frp = tuple(int(x) for x in frpr.read()[1:-1].split(','))
            with open('money_params/m\'R\'.txt', 'r', encoding='utf-8') as mrr:
                mr = tuple(int(x) for x in mrr.read()[1:-1].split(','))
            if not is_on_curve(*sq, a, p):
                print('Точка s\'Q не принадлежит кривой')
                exit()
            if not is_on_curve(*frp, a, p):
                print('Точка f(R\')P не принадлежит кривой')
                exit()
            if not is_on_curve(*mr, a, p):
                print('Точка m\'R\' не принадлежит кривой')
                exit()
            if sq == pp(*frp, *mr, a, p):
                print('Равенство выполняется')
                with open('money_params/s\'.txt', 'r', encoding='utf-8') as sr:
                    s1 = int(sr.read())
                with open('money_params/beta.txt', 'r', encoding='utf-8') as betar:
                    beta = int(betar.read())
                s = (s1*beta) % r
                with open('money_params/s.txt', 'w', encoding='utf-8') as sw:
                    sw.write(f'{s}')
                with open('money_params/m.txt', 'r', encoding='utf-8') as mmr:
                    mm = mmr.read()
                with open('money_params/R.txt', 'r', encoding='utf-8') as Rpr:
                    R = tuple(int(x) for x in Rpr.read()[1:-1].split(','))
                with open('money_params/coin.txt', 'w', encoding='utf-8') as coinw:
                    coinw.write(f'{mm}\n{R}\n{s}')
            else:
                print('Подпись недействительна')
                exit()
        elif opt == '17':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/coin.txt', 'r', encoding='utf-8') as coinr:
                m, R, s = coinr.read().split('\n')
                m = int.from_bytes(m.encode(), byteorder='big') % r
                R = tuple(int(x) for x in R[1:-1].split(','))
                s = int(s)
            if m != 0:
                print('Неравенство выполняется')
            else:
                print('Подпись s недействительна')
                exit()
        elif opt == '18':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/coin.txt', 'r', encoding='utf-8') as coinr:
                m, R, s = coinr.read().split('\n')
                m = int.from_bytes(m.encode(), byteorder='big') % r
                R = tuple(int(x) for x in R[1:-1].split(','))
                s = int(s)
            if not is_on_curve(*R, a, p):
                print('Точка Q не принадлежит кривой')
                exit()
            if f(R, r) != 0:
                print('Неравенство выполняется')
            else:
                print('Подпись s недействительна')
                exit()
        elif opt == '19':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            if not is_on_curve(*q, a, p):
                print('Точка Q не принадлежит кривой')
                exit()
            with open('money_params/coin.txt', 'r', encoding='utf-8') as coinr:
                m, R, s = coinr.read().split('\n')
                m = int.from_bytes(m.encode(), byteorder='big') % r
                R = tuple(int(x) for x in R[1:-1].split(','))
                s = int(s)
            sq = (q[0], q[1])
            print('1 sq', sq)
            for i in range(s-1):
                np = pp(*sq, *q, a, p)
                sq = (np[0], np[1])
                print(f'{i+2} sq', sq)
            with open('money_params/sQ.txt', 'w', encoding='utf-8') as sQw:
                sQw.write(f'{sq}')
        elif opt == '20':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/coin.txt', 'r', encoding='utf-8') as coinr:
                m, R, s = coinr.read().split('\n')
                m = int.from_bytes(m.encode(), byteorder='big') % r
                R = tuple(int(x) for x in R[1:-1].split(','))
                s = int(s)
            if not is_on_curve(*R, a, p):
                print('Точка R не принадлежит кривой')
                exit()
            if not is_on_curve(*_p, a, p):
                print('Точка P не принадлежит кривой')
                exit()
            frp = (_p[0], _p[1])
            print('1 frp', frp)
            for i in range(f(R, r)-1):
                np = pp(*frp, *_p, a, p)
                frp = (np[0], np[1])
                print(f'{i+2} frp', frp)
            with open('money_params/f(R)P.txt', 'w', encoding='utf-8') as fRPw:
                fRPw.write(f'{frp}')
        elif opt == '21':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/coin.txt', 'r', encoding='utf-8') as coinr:
                m, R, s = coinr.read().split('\n')
                m = int.from_bytes(m.encode(), byteorder='big') % r
                R = tuple(int(x) for x in R[1:-1].split(','))
                s = int(s)
            if not is_on_curve(*R, a, p):
                print('Точка R не принадлежит кривой')
                exit()
            mR = (R[0], R[1])
            print('1 mR', mR)
            for i in range(m-1):
                np = pp(*mR, *R, a, p)
                mR = (np[0], np[1])
                print(f'{i+2} mR', mR)
            with open('money_params/mR.txt', 'w', encoding='utf-8') as mRw:
                mRw.write(f'{mR}')
        elif opt == '22':
            with open('money_params/public_key.txt', 'r', encoding='utf-8') as pubkr:
                _, q, _p, r, a, p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q, _p, r)
            with open('money_params/sQ.txt', 'r', encoding='utf-8') as sQr:
                sq = tuple(int(x) for x in sQr.read()[1:-1].split(','))
            with open('money_params/f(R)P.txt', 'r', encoding='utf-8') as frpr:
                frp = tuple(int(x) for x in frpr.read()[1:-1].split(','))
            with open('money_params/mR.txt', 'r', encoding='utf-8') as mrr:
                mr = tuple(int(x) for x in mrr.read()[1:-1].split(','))
            if not is_on_curve(*sq, a, p):
                print('Точка sQ не принадлежит кривой')
                exit()
            if not is_on_curve(*frp, a, p):
                print('Точка f(R)P не принадлежит кривой')
                exit()
            if not is_on_curve(*mr, a, p):
                print('Точка mR не принадлежит кривой')
                exit()
            print(sq, frp, mr)
            if sq == pp(*frp, *mr, a, p):
                print('Подпись s подлинная')
            else:
                print('Подпись недействительна')
                exit()
        else:
            break


if __name__ == '__main__':
    main()
