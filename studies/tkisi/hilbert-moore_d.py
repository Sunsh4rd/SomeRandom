f = open("res6.bin", "rb")

d = {}
tree = {}
alphabet = {}
text = ''
ans = ''

str_keys = f.readline().decode()[:-2].split()
b = True
for i in str_keys:
    if b:
        tmp = i
        b = False
    else:
        alphabet.update({i:tmp})
        b = True

count_of_zero = int(f.readline().decode())
dump = f.read()
bitstr = ''
for b in dump:
    bits = bin(b)[2:].rjust(8, '0')
    bitstr += bits

text = bitstr[count_of_zero:]
f.close()

def true_word(pos, word, text):
    if (len(word) <= len(text) - pos):
        b = True
        for i in range(len(word)):
            if word[i] == text[pos + i]:
                b = b and True
            else:
                b = b and False
    else:
        b = False
    return b
        
i = 0              
while i < len(text):
    for j in list(alphabet.keys()): 
        if true_word(i, j, text):
            ans += alphabet[j]
            i += len(j)
            break
    
ans = ans.replace('_', ' ')
ans = ans.replace('*', '\n')

f = open("restore6.txt", "w")
f.write(ans)
f.close()




