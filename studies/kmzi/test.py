import functools
import itertools
from math import pi
import random
from collections import OrderedDict
from typing import Counter



def apply_permutation(s, p):
    return ''.join(s[i] for i in p)

#3021

msg = 'текстдляшифрования'
l = 5
splt_before_encrypt = [msg[i:i + l] + 'а' * (l-len(msg[i: i + l])) for i in range(0, len(msg), l)]
splt_after_encrypt = [apply_permutation(part, [3,0,2,1,4]) for part in splt_before_encrypt]
srtd = [''.join(sorted(prt)) for prt in splt_after_encrypt]

print(splt_after_encrypt, srtd)

# f = []
# ls = [0,1,2,3,4]
# r = list(filter(lambda x: x not in f, ls))
# print(r)

# to_splt = 'туеукуст'
for part_of_crypt in splt_after_encrypt:    
    encrypt_order = [(part_of_crypt[i], i) for i in range(len(part_of_crypt))]
    print(encrypt_order)
    srtd = sorted(encrypt_order) #[(splt[i], i) for i in range(len(splt))]
    # srtd.sort(key=lambda x: x[0])
    print(srtd)
    alph = { srtd[i]: i for i in range(len(srtd)) }

    print(alph)
    perm = [alph[sym] for sym in encrypt_order]
    print(perm)


to_permute = 'туеукуст'
alph = {'е': [0], 'к': [1], 'с': [2], 'т': [3, 4], 'у': [5, 6, 7]}
poss = [alph[c] for c in to_permute]
print(poss)
all_p = []
curr = []
single = []
last = [3,4]
count = 0
res = [0] * len(poss)
print('res',res)
for ind, e in enumerate(poss):

    print(ind, e)
    if len(e) == 1:
        res[ind] = e[0]
        single.append(ind)


    # print(res, single)
    last = e
    for ind1, e1 in enumerate(poss):
        test = [list(p) for p in itertools.permutations(last)]
        for p in test:
            pass

    
    # if len(ind) > 1:
        # curr.append(ind[i])
        # print(i)
        # i += 1
    # else:
        # curr.append(ind[0])
    
    # if len(ind) > 1:
    #     test = [list(p) for p in itertools.permutations(ind)]
    #     i = 0
    #     for p in test:
    #         while i < len(p):

    #     # perms = list(itertools.permutations(ind))
    #     # print(perms)
    #     print('used', used)
    #     pick = random.choice(list(filter(lambda x: x not in used, ind)))
    #     curr.append(pick)
    #     print('pick', pick)
    #     used.append(pick)
    #     print('used', used)

    # else:
    #     curr.append(ind[0])

print(curr)

#екст
#текс
#3012
# for s in srtd:
    
    # alph = { srtd[i][j]: [] for j in range(len(srtd[i])) }
    # alph = {}
    # print(alph)
    # for i in range(len(s)):
    #     if s[i] not in alph:
    #         alph[s[i]] = [i]
    #     else:
    #         alph[s[i]].append(i)

    # print(alph)
    
    # tmp2 = { j: splt[i][j] for j in range(len(splt[i])) }
    # tmp3 = [(j, srtd[i][j]) for j in range(len(srtd[i]))]
    
    # print(splt[i], alph) #, tmp2, tmp3)

    # currp = [alph[splt[i][j]] for j in range(len(splt[i]))]
    
    # print(currp)

    # currp = [tmp1[tmp2[v]] for k, v in tmp1]
    # print(currp)
    # currp1 = [list(splt[i]).index(tmp1[j][0]) for j in range(len(splt[i]))]
    # currp2 = [list(splt[i]).index(tmp2[j][1]) for j in range(len(splt[i]))]
    # print(currp1, currp2)

