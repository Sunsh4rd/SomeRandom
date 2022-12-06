from random import randint
from elliptic import pp, gen_curve

def is_on_curve(x, y, a, p):
    return pow(y, 2, p) == (pow(x, 3, p) + a*x) % p


def f(p, r):
    return p[0] % r


def main():
    while True:
        opt = input('0 - Генерация параметров\n'
                  + '1 - Вычислить h(m)\n'
                  + '2 - Найти s из h(m)=lf(R) + ks(mod r)\n')
        if opt =='0':
            p,a,q,r = gen_curve()
            print(p,a,q,r)
            eq = f'y**2 = x**3 + {a}*x'
            print(eq)
            # a = 3
            # r = 73
            # p = 137
            # q = (30, 52)
            l = int(input())
            _p = (q[0], q[1])
            print('1 _p', _p)
            for i in range(l-1):
                np = pp(*_p, q[0], q[1], a, p)
                _p = (np[0], np[1])
                print(f'{i+2} _p', _p)
            with open('elgamal_params/public_key.txt','w',encoding='utf-8') as pubkw:
                pubkw.write(f'{eq}\n{q}\n{_p}\n{r}\n{a}\n{p}')
            with open('elgamal_params/private_key.txt','w',encoding='utf-8') as privkw:
                privkw.write(f'{l}')
        elif opt =='1':
            with open('elgamal_params/public_key.txt','r',encoding='utf-8') as pubkr:
                _,q,_p,r,a,p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q,_p,r)
            with open('elgamal_params/message.txt','r',encoding='utf-8') as msgr:
                message = msgr.read()
                print(message)
                hm = int.from_bytes(message.encode(), byteorder='big') %r
                print(hm)
            with open('elgamal_params/hm.txt','w',encoding='utf-8') as hmw:
                hmw.write(str(hm))
        elif opt =='2':
            with open('elgamal_params/private_key.txt','r',encoding='utf-8') as privkr:
                l = int(privkr.read())
            with open('elgamal_params/public_key.txt','r',encoding='utf-8') as pubkr:
                _,q,_p,r,a,p = pubkr.read().split('\n')
                q = tuple(int(x) for x in q[1:-1].split(','))
                _p = tuple(int(x) for x in _p[1:-1].split(','))
                r = int(r)
                a = int(a)
                p = int(p)
                print(q,_p,r)
            with open('elgamal_params/hm.txt','r',encoding='utf-8') as hmr:
                hm = int(hmr.read())
                print(hm)
            while True:
                k = randint(1, r-1)
                print('k', k)
                print(pow(k, -1, r))
                _r = (q[0], q[1])
                print('1 _r', _r)
                for i in range(k-1):
                    np = pp(*_r, *q, a, p)
                    _r = (np[0], np[1])
                    print(f'{i+2} _r', _r)
                if f(_r, r) % r != 0:
                    s = ((hm-l*f(_r, r)) % r * pow(k, -1, r)) % r
                    print(s)
                    break
            with open('elgamal_params/s.txt','w',encoding='utf-8') as sw:
                sw.write(str(s))
            with open('elgamal_params/message.txt','r',encoding='utf-8') as msgr:
                message = msgr.read()
                print(message)
            with open('elgamal_params/signature.txt','w',encoding='utf-8') as sigw:
                sigw.write(f'{message} {_r} {s}')
        elif opt == '3':
            pass
        
    # print('sign:')
    
    signed = (message, _r, s)
    print(signed)
    print('check:')
    print(is_on_curve(*_r, a, p))
    _q = (q[0], q[1])
    print('1 _q', _q)
    for i in range(hm-1):
        np = pp(*_q, q[0], q[1], a, p)
        _q = (np[0], np[1])
        print(f'{i+2} _q', _q)
    __p = (_p[0], _p[1])
    print('1 __p', __p)
    for i in range(f(_r, r)-1):
        np = pp(*__p, _p[0], _p[1], a, p)
        __p = (np[0], np[1])
        print(f'{i+2} __p', __p)
    __r = (_r[0], _r[1])
    print('1 __r', __r)
    for i in range(s-1):
        np = pp(*__r, _r[0], _r[1], a, p)
        __r = (np[0], np[1])
        print(f'{i+2} __r', __r)

    print(_q, __p, __r)
    print(pp(*__p, *__r, a, p))
    print(hm)
    print(_q == pp(*__p, *__r, a, p))


if __name__ == '__main__':
    main()
