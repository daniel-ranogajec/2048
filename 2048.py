import random
import os

poz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

score = 0
blok=0
win = 0

while True:
    os.system('cls')
    i = 0
    t = 0
    while (i < 16):
        if poz[i] == 0:
            t = t + 1
        i = i + 1

    if t == 0:
        print('GAME OVER\n')
        print('SCORE: ', score)
        print('\nName: ')
        ime = input()
        if (int(score) < 10):
            score_ = f'000000{score}'
        elif (int(score) < 100):
            score_ = f'00000{score}'
        elif (int(score) < 1000):
            score_ = f'0000{score}'
        elif (int(score) < 10000):
            score_ = f'000{score}'
        elif (int(score) < 100000):
            score_ = f'00{score}'
        elif (int(score) < 1000000):
            score_ = f'0{score}'
        else:
            score_ = score
        lista = []
        try:
            with open('highscore.txt', 'r') as rf:
                for line in rf:
                    lista.append(line)
        except Exception:
            f = open('highscore.txt', 'w')
            f.close()
        ime_ = f'{score_} {ime}\n'
        lista.append(ime_)
        s = sorted(lista, reverse=True)
        with open('highscore.txt', 'w') as wf:
            for line in s:
                wf.write(line)
        lista_ = []
        for el in s:
            el_ = el.lstrip('0')
            lista_.append(el_)
        num = 0
        kk = 10
        if (len(lista) < 10):
            kk = len(lista)
        print('\n')
        print(f'Top {kk}:')
        print('\n')
        while (num<kk):
            print (lista_[num])
            num = num+1
        print ("""
    Do you want to:
        1. RESTART
        2. EXIT
        """)
        w = input()
        if (w == '1' or  w== '1.' or w.lower() == 'restart' or w.lower() == 'r'):
            score = 0
            blok = 0
            poz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            os.system('cls')
        else:
            exit()

    z = 0
    while (z < 16):
        if (poz[z] == 2048 and win == 0):
            os.system('cls')
            print ("""
            Victory!
        1. CONTINUE
        2. RESTART
        3. EXIT            
            """)
            b = input()
            if (b == '1' or b == '1.' or b.lower() == 'continue' or b.lower() == 'c'):
                win = 1
            elif (b == '2' or b == '2.' or b.lower() == 'restart' or b.lower() == 'r'):
                score = 0
                blok = 0
                poz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                os.system('cls')
            else:
                exit()
        z = z + 1

    brojevi = [2, 2, 2, 2, 4]
    r_broj = random.choice(brojevi)

    n = 0
    if (blok < 4):
        while (n != 1):
            rand = random.randrange(0, 16, 1)
            if poz[rand] == 0:
                poz[rand] = r_broj
                n = 1

    blok = 0

    m = 0
    max = 0
    while (m<16):
        if (max < poz[m]):
            max = poz[m]
        m = m+1

    if (max < 10):
        a = '*************************'
        print(a)
        print('* ', poz[0], ' * ', poz[1], ' * ', poz[2], ' * ', poz[3], ' *')
        print(a)
        print('* ', poz[4], ' * ', poz[5], ' * ', poz[6], ' * ', poz[7], ' *')
        print(a)
        print('* ', poz[8], ' * ', poz[9], ' * ', poz[10], ' * ', poz[11], ' *')
        print(a)
        print('* ', poz[12], ' * ', poz[13], ' * ', poz[14], ' * ', poz[15], ' *')
        print(a)

    elif (max > 10 and max < 100):
        a = '*****************************'
        n=0
        poz_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while (n<16):
            if poz[n]<10:
                poz_[n] = f' {poz[n]}'
            else:
                poz_[n]=poz[n]
            n=n+1
        print(a)
        print('* ', poz_[0], ' * ', poz_[1], ' * ', poz_[2], ' * ', poz_[3], ' *')
        print(a)
        print('* ', poz_[4], ' * ', poz_[5], ' * ', poz_[6], ' * ', poz_[7], ' *')
        print(a)
        print('* ', poz_[8], ' * ', poz_[9], ' * ', poz_[10], ' * ', poz_[11], ' *')
        print(a)
        print('* ', poz_[12], ' * ', poz_[13], ' * ', poz_[14], ' * ', poz_[15], ' *')
        print(a)

    elif (max > 100 and max < 1000):
        a = '*********************************'
        n = 0
        poz_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while (n < 16):
            if poz[n] < 10:
                poz_[n] = f' {poz[n]} '
            elif (poz[n]>10 and poz[n]<100):
                poz_[n] = f' {poz[n]}'
            else:
                poz_[n] = poz[n]
            n = n + 1
        print(a)
        print('* ', poz_[0], ' * ', poz_[1], ' * ', poz_[2], ' * ', poz_[3], ' *')
        print(a)
        print('* ', poz_[4], ' * ', poz_[5], ' * ', poz_[6], ' * ', poz_[7], ' *')
        print(a)
        print('* ', poz_[8], ' * ', poz_[9], ' * ', poz_[10], ' * ', poz_[11], ' *')
        print(a)
        print('* ', poz_[12], ' * ', poz_[13], ' * ', poz_[14], ' * ', poz_[15], ' *')
        print(a)

    elif (max > 1000 and max < 10000):
        a = '*************************************'
        n = 0
        poz_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while (n < 16):
            if poz[n] < 10:
                poz_[n] = f'  {poz[n]} '
            elif (poz[n]>10 and poz[n]<100):
                poz_[n] = f' {poz[n]} '
            elif (poz[n]>100 and poz[n]<1000):
                poz_[n] = f' {poz[n]}'
            else:
                poz_[n] = poz[n]
            n = n + 1
        print(a)
        print('* ', poz_[0], ' * ', poz_[1], ' * ', poz_[2], ' * ', poz_[3], ' *')
        print(a)
        print('* ', poz_[4], ' * ', poz_[5], ' * ', poz_[6], ' * ', poz_[7], ' *')
        print(a)
        print('* ', poz_[8], ' * ', poz_[9], ' * ', poz_[10], ' * ', poz_[11], ' *')
        print(a)
        print('* ', poz_[12], ' * ', poz_[13], ' * ', poz_[14], ' * ', poz_[15], ' *')
        print(a)
    else:
        a = '*****************************************'
        n = 0
        poz_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while (n < 16):
            if poz[n] < 10:
                poz_[n] = f'  {poz[n]}  '
            elif (poz[n] > 10 and poz[n] < 100):
                poz_[n] = f'  {poz[n]} '
            elif (poz[n] > 100 and poz[n] < 1000):
                poz_[n] = f' {poz[n]} '
            elif (poz[n] > 1000 and poz[n] < 10000):
                poz_[n] = f' {poz[n]}'
            else:
                poz_[n] = poz[n]
            n = n + 1
        print(a)
        print('* ', poz_[0], ' * ', poz_[1], ' * ', poz_[2], ' * ', poz_[3], ' *')
        print(a)
        print('* ', poz_[4], ' * ', poz_[5], ' * ', poz_[6], ' * ', poz_[7], ' *')
        print(a)
        print('* ', poz_[8], ' * ', poz_[9], ' * ', poz_[10], ' * ', poz_[11], ' *')
        print(a)
        print('* ', poz_[12], ' * ', poz_[13], ' * ', poz_[14], ' * ', poz_[15], ' *')
        print(a)

    print(score)

    x = input()

    if (x == 'w'):
        for i in range(0, 4):
            if (poz[i + 12] == poz[i] and poz[i + 4] == 0 and poz[i + 8] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 12] != 0 and poz[i] == 0 and poz[i + 4] == 0 and poz[i + 8] == 0):
                poz[i] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i + 12] == poz[i + 4] and poz[i] == 0 and poz[i + 8] == 0 and poz[i + 4] != 0):
                poz[i] = poz[i + 12] * 2
                poz[i + 4] = 0
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 12] != poz[i + 4] and poz[i + 8] == 0 and poz[i] == 0 and poz[i + 12] != 0 and poz[
                i + 4] != 0):
                poz[i] = poz[i + 4]
                poz[i + 4] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i + 12] == poz[i + 8] and poz[i] == poz[i + 4] and poz[i] != 0 and poz[i + 8] != 0):
                poz[i] = poz[i] * 2
                poz[i + 4] = poz[i + 8] * 2
                poz[i + 8] = 0
                poz[i + 12] = 0
                score = score + poz[i] + poz[i + 4]
            elif (poz[i + 12] == poz[i + 8] and poz[i] == 0 and poz[i + 4] == 0 and poz[i + 8] != 0):
                poz[i] = poz[i + 12] * 2
                poz[i + 8] = 0
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 12] == poz[i + 8] and poz[i + 4] == 0 and poz[i] != 0 and poz[i] != poz[i + 8] and poz[
                i + 8] != 0):
                poz[i + 4] = poz[i + 8] * 2
                poz[i + 8] = 0
                poz[i + 12] = 0
                score = score + poz[i + 4]
            elif (poz[i + 12] == poz[i + 4] and poz[i] != 0 and poz[i] != poz[i + 12] and poz[i + 8] == 0 and poz[
                i + 4] != 0):
                poz[i + 4] = poz[i + 4] * 2
                poz[i + 12] = 0
                score = score + poz[i + 4]
            elif (poz[i] == poz[i + 4] and poz[i + 8] != 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 4] = poz[i + 8]
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 8] == poz[i + 4] and poz[i] == 0 and poz[i + 4] != 0):
                poz[i] = poz[i + 4] * 2
                poz[i + 4] = poz[i + 12]
                poz[i + 8] = 0
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 8] == poz[i + 4] and poz[i] != 0 and poz[i + 4] != 0):
                poz[i + 4] = poz[i + 4] * 2
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i + 4]
            elif (poz[i] != poz[i + 4] and poz[i + 4] == poz[i + 8] and poz[i] != 0 and poz[i + 4] != 0):
                poz[i + 4] = poz[i + 4] * 2
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i + 4]
            elif (poz[i + 12] == poz[i + 8] and poz[i] != 0 and poz[i + 4] != 0 and poz[i] != poz[i + 4] and poz[
                i + 8] != 0):
                poz[i + 8] = poz[i + 8] * 2
                poz[i + 12] = 0
                score = score + poz[i + 8]
            elif (poz[i + 12] == poz[i + 8] and poz[i] == 0 and poz[i + 4] != 0):
                poz[i] = poz[i + 4]
                poz[i + 4] = poz[i + 8] * 2
                poz[i + 8] = 0
                poz[i + 12] = 0
                score = score + poz[i + 4]
            elif (poz[i + 8] == poz[i] and poz[i + 4] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 8] = 0
                poz[i + 4] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 4] == poz[i] and poz[i + 8] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 4] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i + 4] == poz[i] and poz[i + 8] != 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 4] = poz[i + 8]
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
                score = score + poz[i]
            elif (poz[i] != poz[i + 12] and poz[i + 4] == 0 and poz[i + 8] == 0 and poz[i + 12] != 0 and poz[i] != 0):
                poz[i + 4] = poz[i + 12]
                poz[i + 8] = 0
                poz[i + 12] = 0
            elif (poz[i] != poz[i + 12] and poz[i + 4] != 0 and poz[i + 8] == 0 and poz[i + 12] != 0 and poz[i] != 0):
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i + 12] != poz[i + 4] and poz[i + 4] != 0 and poz[i + 12] != 0 and poz[i + 8] == 0 and poz[
                i] == 0):
                poz[i] = poz[i + 4]
                poz[i + 4] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i + 12] != poz[i + 4] and poz[i + 4] != 0 and poz[i + 12] != 0 and poz[i + 4] != poz[i] and poz[
                i + 8] == 0 and poz[i] != 0):
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i] == 0 and poz[i + 4] == 0 and poz[i + 8] != poz[i + 12]):
                poz[i] = poz[i + 8]
                poz[i + 4] = poz[i + 12]
                poz[i + 8] = 0
                poz[i + 12] = 0
            elif (poz[i] != poz[i + 8] and poz[i + 4] == 0 and poz[i] != 0 and poz[i + 8] != 0):
                poz[i + 4] = poz[i + 8]
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i] != poz[i + 4] and poz[i] != 0 and poz[i + 8] == 0 and poz[i + 12] != poz[i + 4] and poz[
                i + 12] != 0):
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i] == 0 and poz[i + 4] == 0 and poz[i + 8] != 0 and poz[i + 8] != poz[i + 12]):
                poz[i] = poz[i + 8]
                poz[i + 4] = poz[i + 12]
                poz[i + 8] = 0
                poz[i + 12] = 0
            elif (poz[i] != poz[i + 8] and poz[i] != 0 and poz[i + 8] != 0 and poz[i + 4] == 0):
                poz[i + 4] = poz[i + 8]
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            elif (poz[i] == 0 and poz[i + 4] != poz[i + 8] and poz[i + 8] != poz[i + 12]):
                poz[i] = poz[i + 4]
                poz[i + 4] = poz[i + 8]
                poz[i + 8] = poz[i + 12]
                poz[i + 12] = 0
            else:
                blok = blok + 1

    elif (x == 's'):
        for i in range(0, 4):
            if (poz[i] == poz[i + 12] and poz[i + 8] == 0 and poz[i + 4] == 0 and poz[i + 12] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i] != 0 and poz[i + 12] == 0 and poz[i + 8] == 0 and poz[i + 4] == 0):
                poz[i + 12] = poz[i]
                poz[i] = 0
            elif (poz[i] == poz[i + 8] and poz[i + 12] == 0 and poz[i + 4] == 0 and poz[i + 8] != 0):
                poz[i + 12] = poz[i] * 2
                poz[i + 8] = 0
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i] != poz[i + 8] and poz[i + 4] == 0 and poz[i + 12] == 0 and poz[i] != 0 and poz[
                i + 8] != 0):
                poz[i + 12] = poz[i + 8]
                poz[i + 8] = poz[i]
                poz[i] = 0
            elif (poz[i] == poz[i + 4] and poz[i + 12] == poz[i + 8] and poz[i + 12] != 0 and poz[i + 4] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i + 8] = poz[i + 4] * 2
                poz[i + 4] = 0
                poz[i] = 0
                score = score + poz[i + 12] + poz[i + 8]
            elif (poz[i] == poz[i + 4] and poz[i + 12] == 0 and poz[i + 8] == 0 and poz[i + 4] != 0):
                poz[i + 12] = poz[i] * 2
                poz[i + 4] = 0
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i] == poz[i + 4] and poz[i + 8] == 0 and poz[i + 12] != 0 and poz[i + 12] != poz[i + 4] and poz[
                i + 4] != 0):
                poz[i + 8] = poz[i + 4] * 2
                poz[i + 4] = 0
                poz[i] = 0
                score = score + poz[i + 8]
            elif (poz[i] == poz[i + 8] and poz[i + 12] != 0 and poz[i + 12] != poz[i] and poz[i + 4] == 0 and poz[
                i + 8] != 0):
                poz[i + 8] = poz[i + 8] * 2
                poz[i] = 0
                score = score + poz[i + 8]
            elif (poz[i + 12] == poz[i + 8] and poz[i + 4] != 0 and poz[i + 12] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i + 8] = poz[i + 4]
                poz[i + 4] = poz[i]
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i + 4] == poz[i + 8] and poz[i + 12] == 0 and poz[i + 8] != 0):
                poz[i + 12] = poz[i + 8] * 2
                poz[i + 8] = poz[i]
                poz[i + 4] = 0
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i + 4] == poz[i + 8] and poz[i + 12] != 0 and poz[i + 8] != 0):
                poz[i + 8] = poz[i + 8] * 2
                poz[i + 4] = poz[i]
                poz[i] = 0
                score = score + poz[i + 8]
            elif (poz[i + 12] != poz[i + 8] and poz[i + 8] == poz[i + 4] and poz[i + 12] != 0 and poz[i + 8] != 0):
                poz[i + 8] = poz[i + 8] * 2
                poz[i + 4] = poz[i]
                poz[i] = 0
                score = score + poz[i + 8]
            elif (poz[i] == poz[i + 4] and poz[i + 12] != 0 and poz[i + 8] != 0 and poz[i + 12] != poz[i + 8] and poz[
                i + 4] != 0):
                poz[i + 4] = poz[i + 4] * 2
                poz[i] = 0
                score = score + poz[i + 4]
            elif (poz[i] == poz[i + 4] and poz[i + 12] == 0 and poz[i + 8] != 0):
                poz[i + 12] = poz[i + 8]
                poz[i + 8] = poz[i + 4] * 2
                poz[i + 4] = 0
                poz[i] = 0
                score = score + poz[i + 8]
            elif (poz[i + 4] == poz[i + 12] and poz[i + 8] == 0 and poz[i + 12] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i + 4] = 0
                poz[i + 8] = poz[i]
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i + 8] == poz[i + 12] and poz[i + 4] == 0 and poz[i + 12] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i + 8] = poz[i]
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i + 8] == poz[i + 12] and poz[i + 4] != 0 and poz[i + 12] != 0):
                poz[i + 12] = poz[i + 12] * 2
                poz[i + 8] = poz[i + 4]
                poz[i + 4] = poz[i]
                poz[i] = 0
                score = score + poz[i + 12]
            elif (poz[i + 12] != poz[i] and poz[i + 8] == 0 and poz[i + 4] == 0 and poz[i] != 0 and poz[i + 12] != 0):
                poz[i + 8] = poz[i]
                poz[i + 4] = 0
                poz[i] = 0
            elif (poz[i + 12] != poz[i] and poz[i + 8] != 0 and poz[i + 4] == 0 and poz[i] != 0 and poz[i + 12] != 0):
                poz[i + 4] = poz[i]
                poz[i] = 0
            elif (poz[i] != poz[i + 8] and poz[i + 8] != 0 and poz[i] != 0 and poz[i + 4] == 0 and poz[
                i + 12] == 0):
                poz[i + 12] = poz[i + 8]
                poz[i + 8] = poz[i]
                poz[i] = 0
            elif (poz[i] != poz[i + 8] and poz[i + 8] != 0 and poz[i] != 0 and poz[i + 8] != poz[i + 12] and poz[
                i + 4] == 0 and poz[i + 12] != 0):
                poz[i + 4] = poz[i]
                poz[i] = 0
            elif (poz[i + 12] == 0 and poz[i + 8] == 0 and poz[i + 4] != poz[i]):
                poz[i + 12] = poz[i + 4]
                poz[i + 8] = poz[i]
                poz[i + 4] = 0
                poz[i] = 0
            elif (poz[i + 12] != poz[i + 4] and poz[i + 8] == 0 and poz[i + 12] != 0 and poz[i + 4] != 0):
                poz[i + 8] = poz[i + 4]
                poz[i + 4] = poz[i]
                poz[i] = 0
            elif (poz[i + 12] != poz[i + 8] and poz[i + 12] != 0 and poz[i + 4] == 0 and poz[i] != poz[i + 8] and poz[
                i] != 0):
                poz[i + 4] = poz[i]
                poz[i] = 0
            elif (poz[i + 12] == 0 and poz[i + 8] == 0 and poz[i + 4] != 0 and poz[i + 4] != poz[i]):
                poz[i + 12] = poz[i + 4]
                poz[i + 8] = poz[i]
                poz[i + 4] = 0
                poz[i] = 0
            elif (poz[i + 12] != poz[i + 4] and poz[i + 12] != 0 and poz[i + 4] != 0 and poz[i + 8] == 0):
                poz[i + 8] = poz[i + 4]
                poz[i + 4] = poz[i]
                poz[i] = 0
            elif (poz[i + 12] == 0 and poz[i + 8] != poz[i + 4] and poz[i + 4] != poz[i]):
                poz[i + 12] = poz[i + 8]
                poz[i + 8] = poz[i + 4]
                poz[i + 4] = poz[i]
                poz[i] = 0
            else:
                blok = blok + 1

    elif (x == 'd'):
        for i in range(0, 13, 4):
            if (poz[i] == poz[i + 3] and poz[i + 2] == 0 and poz[i + 1] == 0 and poz[i + 3] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i] != 0 and poz[i + 3] == 0 and poz[i + 2] == 0 and poz[i + 1] == 0):
                poz[i + 3] = poz[i]
                poz[i] = 0
            elif (poz[i] == poz[i + 2] and poz[i + 3] == 0 and poz[i + 1] == 0 and poz[i + 2] != 0):
                poz[i + 3] = poz[i] * 2
                poz[i + 2] = 0
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i] != poz[i + 2] and poz[i + 1] == 0 and poz[i + 3] == 0 and poz[i] != 0 and poz[
                i + 2] != 0):
                poz[i + 3] = poz[i + 2]
                poz[i + 2] = poz[i]
                poz[i] = 0
            elif (poz[i] == poz[i + 1] and poz[i + 3] == poz[i + 2] and poz[i + 3] != 0 and poz[i + 1] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i + 2] = poz[i + 1] * 2
                poz[i + 1] = 0
                poz[i] = 0
                score = score + poz[i + 3] + poz[i + 2]
            elif (poz[i] == poz[i + 1] and poz[i + 3] == 0 and poz[i + 2] == 0 and poz[i + 1] != 0):
                poz[i + 3] = poz[i] * 2
                poz[i + 1] = 0
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i] == poz[i + 1] and poz[i + 2] == 0 and poz[i + 3] != 0 and poz[i + 3] != poz[i + 1] and poz[
                i + 1] != 0):
                poz[i + 2] = poz[i + 1] * 2
                poz[i + 1] = 0
                poz[i] = 0
                score = score + poz[i + 2]
            elif (poz[i] == poz[i + 2] and poz[i + 3] != 0 and poz[i + 3] != poz[i] and poz[i + 1] == 0 and poz[
                i + 2] != 0):
                poz[i + 2] = poz[i + 2] * 2
                poz[i] = 0
                score = score + poz[i + 2]
            elif (poz[i + 3] == poz[i + 2] and poz[i + 1] != 0 and poz[i + 3] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i + 2] = poz[i + 1]
                poz[i + 1] = poz[i]
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i + 1] == poz[i + 2] and poz[i + 3] == 0 and poz[i + 2] != 0):
                poz[i + 3] = poz[i + 2] * 2
                poz[i + 2] = poz[i]
                poz[i + 1] = 0
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i + 1] == poz[i + 2] and poz[i + 3] != 0 and poz[i + 2] != 0):
                poz[i + 2] = poz[i + 2] * 2
                poz[i + 1] = poz[i]
                poz[i] = 0
                score = score + poz[i + 2]
            elif (poz[i + 3] != poz[i + 2] and poz[i + 2] == poz[i + 1] and poz[i + 3] != 0 and poz[i + 2] != 0):
                poz[i + 2] = poz[i + 2] * 2
                poz[i + 1] = poz[i]
                poz[i] = 0
                score = score + poz[i + 2]
            elif (poz[i] == poz[i + 1] and poz[i + 3] != 0 and poz[i + 2] != 0 and poz[i + 3] != poz[i + 2] and poz[
                i + 1] != 0):
                poz[i + 1] = poz[i + 1] * 2
                poz[i] = 0
                score = score + poz[i + 1]
            elif (poz[i] == poz[i + 1] and poz[i + 3] == 0 and poz[i + 2] != 0):
                poz[i + 3] = poz[i + 2]
                poz[i + 2] = poz[i + 1] * 2
                poz[i + 1] = 0
                poz[i] = 0
                score = score + poz[i + 2]
            elif (poz[i + 1] == poz[i + 3] and poz[i + 2] == 0 and poz[i + 3] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i + 1] = 0
                poz[i + 2] = poz[i]
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i + 2] == poz[i + 3] and poz[i + 1] == 0 and poz[i + 3] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i + 2] = poz[i]
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i + 2] == poz[i + 3] and poz[i + 1] != 0 and poz[i + 3] != 0):
                poz[i + 3] = poz[i + 3] * 2
                poz[i + 2] = poz[i + 1]
                poz[i + 1] = poz[i]
                poz[i] = 0
                score = score + poz[i + 3]
            elif (poz[i + 3] != poz[i] and poz[i + 2] == 0 and poz[i + 1] == 0 and poz[i] != 0 and poz[i + 3] != 0):
                poz[i + 2] = poz[i]
                poz[i + 1] = 0
                poz[i] = 0
            elif (poz[i + 3] != poz[i] and poz[i + 2] != 0 and poz[i + 1] == 0 and poz[i] != 0 and poz[i + 3] != 0):
                poz[i + 1] = poz[i]
                poz[i] = 0
            elif (poz[i] != poz[i + 2] and poz[i + 2] != 0 and poz[i] != 0 and poz[i + 1] == 0 and poz[
                i + 3] == 0):
                poz[i + 3] = poz[i + 2]
                poz[i + 2] = poz[i]
                poz[i] = 0
            elif (poz[i] != poz[i + 2] and poz[i + 2] != 0 and poz[i] != 0 and poz[i + 2] != poz[i + 3] and poz[
                i + 1] == 0 and poz[i + 3] != 0):
                poz[i + 1] = poz[i]
                poz[i] = 0
            elif (poz[i + 3] == 0 and poz[i + 2] == 0 and poz[i + 1] != poz[i]):
                poz[i + 3] = poz[i + 1]
                poz[i + 2] = poz[i]
                poz[i + 1] = 0
                poz[i] = 0
            elif (poz[i + 3] != poz[i + 1] and poz[i + 2] == 0 and poz[i + 3] != 0 and poz[i + 1] != 0):
                poz[i + 2] = poz[i + 1]
                poz[i + 1] = poz[i]
                poz[i] = 0
            elif (poz[i + 3] != poz[i + 2] and poz[i + 3] != 0 and poz[i + 1] == 0 and poz[i] != poz[i + 2] and poz[
                i] != 0):
                poz[i + 1] = poz[i]
                poz[i] = 0
            elif (poz[i + 3] == 0 and poz[i + 2] == 0 and poz[i + 1] != 0 and poz[i + 1] != poz[i]):
                poz[i + 3] = poz[i + 1]
                poz[i + 2] = poz[i]
                poz[i + 1] = 0
                poz[i] = 0
            elif (poz[i + 3] != poz[i + 1] and poz[i + 3] != 0 and poz[i + 1] != 0 and poz[i + 2] == 0):
                poz[i + 2] = poz[i + 1]
                poz[i + 1] = poz[i]
                poz[i] = 0
            elif (poz[i + 3] == 0 and poz[i + 2] != poz[i + 1] and poz[i + 1] != poz[i]):
                poz[i + 3] = poz[i + 2]
                poz[i + 2] = poz[i + 1]
                poz[i + 1] = poz[i]
                poz[i] = 0
            else:
                blok = blok + 1

    elif (x == 'a'):
        for i in range(0, 13, 4):
            if (poz[i + 3] == poz[i] and poz[i + 1] == 0 and poz[i + 2] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 3] != 0 and poz[i] == 0 and poz[i + 1] == 0 and poz[i + 2] == 0):
                poz[i] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i + 3] == poz[i + 1] and poz[i] == 0 and poz[i + 2] == 0 and poz[i + 1] != 0):
                poz[i] = poz[i + 3] * 2
                poz[i + 1] = 0
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 3] != poz[i + 1] and poz[i + 2] == 0 and poz[i] == 0 and poz[i + 3] != 0 and poz[
                i + 1] != 0):
                poz[i] = poz[i + 1]
                poz[i + 1] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i + 3] == poz[i + 2] and poz[i] == poz[i + 1] and poz[i] != 0 and poz[i + 2] != 0):
                poz[i] = poz[i] * 2
                poz[i + 1] = poz[i + 2] * 2
                poz[i + 2] = 0
                poz[i + 3] = 0
                score = score + poz[i] + poz[i + 1]
            elif (poz[i + 3] == poz[i + 2] and poz[i] == 0 and poz[i + 1] == 0 and poz[i + 2] != 0):
                poz[i] = poz[i + 3] * 2
                poz[i + 2] = 0
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 3] == poz[i + 2] and poz[i + 1] == 0 and poz[i] != 0 and poz[i] != poz[i + 2] and poz[
                i + 2] != 0):
                poz[i + 1] = poz[i + 2] * 2
                poz[i + 2] = 0
                poz[i + 3] = 0
                score = score + poz[i + 1]
            elif (poz[i + 3] == poz[i + 1] and poz[i] != 0 and poz[i] != poz[i + 3] and poz[i + 2] == 0 and poz[
                i + 1] != 0):
                poz[i + 1] = poz[i + 1] * 2
                poz[i + 3] = 0
                score = score + poz[i + 1]
            elif (poz[i] == poz[i + 1] and poz[i + 2] != 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 1] = poz[i + 2]
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 2] == poz[i + 1] and poz[i] == 0 and poz[i + 1] != 0):
                poz[i] = poz[i + 1] * 2
                poz[i + 1] = poz[i + 3]
                poz[i + 2] = 0
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 2] == poz[i + 1] and poz[i] != 0 and poz[i + 1] != 0):
                poz[i + 1] = poz[i + 1] * 2
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i + 1]
            elif (poz[i] != poz[i + 1] and poz[i + 1] == poz[i + 2] and poz[i] != 0 and poz[i + 1] != 0):
                poz[i + 1] = poz[i + 1] * 2
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i + 1]
            elif (poz[i + 3] == poz[i + 2] and poz[i] != 0 and poz[i + 1] != 0 and poz[i] != poz[i + 1] and poz[
                i + 2] != 0):
                poz[i + 2] = poz[i + 2] * 2
                poz[i + 3] = 0
                score = score + poz[i + 2]
            elif (poz[i + 3] == poz[i + 2] and poz[i] == 0 and poz[i + 1] != 0):
                poz[i] = poz[i + 1]
                poz[i + 1] = poz[i + 2] * 2
                poz[i + 2] = 0
                poz[i + 3] = 0
                score = score + poz[i + 1]
            elif (poz[i + 2] == poz[i] and poz[i + 1] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 2] = 0
                poz[i + 1] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 1] == poz[i] and poz[i + 2] == 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 1] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i + 1] == poz[i] and poz[i + 2] != 0 and poz[i] != 0):
                poz[i] = poz[i] * 2
                poz[i + 1] = poz[i + 2]
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
                score = score + poz[i]
            elif (poz[i] != poz[i + 3] and poz[i + 1] == 0 and poz[i + 2] == 0 and poz[i + 3] != 0 and poz[i] != 0):
                poz[i + 1] = poz[i + 3]
                poz[i + 2] = 0
                poz[i + 3] = 0
            elif (poz[i] != poz[i + 3] and poz[i + 1] != 0 and poz[i + 2] == 0 and poz[i + 3] != 0 and poz[i] != 0):
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i + 3] != poz[i + 1] and poz[i + 1] != 0 and poz[i + 3] != 0 and poz[i + 2] == 0 and poz[
                i] == 0):
                poz[i] = poz[i + 1]
                poz[i + 1] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i + 3] != poz[i + 1] and poz[i + 1] != 0 and poz[i + 3] != 0 and poz[i + 1] != poz[i] and poz[
                i + 2] == 0 and poz[i] != 0):
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i] == 0 and poz[i + 1] == 0 and poz[i + 2] != poz[i + 3]):
                poz[i] = poz[i + 2]
                poz[i + 1] = poz[i + 3]
                poz[i + 2] = 0
                poz[i + 3] = 0
            elif (poz[i] != poz[i + 2] and poz[i + 1] == 0 and poz[i] != 0 and poz[i + 2] != 0):
                poz[i + 1] = poz[i + 2]
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i] != poz[i + 1] and poz[i] != 0 and poz[i + 2] == 0 and poz[i + 3] != poz[i + 1] and poz[
                i + 3] != 0):
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i] == 0 and poz[i + 1] == 0 and poz[i + 2] != 0 and poz[i + 2] != poz[i + 3]):
                poz[i] = poz[i + 2]
                poz[i + 1] = poz[i + 3]
                poz[i + 2] = 0
                poz[i + 3] = 0
            elif (poz[i] != poz[i + 2] and poz[i] != 0 and poz[i + 2] != 0 and poz[i + 1] == 0):
                poz[i + 1] = poz[i + 2]
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            elif (poz[i] == 0 and poz[i + 1] != poz[i + 2] and poz[i + 2] != poz[i + 3]):
                poz[i] = poz[i + 1]
                poz[i + 1] = poz[i + 2]
                poz[i + 2] = poz[i + 3]
                poz[i + 3] = 0
            else:
                blok = blok + 1
    elif (x == '0' or x.lower() == 'exit'):
        exit()
    else:
        blok = 4
