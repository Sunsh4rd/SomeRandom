import string

alph = string.ascii_lowercase
alph_d = {i: alph[i] for i in range(len(alph))}
alph_dr = {alph[i]: i for i in range(len(alph))}

print(alph_d)
print(alph_dr)

s1 = {0: 14, 1: 9, 2: 17, 3: 10, 4: 20, 5: 22, 6: 15, 7: 13, 8: 3, 9: 25, 10: 8, 11: 4, 12: 7,
      13: 23, 14: 1, 15: 0, 16: 6, 17: 11, 18: 12, 19: 18, 20: 16, 21: 24, 22: 21, 23: 2, 24: 5, 25: 19}

s2 = {0: 25, 1: 13, 2: 11, 3: 20, 4: 21, 5: 15, 6: 2, 7: 18, 8: 16, 9: 14, 10: 4, 11: 22, 12: 7,
      13: 17, 14: 8, 15: 1, 16: 19, 17: 10, 18: 5, 19: 12, 20: 24, 21: 0, 22: 23, 23: 9, 24: 6, 25: 3}


msg = 'messagereally'

ms1 = ''.join(alph_d[s1[alph_dr[m]]] for m in msg)
ms1ms2 = ''.join(alph_d[s2[alph_dr[m]]] for m in ms1)
 
print(ms1, ms1ms2)
