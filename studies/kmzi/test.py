msg = 'текстдляшифрования'
l = 9
splt = [msg[i:i+l] for i in range(0, len(msg), l)]
srtd = [''.join(sorted(prt)) for prt in splt]

print(splt, srtd)

sorted()