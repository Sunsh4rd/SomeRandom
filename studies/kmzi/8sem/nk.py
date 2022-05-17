import random

def check(x):
    for i in x:
        if not x.isdigit():
            return False
    return True

def my_sum(a, b):
    ans = [0]
    if len(a) >= len(b):
        j = 0
        k = 0
        for i in a:
            ans += [int(i)]
        while j < len(b):
            ans[len(ans)-1-j] = (ans[len(ans) - 1 - j] + int(b[len(b) - 1 - j]) + k) % 10
            k = (int(a[len(a) - 1 - j]) + int(b[len(b) - 1 - j]) + k) // 10
            j += 1
        ans[len(ans)-1-j] += k
        for i in range(len(ans) - 1, 1, -1):
            if ans[i] == 10:
                ans[i] = 0
                ans[i - 1] += 1
        ans_str = ''
        for i in ans:
            ans_str += str(i)
        if ans_str[0] == '0':
            ans_str = ans_str[1:]
        return ans_str
    else:
        j = 0
        k = 0
        for i in b:
            ans += [int(i)]
        while j < len(a):
            ans[len(ans)-1-j] = (ans[len(ans) - 1 - j] + int(a[len(a) - 1 - j]) + k) % 10
            k = (int(b[len(b) - 1 - j]) + int(a[len(a) - 1 - j]) + k) // 10
            j += 1
        ans[len(ans)-1-j] += k
        for i in range(len(ans) - 1, 1, -1):
            if ans[i] == 10:
                ans[i] = 0
                ans[i - 1] += 1
        ans_str = ''
        for i in ans:
            ans_str += str(i)
        if ans_str[0] == '0':
            ans_str = ans_str[1:]
        return ans_str
    
def dif(a, b):
    if int(a) >= int(b):
        return (a, b, True)
    else:
        return (b, a, False)

def my_mult(a, b):
    j = 0
    ans = [0 for i in range(len(a) + len(b))]
    while j < len(b):
        if int(b[len(b) - j - 1]) == 0:
            ans[len(ans) - 1 - len(a) - j] = 0
            j += 1
        else:
            i = 0
            k = 0
            while i < len(a):
                t = int(a[len(a) - 1 - i]) * int(b[len(b) - 1 - j]) + k + ans[len(ans) - 1 - i - j]
                ans[len(ans) - 1 - i - j] = t % 10
                k = t // 10
                i += 1
            ans[len(ans) - 1 - i - j] = k
            j += 1
    if ans[0] == 0:
        ans = ans[1:]
    ans_str = ''
    for i in ans:
        ans_str += str(i)
    return ans_str

def my_sub(a, b):
    variables = dif(a, b)
    sub_a = variables[0]
    sub_b = variables[1]
    sub_zn = variables[2]
    j = 0
    k = 0
    ans = []
    while j < len(sub_b):
        x_a = len(sub_a) - 1 - j
        x_b = len(sub_b) - 1 - j        
        tmp = int(sub_a[x_a]) - int(sub_b[x_b]) + k
        if tmp < 0:
            tmp += 10
            k = -1
        else:
            k = 0
        ans = [tmp] + ans
        j += 1
    while j < len(sub_a):
        x_a = len(sub_a) - 1 - j
        if int(sub_a[x_a]) + k < 0:
           ans = [int(sub_a[x_a]) + k + 10] + ans
           k = -1
        else:
           ans = [int(sub_a[x_a]) + k] + ans
           k = 0
        j += 1
    i = 0
    for i in range(len(ans)):
        if ans[i] != 0:
            break
    ans = ans[i:]
    ans_str = ''
    for i in ans:
        ans_str += str(i)
    if sub_zn:
        return ans_str
    else:
        return '-' + ans_str
    
def my_div(a, b):
    div_a = a
    ch = len(div_a)
    div_b = b
    d = 10 // (int(div_b[0]) + 1)
    tmp = len(div_a)
    n = len(div_b)
    m = len(div_a) - n
    div_a = my_mult(div_a, str(d))
    div_b = my_mult(div_b, str(d))
    j = m
    ans_ch = ''
    q_ch = '0'
    r_ch = a
    if n == 1:
        while True:
            if int(div_a[0]) >= int(div_b[0]):
                q_ch = (int(div_a[0])) // int(div_b[0])
                r_ch = (int(div_a[0])) % int(div_b[0])
                div_a = str(r_ch) + div_a[1:]
                ans_ch += str(q_ch)
            else:
                if len(div_a) == 1:
                    if ans_ch == '':
                        return ('0', a)
                    else:
                        return (ans_ch, str(r_ch // d))
                else:
                    q_ch = (int(div_a[0]) * 10  + int(div_a[1])) // int(div_b[0])
                    r_ch = (int(div_a[0]) * 10  + int(div_a[1])) % int(div_b[0])
                    div_a = str(r_ch) + div_a[2:]
                    ans_ch += str(q_ch)
    else:
        ans_ch = ''
        if tmp == len(div_a):
            div_a = '0' + div_a
        while j >= 0:
            q_ch = (int(div_a[len(div_a) - j - n - 1]) * 10  + int(div_a[len(div_a) - j - n])) // int(div_b[0])
            r_ch = (int(div_a[len(div_a) - j - n - 1]) * 10  + int(div_a[len(div_a) - j - n])) % int(div_b[0])
            if q_ch == 10 or q_ch * int(div_b[1]) > 10 * r_ch + int(div_a[len(div_a) - j - n + 1]):
                q_ch -= 1
                r_ch += int(div_b[0])
                if r_ch < 10:
                    if q_ch == 10 or q_ch * int(div_b[1]) > 10 * r_ch + int(div_a[len(div_a) - j - n + 1]):
                        q_ch -= 1
                        r_ch += int(div_b[0])
            sub_div_a = ''
            for i in range(len(div_a) - j - n - 1, len(div_a) - j):
                sub_div_a += div_a[i]
            sub_div_a = int(sub_div_a) - q_ch * int(div_b)
            flag = False
            if sub_div_a < 0:
                sub_div_a += pow(10, n + 1)
                flag = True
            sub_div_a = str(sub_div_a)
            while len(sub_div_a) < n + 1:
                sub_div_a = '0' + sub_div_a
            ans_ch += str(q_ch)
            new_div_a = ''
            for i in range(m - j):
                new_div_a += div_a[i]
            new_div_a += sub_div_a
            for i in range(m - j + len(str(sub_div_a)), len(div_a)):
                new_div_a += div_a[i]
            div_a = new_div_a
            if flag:
                ans_ch = ans_ch[:-1]
                ans_ch += str(q_ch - 1)
                sub_div_a = int(sub_div_a) + int(div_b)
                str_sub_div_a = str(sub_div_a)[1:]
                new_div_a = ''
                for i in range(m - j):
                    new_div_a += div_a[i]
                new_div_a += str_sub_div_a
                for i in range(m - j + len(str_sub_div_a), len(div_a)):
                    new_div_a += div_a[i]
                div_a = new_div_a
            j -= 1            
    if ans_ch == '':
        return ('0', a)
    else:
        ans_r = ''
        for i in range(len(div_a) - n - 1, len(div_a)):
            ans_r += div_a[i]
        while True:
            if ans_ch[0] == '0' and len(ans_ch) > 1:
                ans_ch = ans_ch[1:]
            else:
                break
        return (ans_ch, str(int(ans_r) // d))

def my_pow(a, d, m):
    n = d
    #int(d)
    y = '1'
    z = my_div(a, m)[1]
    if a == '0' and d == '0':
        return '0'
    #int(a)
    while True:
        tmp_n = my_div(n, '2')
        n = tmp_n[0]
        #print(tmp_n[0], tmp_n[1])
        if tmp_n[1] != '0':
            y = my_div(my_mult(y, z), m)[1]
        #(z * y) % int(m)
        if n == '0':
            return y
        z = my_div(my_mult(z, z), m)[1]
        #(z * z) % int(m)

def miller_rabin(n):
    n_1 = my_sub(n, '1')
    d = n_1
    s = '0'
    while my_pow(d, '1', '2') == '0':
        s = my_sum(s, '1')
        d = my_div(d, '2')[0]
    a, r = '1', '0'
    flag = True
    while my_sub(n, a) != '0':
        if my_pow(a, d, n) != '1':
            flag = False
            while my_sub(s, r) != '0':
                if my_pow(a, my_mult(my_pow('2', r, n), d), n) == n_1:
                   flag = True
                   break
                r = my_sum(r, '1')
            if not flag:
                break
        a = my_sum(a, '1')
        r = '0'
    return flag
                

def generator_q(k):
    q = '1'
    for i in range(k - 1):
        q += str(int(random.uniform(0, 9)) % 2)
    return q

def generator_s(k):
    s = '1'
    for i in range(k - 2):
        s += str(int(random.uniform(0, 9)) % 2)
    s += '0'
    return s

def to_decade(x):
    ans = '0'
    for i in range(len(x)):
        if x[i] == '1':
            ans = my_sum(ans, my_pow('2', str(len(x) - 1 - i), x))
    return ans

def true_size(x, k):
    s = '0'
    while x != '0' and x != '1':
        x = my_div(x, '2')[0]
        s = my_sum(s, '1')
    return k == my_sum(s, '1')

def generator_p(k):
    q = to_decade(generator_q(int(my_div(k, '2')[0])))
    s = to_decade(generator_s(int(my_sub(k, my_div(k, '2')[0])))) 
    while not miller_rabin(q):
        q = to_decade(generator_q(int(my_div(k, '2')[0])))
    p = my_sum(my_mult(q, s), '1')
    flag = true_size(p, k)
    flag = flag and dif(p, my_mult(my_sum('1', my_mult('2', q)), my_sum('1', my_mult('2', q))))
    flag = flag and my_pow('2', my_mult(q, s), p) == '1'
    flag = flag and my_pow('2', s, p) != '1'
    while not flag:
        q = to_decade(generator_q(int(my_div(k, '2')[0])))
        s = to_decade(generator_s(int(my_sub(k, my_div(k, '2')[0])))) 
        while not miller_rabin(q):
            q = to_decade(generator_q(int(my_div(k, '2')[0]))) 
        p = my_sum(my_mult(q, s), '1')
        flag = true_size(p, k)
        flag = flag and dif(p, my_mult(my_sum('1', my_mult('2', q)), my_sum('1', my_mult('2', q))))
        flag = flag and my_pow('2', my_mult(q, s), p) == '1'
        flag = flag and my_pow('2', s, p) != '1'
    return p


#def reverse(e, n):
   # d = '1'
   # while True:
#      #  if my_div(my_mult(e, d), n)[1] == '1':
 #           break
  #      d = my_sum(d, '1')
   # if d == e:
    #    d = my_sum(d, n)
    #return d

def reverse(e, n):
    t, r, newt, newr = '0', n, '1', e
    while newr != '0':
        while newt[0] == '-':
            newt = my_sub(n, newt[1:])
        while newr[0] == '-':
            newr = my_sub(n, newr[1:])
        q = my_div(r, newr)[0]
        t, newt = newt, my_sub(t, my_mult(q, newt))
        r, newr = newr, my_sub(r, my_mult(q, newr))
    if t == e:
        t = my_sum(t, n)
    return t

def size(x):
    s = '0'
    while x != '0' and x != '1':
        x = my_div(x, '2')[0]
        s = my_sum(s, '1')
    return my_sum(s, '1')

def key_generator():
    p = generator_p('16')
    q = generator_p('16')
    while q == p:
        q = generator_p('16')
    print(p, q)
    n = my_mult(p, q)
    f = my_mult(my_sub(q, '1'), my_sub(p, '1'))
    e = '5'
    e = generator_p(str(int(random.uniform(5, int(size(f)) - 1))))
    while my_div(f, e)[1] == '0':
        e = generator_p(str(int(random.uniform(5, int(size(f)) - 1))))
    d = reverse(e, f)
    return n, e, d


n, e, d = key_generator()

def main(n, e, d):
    print(n, e, d)
    print("Введите команду [1 - Зашифровать сообщение, 2 - Расшифровать сообщение, 3 - Пересчитать ключи]")
    command = int(input())
    if command == 1:
        f = open('message.txt', 'r', encoding='utf-8')
        text = f.read()
        f.close()
        if text != '':
            shifr = ''
            for i in text:
                letter = str(ord(i))
                shifr += my_pow(letter, e, n) + ' '
            shifr = shifr[:-1]
            f = open('shifr.txt', 'w')
            f.write(shifr)
            f.close()
            print("Сообщение зашифровано")
            main(n, e, d)
        else:
            print("Текст сообщения пустой")
            main(n, e, d)
    elif command == 2:
        f = open('shifr.txt', 'r')
        text = f.read()
        f.close()
        if text != '':
            deshifr = ''
            for i in text.split():
                letter = chr(int(my_pow(i, d, n)))
                deshifr += letter
            f = open('deshifr.txt', 'w', encoding='utf-8')
            f.write(deshifr)
            f.close()
            print("Сообщение расшифровано")
            main(n, e, d)
        else:
            print("Текст шифра пустой")
            main(n, e, d)
    elif command == 3:
        n, e, d = key_generator()
        print("Ключи пересчитаны")
        main(n, e, d)
    else:
        print("Неверная команда")
        main(n, e, d)

main(n, e, d)

    
