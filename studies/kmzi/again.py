# p = 4

text1 = 'бавгедёжизйк'
text2 = 'гбавжедёкизй'


def check_permutation(text1, text2, p):
    split_text1 = [text1[i:i + len(p)] for i in range(0, len(text1), len(p))]
    split_text2 = [text2[i:i + len(p)] for i in range(0, len(text2), len(p))]

    for offset in range(0, len(text1), len(p)):
        for i in range(len(p)):
            if text1[offset + i] != text2[offset + p[i]]:
                print(text1[offset + i], text2[offset + p[i]])
                return False
        return True


def R(a, b, pos, p):
    if pos == len(p): 
        check_permutation(text1, text2, p)
        
    for i in range(len(b)):
        if a[pos] == b[i]: 
            p[pos] = i
            if i not in p:
                R(a, b, pos + 1, p)
    
    p = [None] * len(p)


R(text1, text2, 3, [0,1,2,3])