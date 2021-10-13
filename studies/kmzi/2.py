def update_map(s, m, k):
    for i in range(len(s) - k + 1):
        if s[i: i + k] in m:
            m[s[i: i + k]] += 1
        else:
            m[s[i: i + k]] = 1

alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_frequencies = { alph[i]:0 for i in range(len(alph)) }
sorted_by_freq = ['о','е','а','и','н','т','с','р','в','л',
'к','м','д','п','у','я','ы','ь','г','з','б',
'ч','й','х','ж','ш','ю','ц','щ','э','ф','ъ','ё']
sorted_by_freq_cap = [l.upper() for l in sorted_by_freq]

read_text = []
with open('input_4.txt', 'r', encoding='utf-8') as f1:
    
    for s in f1.readlines():
        s = s.replace('\n', '')
        read_text.append(s)


for s in read_text:
    for i in s:
        alph_frequencies[i] += 1
    
print(alph_frequencies)
get_sorted_by_freq = list(alph_frequencies.items())
get_sorted_by_freq.sort(key=lambda x: x[1], reverse=True)
get_sorted_by_freq_only_al = [k for k, v in get_sorted_by_freq]
print(get_sorted_by_freq_only_al)

mapped = []
for s in read_text:
    tmp = ''
    for i in s:
        tmp += sorted_by_freq_cap[get_sorted_by_freq_only_al.index(i)]
    mapped.append(tmp)

print(mapped)

bigramm = { i+j:0 for i in alph for j in alph }

most_frq_bi = ['СТ', 'НО', 'ЕН', 'ТО', 'НА', 'ОВ', 'НИ', 'РА', 'ВО', 'КО']



for s in read_text:
    update_map(s, bigramm, 2)

print(bigramm)

get_sorted_by_freq_bi = list(bigramm.items())
get_sorted_by_freq_bi.sort(key=lambda x: x[1], reverse=True)
get_sorted_by_freq_only_bi = [k for k, v in get_sorted_by_freq_bi]
# print(get_sorted_by_freq_only_bi)

mapped_bi = []
for s in read_text:
    tmp = ''
    while s:
        a = s[:2]
        try:
            tmp += most_frq_bi[get_sorted_by_freq_only_bi.index(i)]
        except ValueError:
            print('e')
        s = s[2:]
    mapped_bi.append(tmp)

print(mapped_bi)

# trigramm = { i+j+k:0 for i in alph for j in alph for k in alph }

# for s in read_text:
#     update_map(s, trigramm, 3)


# print(trigramm)

# get_sorted_by_freq_tri = list(trigramm.items())
# get_sorted_by_freq_tri.sort(key=lambda x: x[1], reverse=True)
# get_sorted_by_freq_only_tri = [k for k, v in get_sorted_by_freq_tri]
# print(get_sorted_by_freq_only_tri)


with open('output.txt', 'w') as f2:
    pass
