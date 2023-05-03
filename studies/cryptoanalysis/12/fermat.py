from math import sqrt, gcd


def main():
    n, k, l = map(int, input('Введите числа n, k (коэффициент близости), l (число итераций): ').split())
    i = 1
    done = False
    while True:
        while i < l + 1:
            s = int(sqrt(k * n)) + i
            t = sqrt(s * s - k * n)
            if t.is_integer(): # and (s + t) % n != 0 and (s - t) % n != 0:
                print(f'p = {gcd(n, gcd(k * n, s - int(t)))}')
                done = True
                break
            i += 1
        if done:
            break
        else:
            opt = input('Прошло l вычислений. Осуществить следующие l вычислений: y/n ')
            if opt == 'y':
                l *= 2
            else:
                break


if __name__ == '__main__':
    main()
