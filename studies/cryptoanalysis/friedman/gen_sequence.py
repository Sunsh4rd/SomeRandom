from random import choices


def gen_sequences(l):
    with open('params/alphrand.txt', 'r', encoding='utf-8') as alph_r, \
            open('params/rand1.txt', 'w', encoding='utf-8') as rt1_w, \
            open('params/rand2.txt', 'w', encoding='utf-8') as rt2_w:
        alph = alph_r.read()
        random_text_1 = ''.join(choices(alph, k=l))
        random_text_2 = ''.join(choices(alph, k=l))
        rt1_w.write(random_text_1)
        rt2_w.write(random_text_2)
        return random_text_1, random_text_2
