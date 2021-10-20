def apply_permutation(s, p):
    return ''.join(s[i] for i in p)

msg = 'текстдляшифрования'
l = 5
splt = [msg[i:i + l] + 'А' * (l-len(msg[i: i + l])) for i in range(0, len(msg), l)]
srtd = [''.join(sorted(prt)) for prt in splt]


print(splt, srtd)


#екст
#текс
#3012
for s in srtd:
    
    # alph = { srtd[i][j]: [] for j in range(len(srtd[i])) }
    alph = {}
    print(alph)
    for i in range(len(s)):
        if s[i] not in alph:
            alph[s[i]] = [i]
        else:
            alph[s[i]].append(i)

    print(alph)
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

