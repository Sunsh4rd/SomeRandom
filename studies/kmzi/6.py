import math
import string
import json

alph = string.ascii_lowercase
alph_d = {str(i): alph[i] for i in range(len(alph))}
alph_dr = {alph[i]: str(i) for i in range(len(alph))}


def subs():
    with open('studies\kmzi\s1.json', 'r') as f:
        s1 = json.load(f)

    with open('studies\kmzi\s2.json', 'r') as f:
        s2 = json.load(f)

    return s1, s2


def encrypt(msg, s):
    return ''.join(alph_d[s[alph_dr[m]]] for m in msg)


def compose(s1, s2):
    return { k: s2[v] for k, v in s1.items()}


def main():

    msg = 'messagereally'

    if subs():
        s1, s2 = subs()
        print('s1(m) =', encrypt(msg, s1))
        print('s2(s1(m)) =', encrypt(encrypt(msg, s1), s2))
        print('s3 = s2(s1)')
        s3 = compose(s1, s2)
        print('s3(m) =', encrypt(msg, s3))

    


if __name__ == '__main__':
    main()
