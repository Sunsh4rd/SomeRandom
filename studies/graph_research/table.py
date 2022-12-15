# TODO: fix for number of verts > 9

for x in range(4,11):
    with open(f'{x}.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        # print(data)
        k = 0
        k1 = 0
        ss = []
        for i in data[:-1]:
            s = i.split(' \t')
            if s[1][-1] == s[2][-2]:
                # print(s)
                ss.append(s)
                k1+=1
            k+=1
        # print(k,k1)
        # print(len(data), data[-1])

    with open(f'{x}r.txt','w',encoding='utf-8') as f1:
        for s in ss:
            f1.write(f'{s[0]} {s[1][-1]} {s[2][-2]}\n')